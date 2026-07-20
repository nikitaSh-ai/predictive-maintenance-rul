"""
generalized_gru.py

Purpose:
GRU model for Version 2 generalized training.
"""

import torch
import torch.nn as nn


class GeneralizedGRU(nn.Module):
    """
    GRU model for generalized RUL prediction.
    """

    def __init__(
        self,
        input_size=24,
        hidden_size=128,
        num_layers=1,
        dropout=0.2
    ):
        super().__init__()

        self.gru = nn.GRU(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )

        self.dropout = nn.Dropout(dropout)

        self.fc = nn.Linear(
            hidden_size,
            1
        )

    def forward(self, x):

        _, hidden = self.gru(x)

        hidden = self.dropout(
            hidden[-1]
        )

        output = self.fc(hidden)

        return output
    



def main():

    model = GeneralizedGRU()

    print(model)

    x = torch.randn(
        64,
        40,
        24
    )

    prediction = model(x)

    print()

    print("Input Shape :", x.shape)
    print("Output Shape:", prediction.shape)


if __name__ == "__main__":
    main()