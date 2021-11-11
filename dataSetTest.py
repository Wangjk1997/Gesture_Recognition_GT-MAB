import os
import pandas as pd
from torchvision.io import read_image
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from PIL import Image

class ImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform
    def __len__(self):  
        return len(self.img_labels)
    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = Image.open(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label

if __name__ == "__main__":
    label_map = {
        0: "no",
        1: "palm",
        2: "one",
    }
    training_set = ImageDataset("label_training.csv","./data/training",transform=ToTensor())
    sample_index = torch.randint(len(training_set), size=(1,)).item()
    img, label = training_set[sample_index]
    print(img.shape)
    plt.title(label_map[label])
    plt.axis("off")
    # plt.imshow(img, cmap="gray")
    print(type(img))
    plt.show()