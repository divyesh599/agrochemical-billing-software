for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split(" ")))

    brr = sorted(arr)
    tarr=[0]*n
    for i in range(n):
        if arr[i]==brr[i]:
            tarr[i]=1
    