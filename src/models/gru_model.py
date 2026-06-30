"""
gru_model.py

Purpose:
Define the GRU model architecture for
Remaining Useful Life prediction.
"""

import torch
import torch.nn as nn


class GRUModel(nn.Module):
    """
    GRU model for Remaining Useful Life prediction.
    """
    def __init__(
    self,
    input_size=17,
    hidden_size=64,
    num_layers=1
     ):
     """
     Initialize the model.
     """

     super().__init__()

     self.input_size = input_size
     self.hidden_size = hidden_size
     self.num_layers = num_layers
     self.gru = nn.GRU(
      input_size=self.input_size,
      hidden_size=self.hidden_size,
      num_layers=self.num_layers,
      batch_first=True
       )
     self.fc = nn.Linear(
        in_features=self.hidden_size,
        out_features=1
       ) 
    def forward(self, x):
        """
        Forward pass of the GRU model.
        """

        _, hidden = self.gru(x)

        output = self.fc(hidden[-1])
        return output
     


if __name__ == "__main__":

    model = GRUModel(
        input_size=17,
        hidden_size=64,
        num_layers=1
    )

    print(model)

    # ---------------------------------
    # Dummy Input
    # ---------------------------------

    x = torch.randn(64, 30, 17)

    prediction = model(x)

    print("\nInput Shape :", x.shape)
    print("Output Shape:", prediction.shape)
    # ---------------------------------
# Model Summary
# ---------------------------------

    print("\n" + "=" * 50)
    print("MODEL SUMMARY")
    print("=" * 50)
  
    total_params = sum(
    p.numel()
    for p in model.parameters()
     )

    trainable_params = sum(
    p.numel()
    for p in model.parameters()
    if p.requires_grad
     )

    print(f"Total Parameters     : {total_params:,}")
    print(f"Trainable Parameters : {trainable_params:,}")