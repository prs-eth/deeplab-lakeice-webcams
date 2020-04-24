# Improting Image class from PIL module 
from PIL import Image 
import os
  
# Opens a image in RGB mode 
path = "/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/SegmentationClassPNG/"
o_path = "/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/Images_cropped_bottom/"

for file in os.listdir(path):
    im = Image.open(os.path.join(path,file)) 
    print(file)
    #name =file.split("/")[11]
  
    width, height = im.size 
  
# Setting the points for cropped image 
#for cam0
    #left = 550
    #top = 700
    #right = 1920
    #bottom = 1080
    
#for cam1
    left = 700
    top = 400
    right = 1909
    bottom = 725
  
# Cropped image of above dimension 
# (It will not change orginal image) 
    im1 = im.crop((left, top, right, bottom)) 
  
# Shows the image in image viewer 
    im1.save(os.path.join(o_path,file))
