with open("FILE", "w", encoding="utf-8") as stream:
    word = "DEFAULT"
    while word != "":
        word = input("Input a word: ")
        if word[-2:] == "re" or word[-2:] == "ri":
            stream.write(word)
            stream.write("\n")
if not stream.writable:
    print("File not accessible.")
