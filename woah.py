failinimi = input("sisestage faili nimi: ")
fail = open(failinimi, encoding = "UTF-8")
sisu = fail.readlines()
print(sisu[0])