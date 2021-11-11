import os
import shutil
import csv

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("New folder is made.")
        
    else:
        print("Folder exists.")

def cpdata(origin, destination):
    mkdir(destination)
    g = os.walk(origin)
    for path, dir_list, file_list in g:
        for file_name in file_list:
            full_path = path +"/" + file_name
            shutil.copy2(full_path, destination)
    
def mkcsv(origin, label, csv_name):
    with open(csv_name, 'a', newline='') as csvfile:
        g = os.walk(origin)
        writer = csv.writer(csvfile)
        for path, dir_list, file_list in g:
            for file_name in file_list:
                writer.writerow([file_name, label])
                

if __name__ == "__main__":
    origin0_training = "./data/gesture0/training"
    origin1_training = "./data/gesture1/training"
    origin2_training = "./data/gesture2/training"
    destination_training = "./data/training"
    csv_training = "label_training.csv"
    cpdata(origin0_training, destination_training)
    cpdata(origin1_training, destination_training)
    cpdata(origin2_training, destination_training)
    mkcsv(origin0_training, '0', csv_training)
    mkcsv(origin1_training, '1', csv_training)
    mkcsv(origin2_training, '2', csv_training)

    origin0_testing = "./data/gesture0/testing"
    origin1_testing = "./data/gesture1/testing"
    origin2_testing = "./data/gesture2/testing"
    destination_testing = "./data/testing"
    csv_testing = "label_testing.csv"
    cpdata(origin0_testing, destination_testing)
    cpdata(origin1_testing, destination_testing)
    cpdata(origin2_testing, destination_testing)
    mkcsv(origin0_testing, '0', csv_testing)
    mkcsv(origin1_testing, '1', csv_testing)
    mkcsv(origin2_testing, '2', csv_testing)