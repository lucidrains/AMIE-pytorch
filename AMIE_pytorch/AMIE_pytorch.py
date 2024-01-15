import torch
from torch import nn, einsum
from torch.nn import Module, ModuleList

from einops import rearrange

class AMIE(Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
