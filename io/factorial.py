N = int(raw_input())

def fact ( num ):
    sum = 1
    while num>0:
        sum = sum * num
        num -= 1
    return sum

n = fact(N)
print n
