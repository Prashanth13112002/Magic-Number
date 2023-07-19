def sum_of (arr):
    sum=0
    for i in arr:
        sum+=i
    b=[]
    if sum>=10:
        j=str(sum)
        for i in j:
            b.append(int(i))
        return sum_of (b)
    if(sum<10):
        if(sum==1):
            return 1
        else:
            return 0

a=list(map(int,input().split()))
print(sum_of(a))


