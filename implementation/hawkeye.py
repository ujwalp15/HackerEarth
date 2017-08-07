a=input()
l=[int(x) for x in raw_input().split()]
for i in range(a):
    for j in range(a):
        if(abs(l[0]-i)>abs(l[1]-j)):
            print max(0,l[2]-abs(l[0]-i)),
        else:
            print max(0,l[2]-abs(l[1]-j)),
    print ''
