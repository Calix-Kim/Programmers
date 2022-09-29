import numpy as np

def solution(a, b):
    return int((np.array(a) * np.array(b)).sum())