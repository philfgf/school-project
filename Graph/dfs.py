class dfs():
    
    def graph(self):
        self.graph = graph = {'A': set(['B', 'C']),
                                'B': set(['A', 'D', 'E']),
                                'C': set(['A', 'F']),
                                'D': set(['B']),
                                'E': set(['B', 'F']),
                                'F': set(['C', 'E'])}
   

def DFS(G):
    for u in range(0, G.V, 1):
        u.color = white
        u.pi = nil
    time = 0
    for u in range(0, G.V, 1):
        if(u.color == white):
            DFS_VISIT(G,u)

def DFS_VISIT(G,u):
    time = time + 1
    u.d = time
    u.color = gray
    for v in range(0, G.adj[u]):
        if(v.color == white):
            v.pi = u
            DFS_VISIT(G,v)
    u.color = black
    time = time + 1
    u.f = time
