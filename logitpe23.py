import linecache
failinimi = input("sisestage faili nimi: ")
fail = open(failinimi, encoding = "UTF-8")
i = 0
for rida in fail:
    i+=1
    print(str(+i)+".",rida)
fail.close
test = int(input("sisesta number: "))
loe = linecache.getline(failinimi, test)
print(loe)