# ➊ 그래프 생성
def build_graph(n, wires):
  graph = [[] for _ in range(n + 1)]
  for a, b in wires:
    graph[a].append(b)
    graph[b].append(a)
  return graph

# ➋ 깊이 우선 탐색 함수
def dfs(node, parent, graph):
  cnt = 1
  # ➌ 현재 노드의 자식 노드들에 방문
  for child in graph[node]:
    # ➍ 부모 노드가 아닌 경우에만 탐색
    if child != parent:
      cnt += dfs(child, node, graph)
  return cnt

def solution(n, wires):
  graph = build_graph(n, wires)
  min_diff = float("inf")

  for a, b in wires:
    # ➎ 간선 제거
    graph[a].remove(b)
    graph[b].remove(a)

    # ➏ 각 전력망 송전탑 개수 계산
    cnt_a = dfs(a, b, graph)
    cnt_b = n - cnt_a

    # ➐ 최솟값 갱신
    min_diff = min(min_diff, abs(cnt_a - cnt_b))

    # ➑ 간선 복원
    graph[a].append(b)
    graph[b].append(a)

  return min_diff

