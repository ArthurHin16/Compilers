text = input("Ingrese el texto: ")
letter = input("Ingrese el carácter: ")
new = ""
for i in range(len(text)):
    if text[i] == letter:
        new += '*'
    else:
        new += text[i]
print(new)