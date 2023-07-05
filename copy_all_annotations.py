import os
import shutil
import subprocess

src_dir = "/home/daniel/autofish_dataset_mini"
dst_dir = "/home/daniel/data_version_control_test/csv"

def push_to_git():
    cmd = "git add csv && git commit -m \"test\" && git push origin snapshot"
    subprocess.call(cmd, shell=True)

def remove_old_csv_file():
    cmd = "rm -r {}".format(os.path.join("~", "data_version_control_test", "csv"))
    subprocess.call(cmd, shell=True)

if __name__=="__main__":
    remove_old_csv_file()
    for root, dirs, files in os.walk(src_dir):
        if os.path.join("jai", "annotations") in root:
            os.makedirs(root.replace(src_dir, dst_dir))
        for file in files:
            if "annotations" in root and file.endswith('.csv'):
                shutil.copy(os.path.join(root, file), os.path.join(root, file).replace(src_dir, dst_dir) )
    push_to_git()