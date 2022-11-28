t = int(input())
while(t):
    t -= 1
    p, q = map(int, input().split())
    s1 = input().strip()
    if(s1.count(' ')): s1, s2 = s1.split()
    else: s2 = input()
    s3 = ""
    s4 = ""
    s5 = ""
    s6 = ""
    be = min(p,q)
    lon = max(p,q)
    for i in range(len(s1)):
        if(s1[i] == str(lon)):
            s3 += str(be)
        else:
            s3 += s1[i]
        if(s1[i] == str(be)):
            s4 += str(lon)
        else:
            s4 += s1[i]
    for i in range(len(s2)):
        if(s2[i] == str(lon)):
            s5 += str(be)
        else:
            s5 += s2[i]
        if(s2[i] == str(be)):
            s6 += str(lon)
        else:
            s6 += s2[i]
    res1 = int(s3) + int(s5)
    res2 = int(s4) + int(s6)
    print(res1, res2)        


