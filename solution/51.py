from itertools import combinations_with_replacement
from collections import Counter

# ➊ 주어진 조합에서 각각의 점수 계산
def calculate_score(combi, info):
  score1, score2 = 0, 0
  for i in range(1, 11):
    if info[10 - i] < combi.count(i):
      score1 += i
    elif info[10 - i] > 0:
      score2 += i
  return score1, score2

# ➋ 최대 차이와 조합 저장
def calculate_best_combination(n, info):
  max_diff = 0
  max_comb = {}

  for combi in combinations_with_replacement(range(11), n):
    cnt = Counter(combi)
    score1, score2 = calculate_score(combi, info)
    diff = score1 - score2

    if diff > max_diff:
      max_diff = diff
      max_comb = cnt

  return max_diff, max_comb

# ➌ 결과 반환
def solution(n, info):
  max_diff, max_comb = calculate_best_combination(n, info)

  if max_diff > 0:
    answer = [0] * 11
    for score in max_comb:
      answer[10 - score] = max_comb[score]
    return answer
  else:
    return [-1]

