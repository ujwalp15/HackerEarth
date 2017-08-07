k = int(input())
str = input()
n = len(str)
current = 0
count = 0
result = 0
data = [n + 1] * 26

for i in range(n):
  ch = ord(str[i]) - ord('a')

  if data[ch] == n + 1:
    if count < k:
      count += 1
    else:
      next = min(data)
      ind = data.index(next)
      data[ind] = n + 1
      current = next + 1

  data[ch] = i
  if count == k:
    next = min(data)
    result += next - current + 1

print(result)
