words = []
word = ""
i = 0

with open('filename.txt', 'r') as file:
    contents = file.read() 

while i < len(contents):
    
    if contents[i] != " ":
        word += contents[i]
        if i == len(contents) - 1:
            words.append(word)
    elif contents[i] == " ":
        if len(word) > 0:
            words.append(word)
            word = ""
    i += 1

    
print("Total de palabras: ", len(words))
print(words)