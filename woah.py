investeering = float(input("Sisestage investeeritav summa (eurodes): "))
aastad = int(input("Sisestage investeeringu kogupikkus (aastates): "))
tootlus_protsentides = float(input("Sisestage oodatav aastatootlus (protsentides): "))

tootlus_kordaja = 1 + tootlus_protsentides / 100
l�ppsumma = investeering * (tootlus_kordaja ** aastad)

print(f"Teie investeeringu l�ppsumma {aastad} aasta p�rast on: {round(l�ppsumma, 2)} eurot")