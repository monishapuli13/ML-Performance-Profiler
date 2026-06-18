# benchmark.py

import os
import torch
import torch.nn as nn
from torch.profiler import profile


class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()

        self.layers = nn.Sequential(
            nn.Linear(1024, 2048),
            nn.ReLU(),
            nn.Linear(2048, 1024)
        )

    def forward(self, x):
        return self.layers(x)


device = "cuda" if torch.cuda.is_available() else "cpu"

model = SimpleNet().to(device)


def train_step():
    x = torch.randn(256, 1024).to(device)

    output = model(x)

    loss = output.mean()

    loss.backward()


os.makedirs("traces", exist_ok=True)

with profile(
    activities=[
        torch.profiler.ProfilerActivity.CPU,
        torch.profiler.ProfilerActivity.CUDA
    ]
) as prof:

    for _ in range(100):
        train_step()

prof.export_chrome_trace(
    "traces/trace.json"
)

print("Trace saved to traces/trace.json")