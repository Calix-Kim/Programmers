def solution(a, b):
    return (a+b)*(abs(b-a)+1)/2
    # return sum(range(a, b+1)) if a < b  else sum(range(b, a+1))