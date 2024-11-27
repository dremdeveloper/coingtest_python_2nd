from collections import defaultdict, deque

# ❶ 전역 변수 선언 및 초기화
adj_list = defaultdict(list)
visited = set()
result = []

def bfs(start):
    # ❷ 탐색 시 맨 처음 방문할 노드를 큐에 추가하고 방문 처리
    queue = deque([start])
    visited.add(start)
    result.append(start)
    # ❸ 큐가 비어 있지 않은 동안 반복
    while queue:
        # ❹ 큐에 있는 원소 중 가장 먼저 푸시된 원소 팝
        node = queue.popleft()  
        
        # ❺ 인접한 이웃 노드들에 대해서 방문하지 않은 노드 푸시
        for neighbor in adj_list.get(node, []):  
            if neighbor not in visited: 
                queue.append(neighbor)
                visited.add(neighbor)
                result.append(neighbor)

def solution(graph, start):
    
    # ❻ 그래프를 인접 리스트로 변환
    for u, v in graph:
        adj_list[u].append(v)
    bfs(start)  
    return result
