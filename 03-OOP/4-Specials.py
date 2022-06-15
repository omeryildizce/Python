mylist = [1,2,3,4]
mystring = "my string"

print(len(mylist))
print(len(mystring))

print(type(mylist))
print(type(mystring))

class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu")

    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("movie silindi")

m = Movie("film","yönetmen", 120)

print(type(m)) 

print(mylist) # __str calışır
print(m)    # __str calışır
print(str(mylist)) # __str calışır
print(str(m)) # __str calışır

print("#############")
print(len(mylist))
print(len(m))

del m
 

