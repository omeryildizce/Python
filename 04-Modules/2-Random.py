import random

resul = dir(random)
print(resul) 

result = help(random.gauss)
print(result)



x = random.random() * 10 
print(x)

y = random.randint(0,10) 
print(y)

z = random.uniform(44,45)
print(z)
names = ["Ali"]
name = ["Ali", "Kadir","Hamit","Cengiz","Fatih","Ayşe","Ebru"]
r = random.randint(0,len(names)-1)
result = names[r]
print(result)

a = list(range(100))
random.shuffle(a)
print(a)

print(random.sample(a,5))