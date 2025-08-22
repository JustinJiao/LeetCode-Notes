# 卡玛网 58 区间和
# 题目链接: https://www.programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html#%E6%80%9D%E8%B7%AF

#方法一一前缀和
import sys
def main():
    data = sys.stdin.read().split()
    index = 0
    n = int(data[index])
    index +=1
    vec = []
    for i in range(n):
        vec.append(int(data[index+i]))
    index += n
    
    p = [0]*n
    presum = 0
    for i in range(n):
        presum += vec[i]
        p[i] = presum
    
    result = []
    while index < len(data):
        a = int(data[index])
        b = int(data[index+1])
        index +=2
        
        if a == 0:
            sum_value = p[b]
        else:
            sum_value = p[b]-p[a-1]
        
        result.append(sum_value)
    for r in result:
        print(r)
        
if __name__ == '__main__':
    main()