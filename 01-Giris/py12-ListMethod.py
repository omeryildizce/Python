



numbers = [1.5,2,3,4,5,6,7,8,9,10,29 ]
letters = ["a","s","d","f","g","h","j","k","l","ş","i","z"]



print(min(numbers))
print(max(numbers))
print(min(letters))
print(max(letters))


numbers.append(49) # eleman ekler
numbers.insert(5,17)

numbers.pop() # son elemanı siler
numbers.pop(4) # 4. elemanı siler

numbers.remove(2) # 2 yi sil

numbers.sort() # küçükten büyüğe sırlama
letters.sort()

print(numbers)
print(letters)

numbers.reverse() # ters çevir
letters.reverse()


print(numbers)
print(letters)

numbers.count(4) # kaç tane 4 var

numbers.clear() # elemanları siler
