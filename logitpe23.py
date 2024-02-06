from time import sleep
i = int(input("sisesta aeg sekudited"))
while i >0:
    print(i)
    sleep(1)
    i -= 1
    if i == 0:
        break