#将一个数字的每一位存入一个list中
def getsum(n:int)-> List[int]:
    result = []
    while n:
        n,r = divmod(n,10)
        result.append(r)
    return result