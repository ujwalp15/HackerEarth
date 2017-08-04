b =  raw_input()
count0 = 0
result0 = 0
count1 = 0
result1 = 0
for i in b:
    if i == '1':
        count0 = 0
    else:
        count0 += 1
        result0 = max(result0,count0)

for i in b:
    if i == '0':
        count1 = 0
    else:
        count1 += 1
        result1 = max(result1,count1)

if result0 >= 6 or result1 >= 6:
    print "Sorry, sorry!"
else:
    print "Good luck!"
