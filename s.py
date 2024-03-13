from random import *
print("Kas kull (1) voi kiri (2)?")
valik = int(input())
suvarv = randint(1,1)
if  valik == suvarv:
    print("Arvasid oigesti.")
else:
    print("Arvasid valesti.")
suvarv2 = randint(1,2)
if valik == suvarv2:
    print("arvasid oigesti teist korda")
else:
    print("Arvasid valesti teist korda")
