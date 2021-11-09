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
    with open(csv_name, 'w', newline='') as csvfile:
        g = os.walk(origin)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for path, dir_list, file_list in g:
            for file_name in file_list:
                

if __name__ == "__main__":
    origin0 = "./data/gesture0/gray"
    origin1 = "./data/gesture1/gray"
    origin2 = "./data/gesture2/gray"
    destination = "./data/all"
    csv_filename = "./data/label.csv"
    cpdata(origin0, destination)
    cpdata(origin1, destination)
    cpdata(origin2, destination)
