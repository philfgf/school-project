def FLOYD_WARSHALL(weight):
    #Setting n to be the keys of the dictionary
    n = weight.keys()
    print weight
    #Checks the amount of vertices
    if len(n) > 100:
        print 'The maximum number of vertices of the directed graph is 100 and yours is', len(n)
    else:
        for m in n:
            print ''
            #If statement signifying the start of the sequence
            if m == 0:
                print 'Inital:'
                print 'm =', m
            #If statement signifying the intermidiate parts of the sequence
            if m < len(n) - 1 and m !=0:
                print 'm =', m
            #If statement signifying the end of the sequence
            if m == len(n) - 1:
                print 'Final:'
                print 'm =', m
            for i in n:
                for j in n:
                    #weight[i][j] is the weight of the edge
                    if weight[i][m] + weight[m][j] < weight[i][j]:
                        weight[i][j] = weight[i][m] + weight[m][j]
                    #The initial start of the sequence
                    if m == 0:
                        print '%5s'% weight[i][j],
                    #The final conclusion of the sequence
                    if m == len(n)-1:
                        print '%5s'% weight[i][j],
                    #The intermidiate steps in the sequence
                    if m > 0 and m < len(n)-1:
                        print '%5s'% weight[i][j],
                print ''

    for m in range(2):
            print ''
            #If statement signifying the start of the sequence
            if m == 0:
                print 'Inital:'
                print 'm =', m
            #If statement signifying the intermidiate parts of the sequence
            if m < len(n) - 1 and m !=0:
                print 'm =', m
            #If statement signifying the end of the sequence
            if m == len(n) - 1:
                print 'Final:'
                print 'm =', m
            for i in n:
                for j in n:
                    #weight[i][j] is the weight of the edge
                    if weight[i][m] + weight[m][j] < weight[i][j]:
                        weight[i][j] = weight[i][m] + weight[m][j]
                    #The initial start of the sequence
                    if m == 0:
                        print '%5s'% weight[i][j],
                    #The final conclusion of the sequence
                    if m == len(n)-1:
                        print '%5s'% weight[i][j],
                    #The intermidiate steps in the sequence
                    if m > 0 and m < len(n)-1:
                        print '%5s'% weight[i][j],
                print ''
    

def main():
    #graph is the dictionary that I will append the list of dictionary to create a
    #nested dictionary
    #newD is the dictionary that I append the weights to
    #l is the list that I append the dictionary weights to
    #weight is a nested list that appends the weights of each row from value that is
    #read from the file f
    graph = {}
    newD = {}
    l = []
    weight = []
    with open('graph_file.txt', "r") as f:
        for line in f:
            values = line.rstrip().split(" ")
            weight.append(values)
        for i in range(len(weight)):
            for j in range(len(weight[i])):
                if weight[i][j] == 'inf':
                    newD[j] = float(weight[i][j])
                else:
                    newD[j] = int(weight[i][j])          
            l.append(newD)
            newD = {}
    
    for i in range(len(l)):
        graph[i] = l[i]
    
    FLOYD_WARSHALL(graph)

main()

