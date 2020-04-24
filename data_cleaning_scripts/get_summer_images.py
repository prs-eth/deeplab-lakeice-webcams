import os
import shutil

# getting summer images from the whole data folder
source = '/home/pf/pfshare/data/MA_Rajanie/Annotated/lakes/SilserSee/Cam5/all_Images'
dest = '/home/pf/pfshare/data/MA_Rajanie/Annotated/lakes/SilserSee/Cam5/Summer'

for file in os.listdir(source):
    x = file.split("-")
    print(x)
    date = x[1]
    a = [date[i:i+2] for i in range(0, len(date), 2)]
    if int(a[0]) >= 5 and int(a[0]) <= 11:
        shutil.move(os.path.join(source, file), dest)
        print(file, "file moved")

