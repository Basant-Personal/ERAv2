import torch

# CUDA?
cuda = torch.cuda.is_available()
print("CUDA Available?", cuda)

import matplotlib.pyplot as plt

from tqdm import tqdm

#!pip install torchsummary
from torchsummary import summary
