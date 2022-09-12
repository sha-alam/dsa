def toh(n,a,b,c):
    if n==1:
        print("Move disc ",n," from ",a," to ",b)
    else:
        toh(n-1,a,c,b)
        print("Move disc ",n," from ",b," to ",a)
        toh(n-1,c,b,a)

n=int(input())
toh(n,'A','B','C')