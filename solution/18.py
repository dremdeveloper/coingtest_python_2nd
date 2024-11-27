def solution(arr, target):
    hash = [0] *(target + 1) # ➊ 해시 테이블 생성 및 초기화
    
  # ➋ arr의 각 원소를 키로 해시테이블을 만듬
    for num in arr:
        if num <= target:
            hash[num] = 1
            
    for num in arr:
        # ➌ target보다 더 큰 수는 답이 될수 없음 
        if(num >= target): 
            continue
       # ➍ arr에 중복되는 원소는 존재하지 않음 
        if((target - num) == num):
            continue
        # ❺ 두 수의 합으로 target을 만들수 있으면 True반환 
        if(hash[target - num]):
            return True
    
    # ❻ 두 수의 합으로 target을 만들 수 없으면 False 반환
    return False
  
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([1, 2, 3, 4, 8], 6)) # 반환값 : True
# print(solution([2, 3, 5, 9], 10)) # 반환값 : False
