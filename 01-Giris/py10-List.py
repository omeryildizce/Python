import numbers
from black import maybe_install_uvloop


message = "Hello there. My name is Ömer YILDIZ.".split()

print(message[0])


mylist = [1, 2, 3]
mylist2 = ["bir", 2, True, 3, 4.4, 5.6, 6.00001 ]


print(mylist)
print(mylist2)

list1=["bir","iki","üç"]
list2=["dört","beş","altı"]

numbers = list1+list2

print(numbers)
print(len(numbers))  # Eleman sayısı


userA = ["Ömer", 27]
userB = ["Ali", 18]

users = userA + userB

print(userA)
print(userB)
print(users)


print(users[0][:2])
