# list = [1,2,3, ... , 100]

for item in range(100):
     print(item)

for item in range(20,30):
     print(item)

for item in range(20,31,2):
     print(item)

# enumarate

index = 0
text = "Hello there"
for letter in text:
    print(letter,index)
    index +=1
    
text = "Hello there"
for indeks,letter in enumerate(text):
    print(letter,indeks)
    

# zip
list1 = [1,2,3,4,5]
list2 = ["a", "b","c","d","e"]
for a,b in zip(list1,list2):
    print(a,b)

