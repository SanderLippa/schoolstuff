nimi = input("sisestage nimi ")
lkiirus = int(input("lubatud kiirus "))
tegelkiirus = int(input("tegelik kiirus "))
trahv = tegelkiirus-lkiirus
trahv2 = trahv*5
if trahv2 <=300:
    print(nimi,", kiiruse ületamise eest on teie trahv",trahv2, "eurot")
else:
    print(nimi,", kiiruse ületamise eest on teie trahv 300 eurot")