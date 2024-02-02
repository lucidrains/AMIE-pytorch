import torch
from torch import nn, einsum
from torch.nn import Module, ModuleList

from einops import rearrange

# self critic prompt
# figure A.15 in paper

SELF_RATING_PROMPT = """
I have a doctor-patient dialogue and the corresponding rating that quantifies its quality according to
the following criterion: <criterion> (e.g., maintaining patient welfare). The rating of the dialogue is
on a scale of 1 to 5 where:

5: <definition> e.g., “Treats patient respectfully, and ensures comfort, safety and dignity”
1: <definition> e.g., “Causes patient physical or emotional discomfort AND jeopardises patient safety”

First, describe which parts of the dialogue are good with respect to the criterion. Then, describe which parts are bad with respect to the criterion. Lastly, summarise the above to explain the
provided rating, using the following format:

Good: ...
Bad: ...
Summary: ...

DIALOGUE: <dialogue>
Rating: <human rating>
EVALUATION:
"""

# main class

class AMIE(Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
