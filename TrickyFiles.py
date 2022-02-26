import os
import shutil

def swap():
    from_file = input("give your file here: ")
    file_to = input("give your swap file here: ")

    shutil.move(file_to,from_file)
    print("Files have been swapped")

swap()