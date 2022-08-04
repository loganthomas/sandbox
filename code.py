import datetime
from collections import namedtuple
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from matplotlib import pyplot as plt
from sklearn import datasets

print("hello world")
print("hello universe")
z = 5 + 3
print("hi logan")
print("hello universe")


def dummy_func(x):
    return x + 2


def dummy2(x: int = 5, y: float = 10):
    import os

    return x + y


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"A Point with x={self.x} and y={self.y}"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


if __name__ == "__main__":
    dummy_func(5)
