import os
import shutil
import argparse
import subprocess

def sync_onedrive():
    cmd = "onedrive --synchronize --single-directory autofish_groups --verbose"
    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    if returned_value != 0:
        print("Could not sync onedrive. Exiting...")
        exit()

def remove_pulled_data_folder():
    cmd = "rm -r data"
    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    if returned_value != 0:
        print("Could not remove the pulled data folder. Exiting...")
        exit()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="full path to the local copy of the dataset")
    parser.add_argument("-o", "--output", type=str, default="data", help="output folder")
    args = parser.parse_args()
    if args.path == None:
        print("Please, provide path to the dataset folder\n     python3 link_dataset.py -p path/to/dataset/")
        exit()

    #Remove pulled data folder 
    if os.path.exists("data"):
        remove_pulled_data_folder()

    #Synch onedrive to get the latest dataset version before creating link
    sync_onedrive()

    #Create hardlink with the dataset on Onedrive
    shutil.copytree(args.path, "data", copy_function=os.link)
    with open(os.path.join(args.output, ".gitignore"), "w") as f:
        f.write("group_*/calibration\n")
        f.write("group_*/heatmaps\n")
        f.write("group_*/jai/annotated\n")
        f.write("group_*/jai/rgb\n")
        f.write("group_*/logs\n")
        f.write("group_*/rs\n")
        f.write("group_*/README.txt\n")
        f.write("dummy_with_screencasts\n")
        f.write("setup_images")
