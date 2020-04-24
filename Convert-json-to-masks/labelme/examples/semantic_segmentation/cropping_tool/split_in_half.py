# Improting Image class from PIL module 
from PIL import Image 
import os
  
# Opens a image in RGB mode 
path = "/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/JPEGImages"
output = "/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/Images_patches"


# Read the image

for file in os.listdir(path):
    im = Image.open(os.path.join(path,file))
    width, height = im.size

    # Cut the image in half
    width_cutoff = width // 2


    left1 = 0
    top1  = 0
    right1 = width // 2
    bottom1 = 380

    left2 = width // 2
    top2 = 0
    right2 = 1370
    bottom2 = 380
  

    im1 = im.crop((left1, top1, right1, bottom1)) 
    im2 = im.crop((left2, top2, right2, bottom2)) 
  
    # saves the cropped image 
    im1.save(os.path.join(output,str(file).strip(".jpg")+"split1.png"))
    im2.save(os.path.join(output,str(file).strip(".jpg")+"split2.png"))
    

