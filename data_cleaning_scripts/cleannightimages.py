import os 
import shutil

# Trashing night images

source = '/home/pf/pfshare/data/MA_Rajanie/Data/Lake_Ice_Dataset_17-18/Sihl/Cam9'
trash = '/home/prabhar/.local/share/Trash'
for file in os.listdir(source):
    x = file.split("_")[1]
    #y = x.split("--")[1].split("-")[0]
    #print(y)
    if int(x) >= 18 or int(x) <= 7:
        shutil.move(os.path.join(source, file), trash)
        print("trashed")
