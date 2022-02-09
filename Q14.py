a = True

while a == True:
    word = str(input("Enter the word: "))
    lower = word.count('a')
    upper = word.count('A')
    if word.upper() == "NO":
        a = False
    else:
        print(lower + upper)
