V = 4
INF = 99999999
def floyd_warshall(graph):
    dist = list(map(lambda i: list(map(lambda j:j,i)),graph))
    print(dist)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    print_solution(dist)
def print_solution(dist):
    print("the shortest way: ")
    for i in range(V):
        for j in range(V):
            if dist[i][j]==INF:
                print(f"{INF}",end=" ")
            else:
                print(f"{dist[i][j]}\t",end=" ")
            if j == V-1:
                print("")

if __name__ == "__main__":
    graph = [[0,5,INF,10,],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
    floyd_warshall(graph)
