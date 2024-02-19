loppseeria = int(input("Sisestage loppseeria arv: "))
summa = 0
i = 1

while i <= loppseeria:
        summa += i
        i += 1
i = loppseeria - 1
while i > 0:
        summa += i
        i -= 1

print(summa)
