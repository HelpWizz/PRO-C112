import os
import shutil
from_dir, to_dir = "C:/Users/seane/Downloads", "C:/Users/seane/OneDrive/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)

for i in list_of_files:
    file_name, ext = os.path.splitext(i)

    if ext == "":
        continue
    
    if ext in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1, path3)