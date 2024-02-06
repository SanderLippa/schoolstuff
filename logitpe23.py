arv1 = int(input("sisestage esimene arv "))
tehe = (input("(+ |  -  | * | /) "))
arv2 = int(input("sisestage teine arv "))

if tehe == '/' and arv1 or arv2 ==0:
    vastus = "Nulliga ei saa jagada."

elif tehe == '+':
    vastus = arv1+arv2
    
elif tehe == '-':
    vastus = arv1-arv2
    
elif tehe == '*':
    vastus = arv1*arv2
    
elif tehe == '/':
    vastus = arv1/arv2

print(vastus)
