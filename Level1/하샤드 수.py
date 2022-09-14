def solution(x):
    n_sum = sum([int(i) for i in str(x)])
    return x % n_sum == 0