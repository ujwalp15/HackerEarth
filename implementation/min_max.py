n = int(raw_input())
l=[int(num) for num in raw_input().split(" ")]

min_index = min(l)
max_index = max(l)

for i in range(min_index+1,max_index):
	if i not in l:
		print "NO"
		exit()
print "YES"
