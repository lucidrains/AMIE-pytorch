import torch
from torch import nn, einsum
from torch.nn import Module, ModuleList

from einops import rearrange

# self critic prompt
# figure A.15 in paper

PROMPT_EVALUATE_EXPLANATION = """
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

# figure A.16

PROMPT_EVALUATE_QUALITATIVE = """
I have a doctor-patient dialogue which I would like you to evaluate on the following criterion:
<criterion> (e.g., maintaining patient welfare). The dialogue should be rated on a scale of 1-5 with
respect to the criterion where:

5: <definition> e.g., “Treats patient respectfully, and ensures comfort, safety and dignity”
1: <definition> e.g., “Causes patient physical or emotional discomfort AND jeopardises patient safety”

Here are some example dialogues and their ratings:
DIALOGUE: <example dialog>
EVALUATION: <example self-generated explanation>
Rating: <example rating>
...

Now, please rate the following dialogue as instructed below. First, describe which parts of the dialogue
are good with respect to the criterion. Then, describe which parts are bad with respect to the criterion.
Third, summarise the above findings. Lastly, rate the dialogue on a scale of 1-5 with respect to the
criterion, according to this schema:

Good: ...
Bad: ...
Summary: ...
Rating: ...

DIALOGUE: <dialogue>
EVALUATION:
"""

# main class

class AMIE(Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
