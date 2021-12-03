# coding my own sklearn modules
import numpy as np
import pandas as pd


def Label_Encoder(arr):
    encoder = {}
    j = 0
    for i in arr:
        if i not in encoder:
            encoder[i] = j
            j += 1
    res = []
    for i in arr:
        res.append(encoder[i])
    return np.array(res)


v = ['h', 'i', 'h', 'z']
print(v)
v = np.array(v)
print(v)
print(Label_Encoder(v))
