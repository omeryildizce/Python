website = "https://www.osmedya.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

hello = " Hello World "

print(hello.strip())
print(hello.lstrip())
print(hello.rstrip())

print(course.lower())
print(course.upper())
print(course.title())
print(course.capitalize())
 
print(course.count("a"))
print(course.count("a", 0,10))

print(website.startswith("https"))
print(website.endswith("com"))

print(website.find("com"))
print(website.rfind("com")) #reverse find

print(course.isalpha())
print(course.isdigit())
print(course.isascii())

print(course.center(100,"*"))
print(course.ljust(100,"*"))
print(course.rjust(100,"*"))

print(course.replace(" ","|",2))
print(course.split(" ",2))


