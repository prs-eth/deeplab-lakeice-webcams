import os
from PIL import Image
import csv
import pandas as pd
import numpy as np
import glob
import re

path = "/home/pf/pfshare/data/MA_Rajanie/raw_labels/moritz_cam0_16-17_preds"
dates=[] 
dictionary = {}
per_day_analysis = []

for file in os.listdir(path):
    im=Image.open(os.path.join(path, file))
    match = re.search(r'\d{4}_\d{4}', file).group()
    #print(match)
    
    
    water =snow=ice=extra=0
    
    pixels = list(im.getdata())
    for i in pixels:
        if i == 1:
            water+=1
        elif i == 2:
            ice+=1
        elif i==3:
            snow+=1
        else:
            extra ==1
    
    #print(water, ice, snow)
    lake= water+ice+snow
    coverage = round(float((ice+snow)/(ice+snow+0.001)), 2)
    if match in dictionary.keys():
        dictionary[match].append(coverage)
    else:
        dictionary[match] = [coverage]

for key, values in dictionary.items():
    dates.append(key)
    per_day_analysis.append(np.median(values))



#print(dictionary)

data=np.array([dates,per_day_analysis]).T
df=pd.DataFrame(columns=['date','day_analysis'],data=data)
df.to_csv('/home/pf/pfshare/data/MA_Rajanie/raw_labels/moritz_cam0_16-17_preds.csv',index=False)



        