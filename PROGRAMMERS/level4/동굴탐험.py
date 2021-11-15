'''
https://programmers.co.kr/learn/courses/30/lessons/67260
'''

from collections import deque

def solution(n, path, order):
    answer = 0
    graph = [[] for _ in range(n)]
    
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    locked = {}
    for a, b in order:
        locked[b] = a
           
    visit = [0 for _ in range(n)] 
    wait = {}
    q = deque([0])
    
    while q:
        current = q.popleft()
        
        if current in locked and not visit[locked[current]]:
            wait[locked[current]] = current
            continue
        
        visit[current] = 1
        answer += 1
        
        for child in graph[current]:
            if not visit[child]:
                q.append(child)
        
        if current in wait:
            q.append(wait[current])

    return answer == n
