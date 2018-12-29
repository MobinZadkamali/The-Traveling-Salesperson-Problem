#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import itertools
import math

# taking n*n matrix input
n = int(input("Enter the number of rows in a matrix: "))
S = []
for i in range(1,n+1):
    S.append(i)
matrix = [[0] * n for i in range(n)]
col_names = []
row_names = []
for i in range(n):
    col_names.append('V' + str(i+1))
    row_names.append('V' + str(i+1))  
    for j in range(n):
          matrix[i][j] = int(input())
print("-------------------------------------------------------------------------")
print(pd.DataFrame(matrix,columns = col_names, index = row_names))

# ُSelect the start node
m = int(input("Select a node to start with:  "))
S.remove(m)
print("-------------------------------------------------------------------------")

# First Stage
print("Stage '1' :")
x = list([row[m-1] for row in matrix])
for i in range(n):
    if i != m-1:
        print("["+str(i+1)+","+str(m)+"]"+" = "+str(x[i]))
        
print("-------------------------------------------------------------------------")

# (n-1)! Stage

v =  sum([list(itertools.combinations(S, i)) for i in range(1,len(S)+1)], [])
w = [[0 for row in range(n+1)] for col in range(n+1)]    
D = [[0 for row in range(len(v)+1)] for col in range(n+1)]
P = [[0 for row in range(len(v)+1)] for col in range(n+1)]
D[0].clear()
P[0].clear()
for i in v:
    D[0].append(list(i))
    P[0].append(list(i))

for i in range(n):
    for j in range(n):
        w[i+1][j+1] = matrix[i][j]

def findsubsets(S,k):
    return set(itertools.combinations(S,k))

# AminusJ generates A-{Vj}
def AminusJ(A,jj,j):
    if len(list(A[jj]))>= 2:
        y = list(A[jj])
        y.remove(j)
        list(A[jj]).insert(0,j)
        return D[j][D[0].index(y)]
    else:
        return w[j][m]

    
# AMJ is AminusJ just for print's stuffs
def AMJ(A,jj,j):
    x = list(A[jj])
    x.remove(j)
    return x 


for k in range(1,n-1):
    print("Stage '"+str(k+1)+"' :")
    A = list(findsubsets(S,k))
    for jj in range(0,len(findsubsets(S,k))):
        g = []
        for i in range(1,n+1):
            g = list(A[jj])
            if i!= m and i not in g:
                temp = []
                minimum = math.inf
                for j in list(A[jj]):
                    D[i][D[0].index(list(A[jj]))] = w[i][j] + AminusJ(A,jj,j)
                    if k == 1:
                        print("["+str(i)+"]{"+str(j)+"} = "+str(D[i][D[0].index(list(A[jj]))]))
                    else:
                        print("["+str(i)+"]["+str(j)+"] + "+str(j)+"{"+str(AMJ(A,jj,j))+"} = "+str(D[i][D[0].index(list(A[jj]))]))
                    temp.append(D[i][D[0].index(list(A[jj]))])
                    for p in temp:
                        if minimum > p:
                            minimum = p
                            P[i][D[0].index(list(A[jj]))] = j
                D[i][D[0].index(list(A[jj]))] = minimum
                if k != 1:
                    print(str(i)+"{"+str(A[jj])+"} = "+str(minimum))
                    print("------------------------------")
    print("-------------------------------------------------------------------------")

# Last Stage    

print("Last Stage :")
temp2 = []
minimum2 = math.inf

# Final Subset minus j
def FMJ(v,j):
    x = list(v[len(v)-1])
    x.remove(j)
    return x
for j in range(1,n+1):
    if j != m:
        D[m][D[0].index(list(v[len(v)-1]))] = w[m][j]+ D[j][D[0].index(FMJ(v,j))]
        print("["+str(m)+"]["+str(j)+"] + "+str(j)+"{"+str(FMJ(v,j))+"} = "+str(D[m][D[0].index(list(v[len(v)-1]))]))
        temp2.append(D[m][D[0].index(list(v[len(v)-1]))])
        for p in temp2:
            if minimum2 > p:
                minimum2 = p
                P[m][D[0].index(list(v[len(v)-1]))] =  j          
D[m][D[0].index(list(v[len(v)-1]))] = minimum2    
minlength = D[m][D[0].index(list(v[len(v)-1]))]

print("MinLength = "+str(minlength))
print("-------------------------------------------------------------------------")

print("The Optimal Tour is :")
d = []
r = m
g = list(v[len(v)-1])
for i in range(0,n-1):
    t = P[r][D[0].index(g)]
    d.append(t)
    r = t
    g.remove(t)
d.insert(0,m)
d.append(m)
text = ""
for i in range(len(d)-1):
    text += str(d[i])+"----->"
print(text+str(d[len(d)-1]))    


# In[ ]:




