num = int(raw_input())

for i in range(num):
    seat = int(raw_input())
    rem = seat%12
    if rem == 0:
        seat -= 11
        print seat,"WS"
    elif rem == 1:
        seat += 11
        print seat,"WS"
    elif rem == 2:
        seat += 9
        print seat,"MS"
    elif rem == 3:
        seat += 7
        print seat,"AS"
    elif rem == 4:
        seat += 5
        print seat,"AS"
    elif rem == 5:
        seat += 3
        print seat,"MS"
    elif rem == 6:
        seat += 1
        print seat,"WS"
    elif rem == 7:
        seat -= 1
        print seat,"WS"
    elif rem == 8:
        seat -= 3
        print seat,"MS"
    elif rem == 9:
        seat -= 5
        print seat,"AS"
    elif rem == 10:
        seat -= 7
        print seat,"AS"
    elif rem == 11:
        seat -= 9
        print seat,"MS"
