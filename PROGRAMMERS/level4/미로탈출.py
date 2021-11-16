from heapq import *

def solution(n, start, end, roads, traps):
    NORMAL, REVERSE = 0, 1
    
    graph = [[] for _ in range(n+1)]
    cost = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for p,q,s in roads:
        graph[p].append([q,s,NORMAL])
        graph[q].append([p,s,REVERSE])
        cost[p][q] = cost[q][p] = s
    
    visit = [[float('inf') for _ in range(n+1)] for _ in range(1<<len(traps))]
    q = []
    q.append([0, start, 0])

    while q:
        time, current, trap_state = heappop(q)
        print(current,bin(trap_state))
        if current == end:
            return time
        
        if visit[trap_state][current] != float('inf'):
            continue
        visit[trap_state][current] = time
        
        flag = (1<<traps.index(current)) if current in traps else 0
        
        for _next, _time, _mode in graph[current]:
            _flag = (1<<traps.index(_next)) if _next in traps else 0
            next_state = trap_state ^ _flag
            if (((trap_state&flag)>0)^((trap_state&_flag)>0)) == _mode:
                heappush(q, [time + _time, _next, next_state])
                
