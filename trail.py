def find(parent,i):
    if parent[i] == i:
       return i
    return find(parent,parent[i])

def union(parent,x,y):
    parent[x] = y
    return parent


def kruskal(nodes,u,v,w):
    parent = [i for i in range(nodes+1)]
    E = [[i,j,k] for i,j,k in zip(u,v,w)]
    i,e,res = 0,0,0
    E.sort(key = lambda a : a[-1])
    while e < nodes - 1:
         uu,vv,ww = E[i]
         xr = find(parent,uu)
         yr = find(parent,vv)
         if xr!= yr:
            e+=1
            res+=ww
            parent = union(parent,xr,yr)
         i+=1
    return res


nodes , edges = map(int,input().rstrip().split())
u = [0]*edges
v = [0]*edges
w = [0]*edges
for i in range(edges):
     u[i],v[i],w[i] = map(int,input().rstrip().split())
res = kruskal(nodes,u,v,w)
print(res)
print(E)


# Input
# 4 6
# 1 2 5
# 1 3 3
# 4 1 6
# 2 4 7
# 3 2 4
# 3 4 5
# 12
