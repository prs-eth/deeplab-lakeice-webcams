# Improting Image class from PIL module 
from PIL import Image 
import os
  

path = "/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/labels_patches_1"
output = "/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/labels_patches"


# Read the image

for file in os.listdir(path):
    # Opens a image in RGB mode 
    im = Image.open(os.path.join(path,file))
    width, height = im.size

    #coordinates for first split
    left1 = 0
    top1  = 0
    bottom1 = height // 2
    right1 = 480

    #coordinates for first split
    left2 = 0
    top2 = height // 2
    right2 = 480
    bottom2 = 1080
  

    im1 = im.crop((left1, top1, right1, bottom1)) 
    im2 = im.crop((left2, top2, right2, bottom2)) 
  
    # saves the cropped image 
    im1.save(os.path.join(output,str(file).strip(".png")+"split3.png"))
    im2.save(os.path.join(output,str(file).strip(".png")+"split4.png"))
    

