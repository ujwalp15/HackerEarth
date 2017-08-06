list_num = list()
list_num.append(0)

for i in range(1, 100001):
    c = 1
    x = i
    while x > 0 and x % 5 == 0:
        x /= 5
        c += 1
    list_num.append(list_num[i - 1] + c)

def find_num (n):
    l = 0
    c = 50000
    r = 100000
    while l <= r:
        if n == ARR[c]:
            print(5)
            print(5 * c, end=' ')
            print(5 * c + 1, end=' ')
            print(5 * c + 2, end=' ')
            print(5 * c + 3, end=' ')
            print(5 * c + 4)
            break
        elif n < ARR[c]:
            r = c - 1
            c = int((l + r) / 2)
        else:
            l = c + 1
            c = int((l + r) / 2)

        if l > r:
            print(0)

T = int(input())
for _ in range(T):
    a = int(input())
    find_num(a)
