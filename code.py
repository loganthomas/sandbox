import datetime
from collections import namedtuple
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn import datasets

print("hello world")
print("hello universe")
z = 5 + 3


def dummy_func(x):
    return x + 2


def dummy2(x: int = 5, y: float = 10):
    import os

    return x + y


if __name__ == "__main__":
    dummy_func(5)
