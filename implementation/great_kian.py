N = int(raw_input())
numArray = map(int, raw_input().split())
sum1 = sum2 = sum3 = 0

for i,n in enumerate(numArray, 1):
    if i%3 == 1:
        sum1 += n
    elif i%3 == 2:
        sum2 += n
    else:
        sum3 += n

print sum1,sum2,sum3
