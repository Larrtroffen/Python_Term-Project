# 练习3
def nextPrime(n):
    m = 2
    while True:
        if judgePrime(m) and m > n:
            return m
        else:
            m+=1

def judgePrime(n):
    judge = True
    for i in range(2,n):
        if n % i == 0:
            judge = False
            break
    return judge

if __name__ == "__main__":
    n = int(input("请输入一个整数："))
    print(nextPrime(n))