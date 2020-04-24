import os
from PIL import Image

output_path = '/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/resized_labels'
path='/home/pf/pfshare/data/MA_Rajanie/Convert_json_to_PNG_masks/labelme/examples/semantic_segmentation/PTZ_Cam1_voc/SegmentationClassPNG'


for file in os.listdir(path):

 
    if file.endswith('png'):
        im = Image.open(os.path.join(path,file))
        new_img = im.resize((1209,324))
        new_img.save(os.path.join(output_path,file), "PNG", optimize=True)
        print("yes")
print("Done")
