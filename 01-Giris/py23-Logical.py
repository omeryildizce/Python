from unittest import result


x = 5

result = 5 < x  < 10
print(result)

result = 5 <= x  < 10
print(result)   

# and
result = x < 10 and x >= 5
print(result)


# and
result = x < 10 or x > 10
print(result)

# not
result = not( x >100) # true
print(result)




