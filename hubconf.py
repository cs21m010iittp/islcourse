import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, ToPILImage
from PIL import Image
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

transform_tensor_to_pil = ToPILImage()
transform_pil_to_tensor = ToTensor()


device = "cuda" if torch.cuda.is_available() else "cpu"

def load_data():

    # Download training data from open datasets.
    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor(),
    )

    # Download test data from open datasets.
    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=True,
        transform=ToTensor(),
    )
    return training_data, test_data


def create_dataloaders(training_data, test_data, batch_size=64):

    # Create data loaders.
    train_dataloader = DataLoader(training_data, batch_size=batch_size)
    test_dataloader = DataLoader(test_data, batch_size=batch_size)

    for X, y in test_dataloader:
        print(f"Shape of X [N, C, H, W]: {X.shape}")
        print(f"Shape of y: {y.shape} {y.dtype}")
        break
        
    return train_dataloader, test_dataloader

train_loader, test_loader = create_dataloaders(training_data, test_data, batch_size = 32)

class cs21m010(nn.Module):
    def __init__(self):
        super(cs21m010, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 10)
        )
        self.sobj =torch.nn.Softmax(dim=1)

    def forward(self, x):
        x = self.flatten(x)
        x =  self.linear_relu_stack(x)
        x=self.sobj(x)

        return x
    
y = (len(set([y for x,y in training_data])))
model = cs21m010()
