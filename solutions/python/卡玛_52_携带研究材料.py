# 卡玛网 52 携带研究材料
# 题目链接: https://kamacoder.com/problempage.php?pid=1052

n,bagV = map(int,(input().split()))
weight = []
value = []
for _ in range(n):
    w, v = map(int,(input().split()))
    weight.append(w)
    value.append(v)
dp = [[0] * (bagV+1) for _ in range(n)]
for j in range(weight[0],bagV+1):
    dp[0][j] = value[0] + dp[0][j-weight[0]]
for i in range(1,n):
    for j in range(bagV+1):
        if j<weight[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-weight[i]]+value[i])
print(dp[n-1][bagV])
    