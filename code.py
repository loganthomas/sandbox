import numpy as np
import pandas as pd

print("hello world")


def dummy_func(x):
    return x + 2


def dummy2(x: int = 5, y: float = 10):
    import os

    return x + y


if __name__ == "__main__":
    dummy_func(5)
