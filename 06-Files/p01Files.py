# open("6-Files//p01File.txt","x")
# x: create
 
yol = "6-Files//p01File.txt"

file = open(yol,"w",encoding="utf-8")
file.write("Hüseyin Şahin")
file.close()

file = open(yol,"a",encoding="utf-8")
file.write(" Fenerbahçeli.\n")
file.write("...")
file.close()

