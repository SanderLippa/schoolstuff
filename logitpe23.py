pakik6rgus = float(input("sisesta k6rgus"))
pakikaal = float(input("sisesta kaal"))
if  pakik6rgus <=9:
    pakisuurus = 'S'
elif 9< pakik6rgus <=19:
    pakisuurus = 'M'
elif pakik6rgus <40:
    pakisuurus = 'L'
else:
    pakisuurus='N/A'

if pakisuurus != 'N/A':
    print("Pakk on",pakisuurus + "-suurusega ja saab saata pakiautomaadist.")
else:
     if pakik6rgus >=40 and pakikaal <=30:
        print("Pakki saab saata postkontorist või kulleriga.")
     elif pakik6rgus >=40 and pakikaal >=31:
         print("Pakki saab saata ainult postkontorist.")