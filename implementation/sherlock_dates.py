from __future__ import print_function
t = int(raw_input())

for i in range(t):
    d,m,y = raw_input().split()
    d = int(d)
    y = int(y)
    if d != 1:
        print (d-1,m,y)
    else:
        if m == "January":
            print ('31 December',y-1)
        elif m == "February":
            print ('31 January',y)
        elif m == "March":
            if y%4==0 and (y%100 != 0 or y%400 == 0):
                print ('29 February',y)
            else:
                print ('28 February',y)
        elif m == "April":
            print ('31 March',y)
        elif m == "May":
            print ('30 April',y)
        elif m == "June":
            print ('31 May',y)
        elif m == "July":
            print ('30 June',y)
        elif m == "August":
            print ("31 July",y)
        elif m == "September":
            print ('31 August',y)
        elif m == "October":
            print ('30 September',y)
        elif m == "November":
            print ('31 October',y)
        elif m == "December":
            print ('30 November',y)
