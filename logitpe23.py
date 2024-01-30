# algus
aeg = float(input("sisestage aeg "))
distants = float(input("sisestage distants "))

#jooksu valemi kraam
A_h = 0.14354
B_h = 220
C_h = 1.4

#teise ajsa kraam
A_js = 25.4347
B_js = 18
C_js = 1.81

# ma soovin surra 
ajaline = int(A_js*(B_js-aeg)**C_js)
distantsiline = int(A_h*(distants-B_h)**C_h)

#prindi tulemused
print(ajaline+distantsiline)