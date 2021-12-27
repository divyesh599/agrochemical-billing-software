for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    print(b)
    i=0
    ans1=0
    while i<n:
        mn=b[i]
        mx=b[i]
        print(mn, mx, "**")
        for j in range(i,n+1):
            mx=max(mx,a[j])
            print(mx, "mx---", b[j])
            if mx==b[j]:
                ans1+=mx-mn
                print(ans1, "ans1--")
                i=j+1
                break
    print(ans1)