# Lake Ice Monitoring with Webcams and Crowd-Sourced Images

This repository provides the implementation (tensorflow), pre-trained model and dataset corresponding to the paper:<br>

>[Lake Ice Monitoring with Webcams and Crowd-​Sourced Images](https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/V-2-2020/549/2020/) (presented at the ISPRS Congress, 2020, virtual conference)<br>
> by Rajanie Prabha, Manu Tom, Mathias Rothermel, Emmanuel Baltsavias, Laura Leal-Taixe and Konrad Schindler

![Lake Detection and Lake Ice Monitoring](images/lakeice_webcams.png)

This work is part of the [Lake Ice Project (Phase 2)](https://prs.igp.ethz.ch/research/current_projects/integrated-lake-ice-monitoring-and-generation-of-sustainable--re.html)  funded by MeteoSwiss in the GCOS Switzerland framework. Here is the link to [Phase 1](https://prs.igp.ethz.ch/research/completed_projects/integrated-monitoring-of-ice-in-selected-swiss-lakes.html) of the same project. 

## What this repo contains?
1. Deeplab v3+ tensorflow model adopted from official tensorflow repository with some changes.
  (a). Code for calculating Individual class IoU. 
  (b). Code for checking confusion matrix on tensorboard.
  (c). Updated xception_65 model with extra skips from encoder to decoder.
2. Using labelme tool to create data annotations and code for converting json annotations to color-indexed masks.
3. Some data cleaning scripts (only valid for our Photi-LakeIce dataset).
4. Jupyter Notebook for visualizing data distribution for 5 classes : background, water, ice, snow, clutter.
5. Jupyter Notebook for inference using a saved tensorflow checkpoint.

## Steps to reproduce the experiment.

Data
Folder structure:
  ```bash
├── datasets
    ├── lake
        ├── JPEGImages
        ├── SegmentationClassPNG
        ├── SegmentationClassRaw
        ├── Imagesets
            ├── train.txt
            ├── val.txt
        ├── abc.tfrecord

```
1. Place the Images in JPEGImages and segmentation color masks in SegmentationClassPNG. Run remove_gt_colormap_lakeice.py to covert the RGB color codes to class number, i.e. 0 for Background, 1 for Water, 2 for Ice, and so on. Take care of paths label_dir (SegmentationClassPNG directory) and new_label_dir (SegmentationClassRaw directory).
2. Create a folder Imagesets which contains the train.txt (training image sample names) and val.txt (testing image sample names) files. Refer sampletrain.txt in datasets folder to see how the txt files look.
3. Update data_generator.py file. Specifically, update the numbers for train samples and val samples in _LAKEICE_INFORMATION.
3. Now, Convert data into tensorflow record by running bash script download_and_convert_lakeice.sh (Take care of the directory paths in the script).

Voila, now you have the dataset to train your model.


By simply running the train_lakeice.sh, the training will start.
For parameters: the specified values were used for all experiments.
1. Setup up the tensorflow records in LAKEICE_DATASET parameter.
2. --model_variant="xception_65" -> Change to "xception_65_skips" to use Deep-U-Lab 
   --skips=0                     -> Change to 1, if using "xception_65_skips" 
   --atrous_rates=6 
   --atrous_rates=12 
   --atrous_rates=18 
   --output_stride=16 
   --decoder_output_stride=4 
   --train_crop_size="321,321"   -> Used 512,512 for lake-detection and 321,321 for lake-ice segmentation 
   --dataset="lake" 
   --train_batch_size=8          -> Set according to GPU availability. This should be >=16 for tuning the batch norm layers 
   --training_number_of_steps="${NUM_ITERATIONS}"
   --fine_tune_batch_norm=false  -> Set to "true" if train_batch_size>=16 
   --train_logdir="${TRAIN_LOGDIR}" 
   --base_learning_rate=0.0001 
   --learning_policy="poly" 
   --tf_initial_checkpoint="/your_checkpoint_folder_name/model.ckpt" (You may update this!) 
   --dataset_dir="${LAKEICE_DATASET}" 
   

For evaluation and visualization, run the eval_lakeice.sh script.
  
   --eval_split="val"             -> Split should be "val", instead of "train" 
   --model_variant="xception_65"  -> Same rules as train script
   --skips=0 
   --eval_crop_size="325,1210"    -> Full image eval_crop_size 
   --max_number_of_evaluations=1  -> If set to 1, evaluation script will run once and exit. If >1, it will keep checking the train logdir for new checkpoints. Useful, when running both train and eval scripts simultaneously (alloting part of GPU to both). 

## Pre-trained model
[Download](https://share.phys.ethz.ch/~pf/tommdata/Pre-trained_Model.tar.xz) the model pre-trained on Lake St. Moritz data (Cam0, winter 2016-17) from the [Photi-LakeIce dataset](https://github.com/czarmanu/photi-lakeice-dataset). Approximate size: 146 MB

## Beware of some common bugs.
1. for no modules called nets.
   Get the 'slim' directory from https://github.com/tensorflow/models/tree/master/research and from the research folder, run 
   ```python
   export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
   ```
2. Iterator end of line error.
   Look for empty lines in the dataset/"your dataset"/List/"train or val".txt files.
  
3. Dataset split  in train.py and eval.py, be careful to not use the default "trainval" split from original tensorflow deeplab    repository.

## Citation
Please cite our paper, if you use this repo:

>@inproceedings{prabha_tom_2020:isprs,<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;author={Rajanie Prabha and Manu Tom and Mathias Rothermel and Emmanuel Baltsavias and Laura Leal-Taixe and Konrad Schindler},<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;title={Lake Ice Monitoring with Webcams and Crowd-Sourced Images},<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;booktitle={ISPRS Ann. Photogramm. Remote Sens. Spatial Inf. Sci.},<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;year={2020},<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;volume={V-2-2020},<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pages={549–556},<br>
>}

## Useful links
1. Photi-Lake Ice Dataset ([Github repo](https://github.com/czarmanu/photi-lakeice-dataset))
2. Multi-sensor lake ice monitoring with machine (deep) learning. [Project github page](https://github.com/czarmanu/lake-ice-ml).
3. Lake ice detection from Sentinel-1 SAR with deep learning. [Github repo (tensorflow code, pre-trained model)](https://github.com/czarmanu/sentinel_lakeice). [Paper](https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/V-3-2020/409/2020/) 
4. Tom, M., Suetterlin, M., Bouffard, D., Rothermel, M., Wunderle, S., Baltsavias, E., 2019. [Integrated monitoring of ice in selected Swiss lakes](https://arxiv.org/abs/2008.00512). Final Project Report
5. Tom et al. 2020, [Ice monitoring in Swiss lakes from optical satellites and webcams using machine learning](https://www.mdpi.com/2072-4292/12/21/3555), MDPI Remote Sensing, 12(21), 3555
6. [Deeplab v3+](https://github.com/tensorflow/models/tree/master/research/deeplab) 

## Licence

MIT License

Copyright (c) 2020 ETH Zurich

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: Manu Tom
