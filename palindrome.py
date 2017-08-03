str = raw_input()
rev_str = reversed(str)
if list(rev_str) == list(str):
    print ("YES")
else:
    print ("NO")
