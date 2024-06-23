c, o, n = False, False, False

word = ""

while True:
    letter = input()

    if letter == "End":
        break

    if letter not in "con" and letter.isalpha():
        word += letter
        continue

    if c and letter == "c":
        word += "c"
    elif o and letter == "o":
        word += "o"
    elif n and letter == "n":
        word += "n"

    if not c and letter == "c":
        c = True
    elif not o and letter == "o":
        o = True
    elif not n and letter == "n":
        n = True

    if c and o and n:
        print(word, end=" ")
        word = ""
        c = False
        o = False
        n = False
