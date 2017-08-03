def isArmstrong( num ):
    string = str(num)
    sum = 0
    l = len(string)
    for digit in string:
        sum += int(digit)**l
        if sum > num:
            return False

    if sum != num:
        return False

    if sum == num:
        return True



start = int(raw_input())
end =  int(raw_input())
for num in range(start,end + 1):
    if isArmstrong(num):
        print num
