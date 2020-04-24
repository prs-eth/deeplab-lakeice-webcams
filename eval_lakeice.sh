#!/usr/bin/env bash

cd ..
# Set up the working environment.
CURRENT_DIR=$(pwd)
WORK_DIR="${CURRENT_DIR}/deeplab"
DATASET_DIR="datasets"

# Set up the working directories.
LAKEICE_FOLDER="lake"
EXP_FOLDER="exp/ptz_downsampled_cam1"
INIT_FOLDER="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/init_models"
TRAIN_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/train"
EVAL_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/eval"
VIS_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/vis"
LOGITS_LOGDIR="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/${EXP_FOLDER}/logits"

#mkdir -p "${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/exp"
mkdir -p "${EVAL_LOGDIR}"
mkdir -p "${VIS_LOGDIR}"
mkdir -p "${LOGITS_LOGDIR}"

LAKEICE_DATASET="${WORK_DIR}/${DATASET_DIR}/${LAKEICE_FOLDER}/ptz_cam1_resized_324x1209_tfrecord"

NUM_ITERATIONS=100000

#Saving hyperparameters
# cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/train_lakeice.sh ${TRAIN_LOGDIR}/
# cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/train.py ${TRAIN_LOGDIR}/
# cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/utils/train_utils.py ${TRAIN_LOGDIR}/
# cp /home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/eval.py ${TRAIN_LOGDIR}/

##  Comments on changes done
## --model_variant="xception_skips" if you want to use the model with skips from encoder to decoder, "xception_65 otherwise
## --skips=1 if you want 4 extra skip concat layers from encoder to decoder, 0 otherwise

 
python3 "${WORK_DIR}"/eval.py \
  --logtostderr \
  --eval_split="val" \
  --model_variant="xception_65" \
  --skips=0 \
  --atrous_rates=12 \
  --atrous_rates=18 \
  --atrous_rates=24 \
  --output_stride=8 \
  --decoder_output_stride=4 \
  --eval_crop_size="325,1210" \
  --dataset="lake" \
  --checkpoint_dir="${TRAIN_LOGDIR}" \
  --eval_logdir="${EVAL_LOGDIR}" \
  --dataset_dir="${LAKEICE_DATASET}" \
  --max_number_of_evaluations=1

  #,1081,1921

# # Visualize the results.
python3 "${WORK_DIR}"/vis.py \
  --logtostderr \
  --vis_split="val" \
  --model_variant="xception_65" \
  --atrous_rates=12 \
  --atrous_rates=18 \
  --atrous_rates=24 \
  --output_stride=8 \
  --decoder_output_stride=4 \
  --vis_crop_size="325,1210"  \
  --checkpoint_dir="${TRAIN_LOGDIR}" \
  --vis_logdir="${EVAL_LOGDIR}" \
  --logits_file="${LOGITS_LOGDIR}" \
  --dataset="lake" \
  --dataset_dir="${LAKEICE_DATASET}" \
  --colormap_type="lake" \
  --max_number_of_iterations=1


##Export the trained checkpoint.
# CKPT_PATH="${TRAIN_LOGDIR}/model.ckpt-${NUM_ITERATIONS}"
# EXPORT_PATH="${EXPORT_DIR}/frozen_inference_graph.pb"

# python3 "${WORK_DIR}"/export_model.py \
#   --logtostderr \
#   --checkpoint_path="${CKPT_PATH}" \
#   --export_path="${EXPORT_PATH}" \
#   --model_variant="xception_65_skips" \
#   --atrous_rates=12 \
#   --atrous_rates=24 \
#   --atrous_rates=36 \
#   --output_stride=8 \
#   --decoder_output_stride=4 \
#   --num_classes=5 \
#   --inference_scales=1.0

 #######################################
#Lake Detection params
#python3 "${WORK_DIR}"/train.py \
#  --logtostderr \
#  --train_split="trainval" \
#  --model_variant="xception_65" \
#  --atrous_rates=6 \
#  --atrous_rates=12 \
#  --atrous_rates=18 \
#  --output_stride=16 \
#  --decoder_output_stride=4 \
#  --train_crop_size="321,321" \
#  --dataset="lake" \
#  --train_batch_size=8 \
#  --training_number_of_steps="${NUM_ITERATIONS}" \
#  --fine_tune_batch_norm=false \
#  --train_logdir="${TRAIN_LOGDIR}" \
#  --base_learning_rate=9e-5 \
#  --learning_policy="poly" \
#  --tf_initial_checkpoint="/home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/datasets/lake/init_models/deeplabv3_pascal_train_aug/model.ckpt" \
#  --dataset_dir="${LAKEICE_DATASET}"
