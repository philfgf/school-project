def KMP_Matcher(T,P):
    n = len(T) - 2
    m = len(P) - 2
    pi = Compute_Prefix_Function(P)
    q = 0
    start = 0
    
    for i in range(1, n, 1):
        while(q > 0 and P[q+1] != T[i] and start == 0):
            q = pi[q]
        if(P[q+1] == T[i]):
            q += 1
        if(q == m):
            print('Pattern occurs with shift')
            start = (i - m) + 1  #add 1 because starts at 0 instead of 1
            q = pi[q]
    print(pi)
    return start
            
def Compute_Prefix_Function(P):
    m = len(P) - 2
    pi = [0] * (len(P)-1)
    pi[0] = -1
    k = 0
    
    for q in range(2, m, 1):
        while(k > 0 and (P[k] != P[q])):
            k = pi[k]
        if(P[k] == P[q]):
            k = k + 1
        pi[q+1] = k
    return pi
        
def main():
    T = []
    P = []
    f = open('string_info.txt', 'r')
    T = f.readline()
    
    for line in f:    
        P = line.split('\n', 1)[0]

    start = KMP_Matcher(T,P)
    print('start is:', start)


main()
