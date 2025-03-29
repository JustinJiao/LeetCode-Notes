# 卡玛网 54 替换数字
# 题目链接: https://kamacoder.com/problempage.php?pid=1064

#方法一
def replace (l)->str:
    result = []
    for i in range(len(l)):
        if l[i].isdigit():
            result.append("number")
        else:
            result.append(l[i])
    return "".join(result)

def main():
    import sys
    data = sys.stdin.read().strip()
    l = list(data)
    result = replace(l)
    print(result)

if __name__ == "__main__":
    main()