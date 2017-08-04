import re
N = int(raw_input())

for n in range(N):
    l = int(raw_input())
    ch = raw_input()

    list_of_num = list(re.findall(r'\d+', ch))
    print len(list_of_num)
