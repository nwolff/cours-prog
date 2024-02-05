import numpy as np


def f1(x):
    return (x - 31) * (x + 2) * (x + 4)


def f2(x):
    return np.sin(np.pi * (x - 4) / 16) * (x - 16) + 1
