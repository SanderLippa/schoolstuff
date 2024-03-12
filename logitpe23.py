sispin = input("sisestage pin: ")
raha = 3000000
orjad = 39
if sispin == "1234":
    print("pang:",raha)
    print("sul on",orjad,"orja")
    print("palju raha soovid:")
    rahav = int(input())
    if rahav <= raha:
        raha -= rahav
        print("teil on",raha,"eurot")
    
else:
    print("vale pin")