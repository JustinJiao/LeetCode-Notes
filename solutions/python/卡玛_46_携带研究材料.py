# 卡玛网 46 携带研究材料
# 题目链接: https://kamacoder.com/problempage.php?pid=1046

from typing import List
import sys
def f (bagV:int,weight:List[int],value:List[int]):
    num = len(weight) #物品数量
    dp = [[0]*(bagV+1) for _ in range(num)]

    for i in range(num):
        dp[i][0] = 0
    for j in range(bagV+1):
        if j < weight[0]:
            dp[0][j] = 0
        else:
            dp[0][j] = value[0]
    
    for i in range(1,num):
        for j in range(1,bagV+1):
            if j<weight[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],value[i]+dp[i-1][j-weight[i]])
    return dp[num-1][bagV]

def main():
    data = sys.stdin.read().split()
    num = int(data[0])
    bagV = int(data[1])
    weight = list(map(int,data[2:num+2]))
    value = list(map(int,data[num+2:num+2+num]))
    print(f(bagV,weight,value))

if __name__ == "__main__":
    main() 
    
""" M,bagV = map(int,input().split())
weight = list(map(int,input().split()))
value =  list(map(int,input().split()))

dp = [0] * (bagV+1)

dp[0] = 0

for i in range(M):
    for j in range(bagV,-1,-1):
        if weight[i] <= j:
            dp[j] = max(dp[j],value[i]+dp[j-weight[i]])

print(dp[bagV]) """