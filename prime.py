N = int(input())
for num in range(2,N):
    if all(num%i!=0 for i in range(2,num)):
       print (num, end=" ")
