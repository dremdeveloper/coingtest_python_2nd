# ❶ 2차원 배열을 90도 회전시키는 함수
def rotate_90(arr):
  n = len(arr)  
  rotated_arr = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      rotated_arr[j][n - i - 1] = arr[i][j]

  return rotated_arr
# ❷ 배열을 n번 90도 회전시키는 함수
def solution(arr, rotations):
  rotated_arr = arr.copy()
  for _ in range(rotations):
    rotated_arr = rotate_90(rotated_arr)

  return rotated_arr


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
'''
print(solution(
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]
], 1))
'''

'''
반환값 : 
[
[13, 9, 5, 1],
[14, 10, 6, 2],
[15, 11, 7, 3],
[16, 12, 8, 4]
]
'''
    
'''    
print(solution(
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14,15,16]
 ], 2))
'''

'''
반환값 : 
[
[16, 15, 14, 13],
[12, 11, 10, 9],
[8, 7, 6, 5],
[4, 3, 2, 1]
]
'''
