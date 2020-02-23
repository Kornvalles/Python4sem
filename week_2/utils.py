# 3
import os

def filenames_from_folder(folder_path, output_file):
    with open(output_file, "w") as f_obj:
        for file in os.listdir(folder_path):
            f_obj.write(file + "\n")


#filenames_from_folder("/Users/mikkel/first-app", "./tmp.txt")

def 