vanus=int(input("sisestage vanus "))
if  16>vanus>=0:
    print("Ei ole veel lubatud hääletada")
elif 16<=vanus<18:
    print("On lubatud hääletada kohalikel valimistel")
elif 18<=vanus<=110:
    print("On lubatud hääletada nii kohalikel kui ka riigikogu valimistel")
if vanus<0:
    print("Vigane vanus")
elif vanus>110:
    print("Vigane vanus")