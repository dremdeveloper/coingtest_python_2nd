from collections import defaultdict

# ❶ 너비 우선 탐색에 필요한 전역 변수 선언 
adj_list = defaultdict(list)
visited = set()
result = []

def dfs(node):
    # ❷ 현재 노드 방문 여부를 표시
    visited.add(node)  
    result.append(node) 
    # ❸ 현재 노드와 인접한 노드를 순회하며 인접하지 않은 노드 탐색
    for neighbor in adj_list.get(node, []):  
        if neighbor not in visited:  
            dfs(neighbor)

def solution(graph, start):
    # ❹ 그래프를 인접 리스트로 변환
    for u, v in graph:
        adj_list[u].append(v)
    
    dfs(start)
    return result
