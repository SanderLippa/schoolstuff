investeering = float(input("Sisestage investeeritav summa (eurodes): "))
aastad = int(input("Sisestage investeeringu kogupikkus (aastates): "))
tootlus_protsentides = float(input("Sisestage oodatav aastatootlus (protsentides): "))

tootlus_kordaja = 1 + tootlus_protsentides / 100
lõppsumma = investeering * (tootlus_kordaja ** aastad)

print(f"Teie investeeringu lõppsumma {aastad} aasta pärast on: {round(lõppsumma, 2)} eurot")