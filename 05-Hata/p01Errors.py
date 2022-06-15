#
##
###
# print(a)          => name error
# int("1as2")       => valu error
# x/0               => ZeroDivisionError
# print("van" van)  => SyntaxError
###
##
#

try:
    x = int(input("X : "))
    y = int(input("Y : "))
    print(x/y)
except:
    print("undefined")
     
        
"""****************************************"""
try:
    x = int(input("X : "))
    y = int(input("Y : "))
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print("undefined")
    print(e) # hangi hata
"""*****************************************"""
while True:        
    try  :
        x = int(input("X : "))
        y = int(input("Y : "))
        print(x/y)
    except Exception as ex:
        print("undefined", ex)
    else:
        break
    finally:
        print("finally")
