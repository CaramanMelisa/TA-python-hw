'''
12. Functie calculator care sa returneze 4 valori
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
'''
def calculator(x, y):
    a=x+y
    print(f'Suma: {a}')
    b=x-y
    print(f'Diferenta {b}')
    c=x*y
    print(f'Inmultirea: {c}')
    d=x/y
    print(f'Impartirea: {d}')
print(calculator(9,9))
