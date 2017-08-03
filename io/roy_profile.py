l = int(input())
N = int(input())
w = []
h = []
for i in range(N):
    a,b = input().split()
    a = int(a)
    b = int(b)
    w.append(a)
    h.append(b)

for i in range(N):
    if w[i]<l or h[i]<l:
        print ("UPLOAD ANOTHER")
    elif w[i] == h[i]:
        print ("ACCEPTED")
    elif w[i]>l or h[i]>l:
        print ("CROP IT")
    else:
        print ("ACCEPTED")
