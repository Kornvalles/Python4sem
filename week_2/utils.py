# Exercise 2
import os
import sys

# 1
def filenames_from_folder(folder_path, output_file):
    with open(output_file, "w") as f_obj:
        for file in os.listdir(folder_path):
            f_obj.write(file + "\n")


# filenames_from_folder("/Users/mikkel/first-app", "./tmp.txt")

# 2
def filename_recursively(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        print(dirpath, filenames)
        for dirname in dirnames:
            for (dirpath, dirnames, filenames) in os.walk(dirname):
                print(filenames)


# filename_recursively("/Users/mikkel/Downloads")

# 3
def first_line_filenames(filenames):
    for file in filenames:
        with open(file) as r_obj:
            print(r_obj.readline())


files = ["../output.txt", "../outputfile.txt"]
# first_line_filenames(files)

# 4
def if_contains(filenames):
    for file in filenames:
        with open(file) as r_obj:
            for line in r_obj.readlines():
                if '@' in line:
                    print(line)

# if_contains(files)

# 5
def headlines(macdowns):
    for md in macdowns:
        with open(md) as md_obj:
            for line in md_obj.readlines():
                if '#' in line:
                    with open("./md_temp.txt", 'a') as a_obj:
                        a_obj.write(line + "\n")

macdowns = ["one.md", "two.md", "three.md"]
headlines(macdowns)

""" if __name__ == '__main__':
    filenames_from_folder(sys.argv[1:]) """