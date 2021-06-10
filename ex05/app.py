from collections import deque

# 높이, 넓이
n, m = 10, 10

# 디지털 연못
graph = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# for i in range(n):
#     graph.append(list(map(int, input().split())))

# 셀의 깊이를 확인했는지 참거짓 리스트
checked_bottom = [[False for i in range(n)] for j in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 연못 깊이를 측정하는 함수
def measure_depth_of_pond(x, y):
    queue = deque()
    queue.append((x, y))

    # 모든 셀의 바닥 깊이를 확인할 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 상하좌우의 셀이 현재 셀보다 깊거나 같은지에 대한 참거짓 리스트
        check_surrounding_deeper = [False, False, False, False]

        # 바닥이 확인된 경우 생략
        if checked_bottom[x][y]:
            continue

        # 상하좌우의 셀을 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주변 셀이 리스트 범위를 벗어난 셀일 경우 생략
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 바닥을 확인하지 않았으면서 큐에 없는 주변 셀을 큐에 추가
            if not checked_bottom[nx][ny] and not (nx, ny) in queue:
                queue.append((nx, ny))

            # 주변 셀이 땅인 경우 깊이를 측정하지 않음
            if graph[nx][ny] == 0:
                continue

            # 주변 셀이 현재 셀보다 깊거나 같은 경우
            if graph[nx][ny] >= graph[x][y]:
                # 참으로 변경
                check_surrounding_deeper[i] = True
                
        # 만약 상하좌우 셀 중 하나라도 현재 셀보다 얕거나, 현재 셀이 땅이라면
        if False in check_surrounding_deeper or graph[x][y] == 0:
            # 현재 셀의 깊이 측정 완료
            checked_bottom[x][y] = True
        # 상하좌우 셀 모두가 현재 셀보다 깊거나 같다면
        else:
            # 현재 셀의 깊이에 1 더함
            graph[x][y] += 1

    # 깊이 그래프 반환
    return graph

result = measure_depth_of_pond(0, 0)

print(sum(sum(i) for i in result))

for r in result:
    print(r)
