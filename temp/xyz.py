for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    s = str(input())

    ans=""
    i=0
    j=k-1
    while(i<j):
        ans+=(s[i]+s[j])
        i+=1
        j-=1
    if i==j:
        ans+=s[i]
    
    ans = ans[::-1]
    ans += s[k:]
    print(ans)
