mas = [-1, 20, 11, 15, 1, 15, 48, -15, 5, -10]
ex_el = mas[0]

for el in mas:
    if (el % 2 == 0):
        if (ex_el < el):
            ex_el = el

print(ex_el)
