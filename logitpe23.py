temp = int(input("sisestage temperatuur "))
sun = input("kas päike paistab ")
lipp = input("kas rannas on roheline lipp")

if lipp == 'jah':
    print("Võid minna randa!")
else:
    if temp >=20 and sun == 'jah':
        print("Võid minna randa!")
    elif temp <=19 or sun == 'ei':
        print("Täna ei tasu randa minna.")
