def Parent(i):
    return i / 2

def Left(i):
    return 2 * i + 1

def Right(i):
    return 2 * i + 2

def Extract_Min(Q):
    heapSize = len(Q) - 1
    if(heapSize < 0):
        print("error heap underflow")
    #Smallest variable and 1st element in list
    s = Q[0]
    Q[0] = Q[heapSize]
    del(Q[0])
    Min_Heapify(Q,0)
    return s

def Build_Heap(Q):
    #For loop that goes from the floor of len S to 0
    for i in range(len(Q) - 1/ 2, -1, -1):
        Min_Heapify(Q,i)
        
def Min_Heapify(Q,i):
    #Declared left and right variables
    l = Left(i)
    r = Right(i)
    
    #Changed the max heapify into a min heap.
    if(l < len(Q) and Q[l] < Q[i]):
        smallest = l
    else:
        smallest = i
    if(r < len(Q) and Q[r] < Q[smallest]):
       smallest = r
    if(smallest != i):
       Q[i], Q[smallest] = Q[smallest], Q[i]
       Min_Heapify(Q,smallest)


p = dict()
rank = dict()
def MAKE_SET(x):
    p[x] = x
    rank[x] = 0   

def UNION(x,y):
    LINK(FIND_SET(x),FIND_SET(y))

def LINK(x,y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] = rank[y] + 1
            
def FIND_SET(x):
    if x != p[x]:
        p[x] = FIND_SET(p[x])
    return p[x]

def MST_KRUSKAL(G,adj):
    #A is the adjacency matrix that we will append the tuples of w,u,v
    inf = float('inf')
    A = []

    for v in range(len(adj)):
        MAKE_SET(v)

    Build_Heap(G)

    #for loop that goes through the graph 
    for e in range(len(G)):
        E = Extract_Min(G)
        #w is the weight, u is the vertex, and v is the other vertex attatched to the edge
        w,u,v = E
        if FIND_SET(u) != FIND_SET(v):
            A.append(E)
            UNION(u,v)
    print 'verticies with weight:'
    print A
    return A

def main():
    #weight is a nested list that appends the weights of each row from value that is
    #read from the file f
    #graph is the list that we will append the tuples of w,u,v
    graph = []
    weight = []
    with open('graph_file.txt', "r") as f:
        for line in f:
            values = line.rstrip().split(" ")
            weight.append(values)

    #assign the value of Adj = weight
    Adj = weight

    #Adj will be the assigned in this for loop by checking through the weight
    #hi and low creates duplicates so you only go through one direction
    #graph is a list of tuples containing the weight and verticies in the form w,u,v
    for i in range(len(weight)):
        for j in range(len(weight[i])):      
            if weight[i][j] != 'inf' and weight[i][j] != '0':
                Adj[i][j] = int(Adj[i][j])
                if i >= j:
                    hi = i
                    low = j
                elif j > i:
                    hi = j
                    low = i
                graph.append((int(weight[i][j]),(low),(hi)))
                if weight[i][j] == 'inf'or weight[i][j] == '0':
                    Adj[i][j] = 0
    #dup is the duplicates that we have in the file and we will use a for loop
    #to remove all of the duplicates
    dup = set()
    dupA = dup.add
    graph = [x for x in graph if not (x in dup or dupA(x))]

    #verticies can be only up to 100
    if len(graph) < 100:
       A = MST_KRUSKAL(graph,Adj)
       
    #Initialize the Adjacency matrix to all 0's
    Adjacency = [[0 for i in range(len(A)+1)] for j in range(len(A)+1)]
    
    print ''
    print 'Adjacency matrix ='

    #for loop that uses each tuple to place the weight i in the correct location in the
    #adjacency matrix using the vertecies j and k
    for i,j,k in A:
        Adjacency[j][k] = i
        Adjacency[k][j] = i

    #prints the matrix
    for i in Adjacency:
        print i
    

main()
