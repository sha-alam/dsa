
N=int(input())
board=[[0]*N for _ in range(N)]

def isattack(i,j):
    for k in range(0,N):
        if board[i][k]== 1 or board[k][j]==1:
            return 1
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return 1
    return 0
def nq(n):
    if n==0:
        return 1
    for i in range(0,N):
        for j in range (0,N):
            if (not (isattack(i,j))) and board[i][j]!= 1:
                board[i][j]=1
                if nq(n-1)==1:
                    return 1
                board[i][j]=0
    return 0

nq(N)
for i in board:
    print(i)