yol = "6-Files//p03Traversing.txt"

with open(yol,"r",encoding="utf-8") as file:
    text = file.read()
    print(text)
    print(file.tell())

    file.seek(10)
    text2 = file.read(10)
    print(text2)
    print(file.tell())

