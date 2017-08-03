N = int(input())

numArray = list(map(int, raw_input().split()))
ans = 1
for item in numArray:
    ans = (ans*item)%(10**9+7)
print (ans)
