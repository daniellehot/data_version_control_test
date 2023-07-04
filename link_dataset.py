import os
import shutil
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="full path to the local copy of the dataset")
    parser.add_argument("-o", "--output", type=str, default="data", help="output folder")
    args = parser.parse_args()
    if args.path == None:
        print("Please, provide path to the dataset folder\n     python3 link_dataset.py -p path/to/dataset/")
        exit()
    shutil.copytree(args.path, "data", copy_function=os.link)


    """
    for path, subdirs, files in os.walk(args.path):
        for file in files:
            src = os.path.join(path, file)
            print(src)
            dst = src.replace(args.path, "")
            dst = os.path.join("data", dst)
            shutil.copytree(src, dst, copy_function=os.link)
    """