import numpy as np

def solution(arr1, arr2):
#     answer = []
#     row_len = len(arr1)
#     col_len = len(arr1[0])
    
#     for i in range(row_len):
#         answer_in = []
#         for j in range(col_len):
#             answer_in.append(arr1[i][j] + arr2[i][j])
#         answer.append(answer_in)
#     return answer

    # Using Numpy
    answer = np.array(arr1) + np.array(arr2)
    return answer.tolist()