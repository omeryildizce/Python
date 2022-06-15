meyveler = {"elma", "armut", "portakal"}

# print(meyveler[0]) //kümeler indexlenemez

for meyve in meyveler:
    print(meyve)

meyveler.add("ananas")
meyveler.update(["mango","muz"])

meyveler.remove("elma")
meyveler.discard("armut")

print(meyveler)