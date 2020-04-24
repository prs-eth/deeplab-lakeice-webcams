#!/usr/bin/env bash

cd ..
# Set up the working environment.
CURRENT_DIR=$(pwd)
WORK_DIR="${CURRENT_DIR}/deeplab"
DATASET_DIR="datasets"

# Set up the working directories.
LAKEICE_FOLDER="lake"
EXP_FOLDER="exp/moritz_cam1_1718"
INIT_FOLDER="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/init_models"
TRAIN_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/train"
EVAL_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/eval"
VIS_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/vis"
EXPORT_DIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/export"

mkdir -p "${TRAIN_LOGDIR}"
mkdir -p "${EVAL_LOGDIR}"
mkdir -p "${VIS_LOGDIR}"

LAKEICE_DATASET="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/Moritz_cam1_17-18_tfrecord"

NUM_ITERATIONS=100000

#Saving hyperparameters
cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/train_lakeice.sh ${TRAIN_LOGDIR}/
cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/train.py ${TRAIN_LOGDIR}/
cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/utils/train_utils.py ${TRAIN_LOGDIR}/
cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/eval.py ${TRAIN_LOGDIR}/

##  Comments on changes done
## --model_variant="xception_skips" if you want to use the model with skips from encoder to decoder, "xception_65 otherwise
## --skips=1 if you want 4 extra skip concat layers from encoder to decoder, 0 otherwise

python3 "${WORK_DIR}"/train.py \
  --logtostderr \
  --train_split="train" \
  --model_variant="xception_65" \
  --skips=0 \
  --atrous_rates=6 \
  --atrous_rates=12 \
  --atrous_rates=18 \
  --output_stride=16 \
  --decoder_output_stride=4 \
  --train_crop_size="321,321" \
  --dataset="lake" \
  --train_batch_size=8 \
  --training_number_of_steps="${NUM_ITERATIONS}" \
  --fine_tune_batch_norm=false \
  --train_logdir="${TRAIN_LOGDIR}" \
  --base_learning_rate=0.0001 \
  --learning_policy="poly" \
  --tf_initial_checkpoint="/home/pf/pfshare/data/MA_Rajanie/pretrained/deeplabv3_pascal_trainval/model.ckpt" \
  --dataset_dir="${LAKEICE_DATASET}"

