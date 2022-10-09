def solution(s):
    # try:
    #     if len(s)==4 or len(s)==6:
    #         a = int(s)
    #         return True
    #     else:
    #         return False
    # except:
    #     return False
    
# Comment: isdigit() 함수 사용 가능
    return s.isdigit() and (len(s)==4 or len(s)==6)