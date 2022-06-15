def cube():
    result=[]

    for i in range(5):
        result.append(i**3)
   
    return result

print(cube())

# generator
def cubeg():
    for i in range(5,1001):
       yield i**3 

print(cubeg())
iterator = cubeg()
#iterator = iter(generator)

for i in iterator:
    print(i)