from skimage import draw
from skimage import io
import numpy as np
import urllib.request
import json
import logging
import os
import sys
import PIL.Image
import argparse

#enable info logging.
logging.getLogger().setLevel(logging.INFO)

def poly2mask(blobs,path_to_masks_folder, h, w, label, idx, filename):
    mask = np.zeros((h, w))
    for l in blobs:
        fill_row_coords, fill_col_coords = draw.polygon(l[1], l[0], l[2])
        mask[fill_row_coords, fill_col_coords] = 128
    io.imsave(path_to_masks_folder + "/" + filename + ".png", mask)


def convert_dataturks_to_masks(path_to_dataturks_annotation_json, path_to_original_images_folder, path_to_masks_folder):
    # make sure everything is setup.
    if (not os.path.isdir(path_to_original_images_folder)):
        logging.exception(
            "Please specify a valid directory path to download images, " + path_to_original_images_folder + " doesn't exist")
        return
    if (not os.path.isdir(path_to_masks_folder)):
        logging.exception(
            "Please specify a valid directory path to write mask files, " + path_to_masks_folder + " doesn't exist")
        return
    if (not os.path.exists(path_to_dataturks_annotation_json)):
        logging.exception(
            "Please specify a valid path to dataturks JSON output file, " + path_to_dataturks_annotation_json + " doesn't exist")
        return

    for fil in os.listdir(path_to_dataturks_annotation_json):
        if fil.endswith(".json"):
            img_file = fil.replace(".json", ".jpg")
            filename = (img_file.strip(".jpg"))
            img = np.asarray(PIL.Image.open(os.path.join(path_to_dataturks_annotation_json, img_file)))
            f = open(os.path.join(path_to_dataturks_annotation_json, fil))
            data = json.load(f)

            blobs = []
            classes = {}

            annotations = data["shapes"]

            for i in range(1):
                blobs = []
                label = annotations[0]["label"]
                
                if (label != ''):
                    if label not in classes:
                        classes[label] = 0
                    print(classes)

                    points = annotations[0]["points"]
                    h = data["imageHeight"]
                    w = data["imageWidth"]
                    x_coord = []
                    y_coord = []
                    l = []
                    for p in points:
                        x_coord.append(p[0])
                        y_coord.append(p[1])
                    shape = (h, w)
                    l.append(x_coord)
                    l.append(y_coord)
                    l.append(shape)
                    blobs.append(l)
                    poly2mask(blobs, path_to_masks_folder, data['imageHeight'], data['imageWidth'], label,
                          classes[label],filename)
                   # classes[label] += 1


def main():
    print(
    "Please provide path to dataturks json file, path to store ground truth images and path to store mask images in this order.")

convert_dataturks_to_masks(sys.argv[1], sys.argv[1], sys.argv[2])
