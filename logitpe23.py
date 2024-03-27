knimi = "sander"
kparool = "1234"
i = 0
while i < 3:
    nimi = input("sisestage kasutajanimi: ") 
    parool = input("sisestage parool: ")
    if nimi != knimi:
        print("vale kasutajanimi")
    if parool != kparool:
        print("vale parool")
        i+=1
    else:
        kood = input("sisestage kood:")
        kood2 = len(kood)
        if kood2 == 6:
            print("olete sisse logitud")
            exit()
        else:
            print("2fa koodis on 6 numbrit")
            i+=1