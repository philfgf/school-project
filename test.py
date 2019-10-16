#import matplotlib.pyplot as plt
#from matplotlib import rc,rcParams
def REPETITION_MATCHER(P, T):
    m = len(P) - 1
    n = len(T) - 1
    k = 1
    q = 0
    s = 0
    while (s <= (n - m)):
        if(T[s + q + 1] == P[q + 1]):
           q = q + 1
           if(q == m):
               print("Pattern occurs with shift", s)
        if(q == m or T[s + q + 1] != P[q + 1]):
          s = s + max(1, ceil(q/k))
          q = 0
    print(s)

P = ['a','b','a','a','b','a','b','a','b','b','a','b','a','b','a','b','b','a','b','a','b','a','a']
T = ['a','b','a','b','b','a','b','a','b','a','a']
REPETITION_MATCHER(P, T)
