def solution(numbers):
    return sum([i for i in range(10) if i not in numbers ])

    # Easier solution
    return 45 - sum(numbers)