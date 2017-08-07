t = int(raw_input())
for i in range(t) :
    st1 = raw_input().split()
    st2 = raw_input().split()
    ammo = int(st1[0])
    finish = True
    for j in range(int(st1[1])) :
        if st2[j] == '1' :
            ammo += 2
        else :
            ammo -=1
            if ammo == 0  and j != int(st1[1])-1 :
                finish = False
                ammo = j+1
                break
    if finish :
        print 'Yes',ammo
    else :
        print 'No',ammo
