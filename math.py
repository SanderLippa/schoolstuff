from math import *
ringiläbimõõt = float(input("sisesta läbimõõt: "))
raadius = (ringiläbimõõt / 2)
pindala = pi*raadius**2
print("ringi pindala on:",pindala)
küljekõrgus = float(input("sisesta silindri külje kõrgus: "))
küljepind = (2*pi*raadius)*küljekõrgus
ruumala = (pi*raadius**2)*küljekõrgus
print("silindri külje pindala on:",küljepind,"ja ruumala on",ruumala)
    