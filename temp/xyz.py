for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split(" ")))

    ans=arr[0]&arr[1]

    for i in range(n-1):
        for j in range(i+1, n):
            ans=ans|(arr[i]&arr[j])
    
    print(ans)
