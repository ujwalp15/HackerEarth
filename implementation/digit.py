num,val = raw_input().split()
val = int(val)
listnum = list(num)
j = 0
while True:
    if val == 0 or j > len(num):
        break
    if int(listnum[j]) < 9:
        listnum[j] = '9'
        j += 1
        val -= 1
    else:
        j += 1

num = ''.join(listnum)

print num
