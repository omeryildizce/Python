from pprint import pprint
import re
result = dir(re)

str = "Python Kursu: Python programlama rehberiniz | 40 saat"

print(re.findall("Python",str))
print(len(re.findall("Python",str)))

print(re.split(" ",str))
print(re.sub(" ","-",str))
print(re.sub("\s","-",str))

print(re.search("Python",str))
print(re.search("Python",str).span())
print(re.search("Python",str).start())
print(re.search("Python",str).group())
print(re.search("Python",str).string())

