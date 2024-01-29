emap = int(input("sisestage ema pikkus "))
isap = int(input("sisestaga isa pikkus "))
sugu = str(input("sisesta sugu "))
if sugu == ("n"):
    lapse_pikkus = (emap+isap) / 2 - 6.5
elif sugu == ("N"):
    lapse_pikkus = (emap+isap) / 2 - 6.5
if sugu == ("m"):
    lapse_pikkus = (emap+isap) / 2 + 6.5
elif sugu == ("M"):
    lapse_pikkus = (emap+isap) / 2 - 6.5
print(lapse_pikkus)