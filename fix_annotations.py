from argparse import ArgumentParser
import os 
import csv
import cv2 as cv

DATASET_PATH = "/home/daniel/autofish_dataset_mini/"

def createArgumentParser():
    parser = ArgumentParser()
    parser.add_argument("-p", "--path", default=DATASET_PATH, type=str, help="full path to the folder with groups")
    parser.add_argument("-g", "--group", type=int, help="specify group number you want to correct, must be an intenger")
    parser.add_argument("-f", "--files", type=str, help="insert file numbers, without zeros and separated by a comma,  you want to correct")
    parser.add_argument("-q", "--querry_annotation", type=str, help="annotation to fix, format is id(int)-SIDE(L or R)-species")
    parser.add_argument("-n", "--new_annotation", type=str, help="new annotation, format is id-SIDE-species")
    return parser

def format_args(args):
    group = "group_{}".format(args.group)
    files = args.files.split(",")
    files = [file.zfill(5) for file in files]
    querry_annotation = args.querry_annotation.split("-")
    querry_annotation = querry_annotation[0] + querry_annotation[1] + "-" + querry_annotation[2]
    return args.path, group, files, querry_annotation, args.new_annotation.split("-")

if __name__=="__main__":
    args = createArgumentParser().parse_args()
    path, group, files, querry_annotation, new_annotation = format_args(args)

    print(querry_annotation)
    print(new_annotation)
    print("====")

    for file in files:
        print(file)
        annotation_file_path = os.path.join(path, group, "jai", "annotations", file+".csv")
        with open(annotation_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter = ",")
            annotations = list(csv_reader)

            for annotation in annotations:
                saved_annotation = annotation["id"] + annotation["side"] + "-" + annotation["species"]
                if saved_annotation == querry_annotation:
                    print(saved_annotation)
                    print(querry_annotation) 

        #print(tiff_img.shape)
        #print(annotated_img.shape)