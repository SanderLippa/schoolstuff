from time import sleep
i = int(input("sisesta aeg"))
if i == 0:
    print("0")
while i >0:
    print(i)
    sleep(1)
    i -= 1
    if i == 0:
        print("0")
        break