temp = int(input("sisestage temperatuur "))
sun = input("kas p�ike paistab ")
lipp = input("kas rannas on roheline lipp")

if lipp == 'jah':
    print("V�id minna randa!")
else:
    if temp >=20 and sun == 'jah':
        print("V�id minna randa!")
    elif temp <=19 or sun == 'ei':
        print("T�na ei tasu randa minna.")
