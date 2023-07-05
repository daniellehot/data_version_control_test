import os
import shutil
src_dir = "/home/daniel/data_version_control_test/csv"
dst_dir = "/home/daniel/autofish_dataset_mini"

for root, dirs, files in os.walk(src_dir):
    for file in files:
        print(os.path.join(root, file))
        print(os.path.join(root, file).replace(src_dir, dst_dir))
        print("========================")
        shutil.copy(os.path.join(root, file), os.path.join(root, file).replace(src_dir, dst_dir) )