'''
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere
Populati corect celelalte liste
Afisati cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar%2 ==0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar >0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista nr. pare: {numere_pare}')
print(f'Lista nr. impare: {numere_impare}')
print(f'Lista nr. pozitive: {numere_pozitive}')
print(f'Lista nr. negative: {numere_negative}')