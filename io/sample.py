from __future__ import print_function
N = int(input())

# Get the array
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic here:
[sumArray[i] for i in zip(numArray1,numArray2)]

# Print the sumArray
for element in sumArray:
    print(element, end=" ")

print("")
