line = str(input("Etner string: "))

ex_char = None
count = 0
ex_count = 0
for i in range(0, len(line)):
    if (line[i] == 'н' or line[i] == "Н"):
        count += 1

    elif (line[i] == '!'):
        line = line[0:i] + '.' + line[i+1:]
        count = 0

    else:
        count = 0

    if (ex_count < count):
        ex_count = count

    ex_char = line[i]

print(f"String: {line}")
print(f"Max count of 'н' char: {ex_count}")
