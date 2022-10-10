import numpy as np

def solution(a, b):
    # Usig Numpy
    # return int((np.array(a) * np.array(b)).sum())
    
    # Not using Numpy
    return sum([x*y for x,y in zip(a,b)])