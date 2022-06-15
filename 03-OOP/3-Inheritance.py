# inheritance (kalıtım) : Miras Alma

# Person => name, year, eat(), run()
# Student(Person), Teacher(Person)

class Person():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        print("Person created")
    def who_am_i(self):
        print(f"I am {self.name} {self.last_name} ")

    def eat(self):
        print(f"{self.name} {self.last_name} eat food")


class Student(Person):
    def __init__(self, name, last_name, number):
        Person.__init__(self, name, last_name)
        self.number = number
        print("Student created")        
    # overridr
    def who_am_i(self):
        print(f"I am {self.name} {self.last_name}  and I am a student")

    def sayHello(self):
        print("Hello I am a student")
class Teacher(Person):
    def __init__(self, name, last_name, branch):
        super().__init__(name, last_name)
        self.branch = branch
    
    def who_am_i(self):
        print("Teacher")

p1 = Person("Ali", "YILDIZ")
s1 = Student("Ömer" ,"YILDIZ", 123456)

print(p1.name+" "+p1.last_name)
print(s1.name,"  ",s1.last_name," ", s1.number)

p1.who_am_i()
s1.who_am_i()   

p1.eat()
s1.eat()
s1.sayHello()

t1 = Teacher("Kadir","Taş", "Singer")
t1.name = "Ahmet"
t1.last_name = "Kaya"
t1.branch = "Math"

t1.who_am_i()