# !/usr/bin/env python3
#  -*- coding: utf-8 -*-

import tensorflow as tf
from PIL import Image
from tqdm import tqdm
import numpy as np
import cv2

import os, shutil

# palette (color map) describes the (R, G, B): Label pair
palette = {(0, 0, 0): 0,
           (127, 127, 127): 1,
           (191, 191, 191): 2,
           (255, 255, 255): 3,
           (64, 64, 64): 4
           }


def convert_from_color_segmentation(arr_3d):
    arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)

    for c, i in palette.items():
        m = np.all(arr_3d == np.array(c).reshape(1, 1, 3), axis=2)
        arr_2d[m] = i
    return arr_2d


dataset_nbr = [300]

for i in range(len(dataset_nbr)):

    label_dir = '/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/Images_cropped_bottom/'
    new_label_dir = '/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/check/'

    if not os.path.isdir(new_label_dir):
        print("creating folder: ", new_label_dir)
        os.mkdir(new_label_dir)
    else:
        print("Folder already exists. Delete the folder and re-run the code!!!")

    label_files = os.listdir(label_dir)

    for l_f in tqdm(label_files):
        arr = cv2.imread(label_dir + l_f)
        print(arr.shape)
        arr = arr[:, :, 0:3]
        arr_2d = convert_from_color_segmentation(arr)
        Image.fromarray(arr_2d).save(new_label_dir + l_f)




