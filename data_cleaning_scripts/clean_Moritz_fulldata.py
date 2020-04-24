import os
import shutil
import sys

## Removing images before 6 am and after 5 pm from the PTZ images

source = sys.argv[1]
dest = '/home/pf/pfshare/data/MA_Rajanie/Data/PTZ_notuseful'

for file in os.listdir(source):
    if file.startswith('img'):
        time = file.split('_')
        hour = time[1].split('--')[1].split('-')
        print(hour[0])
        if int(hour[0]) <= 6 or int(hour[0]) >= 17:
            shutil.move(os.path.join(source,file), dest)
            print("file moved")



