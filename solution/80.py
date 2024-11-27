def solution(amount):
  denominations = [100, 50, 10, 1]  
  change = []  
  for coin in denominations:
    # ❶ 현재 화폐 단위로 최대한 거슬러 줄 수 있는 동전의 갯수 구함
    count = amount // coin  
    change.extend([coin] * count)
    # ❷ 정산이 완료된 거스름돈을 제외함
    amount %= coin  
  return change



# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(123)) # 반환값 : [100, 10, 10, 1, 1, 1]
# print(solution(350)) # 반환값 : [100, 100, 100, 50]
