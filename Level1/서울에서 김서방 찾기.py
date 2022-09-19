def solution(seoul):
    # loc = [i for i, s in enumerate(seoul) if s=='Kim']
    # return f"김서방은 {loc[0]}에 있다"
    
    return f"김서방은 {seoul.index('Kim')}에 있다" 

# Comment: index 함수 사용 가능