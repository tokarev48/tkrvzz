mas = [-1, 20, 8, 6, 1, 15, 48, -15, 5, -10]
new_mas = []

for el in mas:
    if ((el < 10) and (el % 2 == 0)):
        new_mas.append(el)

new_mas.sort()

if (new_mas != []):
    print(f"Massive: {new_mas}")
else:
    print("New massive is empty")
