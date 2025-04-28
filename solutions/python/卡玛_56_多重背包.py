C,N = map(int,input().split())
weight = list(map(int,input().split()))
value  =  [int(x) for x in input().split(" ") if x]
nums   = list(map(int,input().split()))

dp = [0] * (C+1)
for i in range(N):
    for j in range(C,weight[i]-1,-1):
        for k in range(1,nums[i]+1):
            if k * weight[i] > j:
                break
            dp[j] = max(dp[j],dp[j-weight[i]*k]+value[i]*k)

print(dp[-1]) 
