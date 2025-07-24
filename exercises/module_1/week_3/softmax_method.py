import torch
import torch.nn as nn
import math


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        total = sum(math.exp(value) for value in data)
        result = [math.exp(value)/total for value in data]

        return torch.Tensor(result)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        data = data - max(data)
        total = sum(math.exp(value) for value in data)
        result = [(math.exp(value))/total for value in data]

        return torch.Tensor(result)


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])

    softmax = Softmax()
    print(f"Softmax data: {softmax(data)}")

    softmax_stable = SoftmaxStable()
    print(f"Softmax Stable data: {softmax_stable(data)}")
