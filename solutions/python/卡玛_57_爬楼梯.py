# 卡玛网 57 爬楼梯
# 题目链接: https://kamacoder.com/problempage.php?pid=1067

#方法一一维数组
n,m = map(int,input().split())
dp = [0]*(n+1)
dp[0] = 1
for j in range(1,n+1):
    for i in range(1,m+1):
        if j >= i:
            dp[j] += dp[j-i]
        
print(dp[n])

