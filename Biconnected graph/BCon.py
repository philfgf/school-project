#declaring all of the lists globally to access throughout the file
parent = []
visited = []
d = []
b = []
c = []
APP = []
low = []
count = 0    
stack = []

def adj(Adj,u):
    #A appends the adjacency from Adj for the vertex we are located in
    A = []
    for x in range(len(Adj)):
        if Adj[u][x] != 0:
            A.append(x)
    return A

def BiconnectedComponents(V,A):
    global visited
    global d
    global parent
    global low
    
    visited = [False] * V
    parent = [None] * V
    d = [0] * V 
    low = [0] * V
    
    for v in range(V):
        if not visited[v]:
            DFS_Visit(A,v)
    AP(parent, V)

def DFS_Visit(A,u):
    global count
    visited[u] = True
    count = count + 1
    d[u] = count
    low[u] = d[u]
    Adj = adj(A,u)
    for v in Adj:
        if not visited[v]:
            stack.append((u,v))
            parent[v] = u
            DFS_Visit(A,v)
            if low[v] >= d[u]:
                if u not in c and u != 0:
                    c.append(u)
                outputComp(u,v)
            low[u] = min(low[u],low[v])
        elif not parent[u] == v and d[v] < d[u]:
            stack.append((u,v))
            low[u] = min(low[u],d[v])

def outputComp(u,v):
    #pops the edge from the stack until empty and checks for bridges
    e = stack.pop()
    print 'New Biconnected Component Found',e
    bridge = True
    while not (e == (u,v)):
        bridge = False
        e = stack.pop()
        print 'New Biconnected Component Found',e
    if bridge:
        b.append((u,v))

def AP(p,vert):
    #for loop that checks for Articulation points
    for i in range(vert):
        count = 0
        for j in range(len(p)):
            if i == p[j]:
                count = count + 1
            if count == 2:
                if i not in APP:
                    APP.append(i)
    
            
def main():
    #weight is a nested list that appends the weights of each row from value that is
    #read from the file f
    weight = []
    inf = float('inf')
    with open('graph_file.txt', "r") as f:
        for line in f:
            values = line.rstrip().split(" ")
            weight.append(values)

    #assign the value of Adj = weight
    Adj = weight

    #Adj will be the assigned in this for loop by checking through the weight
    for i in range(len(weight)):
        for j in range(len(weight[i])):      
            if weight[i][j] != 'inf' and weight[i][j] != '0':
                Adj[i][j] = int(Adj[i][j])
            if weight[i][j] == 'inf'or weight[i][j] == '0':
                Adj[i][j] = 0

    #verticies can be only up to 100
    if len(Adj) < 100:
        BiconnectedComponents(len(Adj),Adj)

    #prints the bridges in the graph
    print 'bridges:', b
    print 'Articulation Points:', APP
    


main()
