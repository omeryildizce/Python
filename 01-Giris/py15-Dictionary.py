sehirler = ["Kocaeli", "istanbul"]
plakalar = [41,34]

plakalar = {"Kocaeli":41, "İstanbul":34}


print(plakalar["Kocaeli"])

plakalar["Ankara"] = 6
print(plakalar)

users = {
    "Ömer" : {
        "age":36,
        "years" : 2000
    },
    "Ali" : {
        "age":16,
        "years" : 2008
    }
}

print(users["Ömer"]["age"])
