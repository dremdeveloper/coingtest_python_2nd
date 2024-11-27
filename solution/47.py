def backtrack(sum, selected_nums, start, N, results):
  if sum == 10:  # ❷ 합이 10이 되면 결과 리스트에 추가
    results.append(selected_nums)
    return
  for i in range(start, N + 1):  # ❸ 다음에 선택할 수 있는 숫자들을 하나씩 선택하면서
    if sum + i <= 10:  # ❹ 선택한 숫자의 합이 10보다 작거나 같으면
      backtrack(
        sum + i, selected_nums + [i], i + 1, N, results
      )  # ❺ 백트래킹 함수를 재귀적으로 호출

def solution(N):
  results = []  # ➊ 조합 결과를 담을 리스트
  backtrack(0, [], 1, N, results)  # ❻ 백트래킹 함수 호출
  return results  # ❼ 조합 결과 반환
