yol = "6-Files//p04Updating.txt"

with open(yol, "r+", encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.write("\nfor i in range(100):print(i)")


with open(yol,"a",encoding="utf-8") as file:
    file.write("\nÖmer Yıldız")

with open(yol,"r+",encoding="utf-8") as file:
    content = file.read()
    print(content)

with open(yol,"r+",encoding="utf-8") as file:
    content = file.read()
    content = "Ömer Yıldız\n*****\n" + content
    file.seek(0)
    file.write(content)
    print(content)

with open (yol ,"r+",encoding="utf-8")as file:
    list = file.readlines()
    list.insert(int(len(list)/2),"99999999999999999999999999999999999999999999999999999\n")
    file.seek(0)
    # for i in list:
    #     file.write(i)
    # print(file.read())
    file.writelines(list)