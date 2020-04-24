#!/bin/bash
# Copyright 2018 The TensorFlow Authors All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
# Script to download and preprocess the PASCAL VOC 2012 dataset.
#
# Usage:
#   bash ./download_and_convert_voc2012.sh
#
# The folder structure is assumed to be:
#  + datasets
#     - build_data.py
#     - build_lakeice.py
#     - download_and_convert_voc2012.sh
#     - remove_gt_colormap.py
#     + pascal_voc_seg
#       + VOCdevkit
#         + VOC2012
#           + JPEGImages
#           + SegmentationClass
#

# Exit immediately if a command exits with a non-zero status.

CURRENT_DIR=$(pwd)
WORK_DIR="/home/pf/pfshare/data/MA_Rajanie/models/research/deeplab/datasets/lake"
PQR_ROOT="${WORK_DIR}"
SEG_FOLDER="${PQR_ROOT}/SegmentationClassRaw"
#SEG_FOLDER="/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/labels_cropped_raw"
#SEMANTIC_SEG_FOLDER="${PQR_ROOT}/SegmentationClass"
# Build TFRecords of the dataset.
OUTPUT_DIR="${WORK_DIR}/nonptz_all_except_sihl_1617_tfrecord"
mkdir -p "${OUTPUT_DIR}"
#IMAGE_FOLDER="/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/Images_cropped"
IMAGE_FOLDER="${PQR_ROOT}/JPEGImages"
LIST_FOLDER="${PQR_ROOT}/nonptz_all_except_sihl_1617"
#LIST_FOLDER="/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/ptz_cam1_cropped_topbottom_325x1209"
echo "Converting lakeice dataset..."
python3 ./build_lakeice.py \
  --image_folder="${IMAGE_FOLDER}" \
  --semantic_segmentation_folder="${SEG_FOLDER}" \
  --list_folder="${LIST_FOLDER}" \
  --image_format="png" \
  --output_dir="${OUTPUT_DIR}"
