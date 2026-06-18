# benchmark.py
from torch.profiler import profile
import torch
import torch.nn as nn

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
    model = SimpleNet().cuda()

for _ in range(100):
    x = torch.randn(256,1024).cuda()

    output = model(x)

    loss = output.mean()

    loss.backward()
with profile(
    activities=[
        torch.profiler.ProfilerActivity.CPU,
        torch.profiler.ProfilerActivity.CUDA
    ]
) as prof:
        train_step()
prof.export_chrome_trace(
    "traces/trace.json"
)