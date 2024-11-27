INF = 9999999999

def solution(num_vertices, edges, source):
  # ❶ 간선 정보를 활용해서 인접 리스트를 생성
  graph = [[] for _ in range(num_vertices)]
  for edge in edges:
    from_vertex, to_vertex, weight = edge
    graph[from_vertex].append((to_vertex, weight))
  
  # ❷ 현재까지 구한 최소 비용을 INF로 설정(시작 노드는 제외)
  distance = [INF] * num_vertices
  distance[source] = 0
  
  # ❸ 정점의 개수 -1 만큼 최소 비용을 갱신
  for _ in range(num_vertices - 1):
    for u in range(num_vertices):
      for v, weight in graph[u]:
        if distance[u] + weight < distance[v]:
          distance[v] = distance[u] + weight
  
  # ❹ 음의 순환이 있는지 확인
  for u in range(num_vertices):
    for v, weight in graph[u]:
      if distance[u] + weight < distance[v]:
        return [-1]
  
  return distance
