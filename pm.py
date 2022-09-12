def pm(t,p):
    for i in range(0,len(t)-len(p)+1):
        for j in range(0,len(p)):
            if t[i+j] is not p[j]:
                break
            if j==len(p)-1:
                return i
    return -1


print(pm("rubel","be"))