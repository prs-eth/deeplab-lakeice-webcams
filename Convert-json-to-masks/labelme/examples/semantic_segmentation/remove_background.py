#!/usr/bin/env python

from __future__ import print_function

import argparse
import os
import os.path as osp
import sys

import numpy as np
from PIL import Image

import labelme
import PIL.Image
import cv2

## Using the lake detection image masks on creating masks on all images in the dataset

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--input_dir_images',default='/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/crowdsourced_voc/Images/',help='input annotated directory')
    parser.add_argument('--input_dir_masks',default='/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/crowdsourced_voc/labels/',help='input annotated directory')
    parser.add_argument('--output_dir', default='/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/crowdsourced_voc/Images_withoutBG/', help='output dataset directory')

    args = parser.parse_args()



    for label_file in os.listdir(args.input_dir_masks):
        image_file = label_file.strip("png") + "jpg"
        
        label = Image.open(os.path.join(args.input_dir_masks,label_file), 'r')
        pixels_label = list(label.getdata())
        label_ = label.load()

        im = Image.open(os.path.join(args.input_dir_images,image_file), 'r')
        pixels_im = list(im.getdata())
        image_old = im.load()

        for i in range(im.size[0]):    # for every col:
            for j in range(im.size[1]):    # For every row
                if (label_[i,j]) == 0:
                    image_old[i, j] = 0

        out_img_file = osp.join(args.output_dir, label_file)        
        print('Generating dataset from:', label_file)
        im.save(out_img_file, format='PNG')



if __name__ == '__main__':
    main()
