x = "global x"

def function():
    x= "local x"
    print(x)

print(x)
function()
print(x)


x=50
name = "ömer"
def Name(n):
    name = n
    print(name)
    global x 
    x=100
Name("Ali")
print(name)
print(x)