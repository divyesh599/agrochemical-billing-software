for _ in range(int(input())):
    n = int(input())
    arr=[]
    x=[]

    for i in range(n):
        l, r, c=map(int, input().split(" "))
        if i==0:
            arr.append([l, r, c])
            x=[l, r, c]
            print(x[2])
        else:
            if x[0]<=l<=r<=x[1]:
                pass
            elif l<=x[0]<=x[1]<=r:
                pass
            elif x[1] <= l and x[0] <=
                y=[0, 0, 0]
                # arr[j] & l,c,r
                for j in range(i+1):
                    if arr[j][1]<=l and arr[j][0]<=r:
                        if 
                    else:
                        y[2]+=c
                        y[0]=min(arr[j][0], l)
                        y[1]=max(arr[j][1], r)
            else:
                x[2]+=c
                x[0]=min(x[0], l)
                x[1]=max(x[1], r)
            print(x[2])