import math
from addmain import an2sa
def ansa(a,b):
  if a>=15:
    z=math.sin(2*a)+math.cos(2*b)
  else:
    z=math.sqrt(a+b**2)
  return z  

a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
while a<0 and a+b**2<0:
  print("При заданих значеннях a та b вирішення виразу не є можливим")
  a = int(input("Введіть значення a: "))
  b = int(input("Введіть значення b: "))
print ("Значення виразу z = ", ansa(a,b))

n = int(input("Введіть значення n: "))
while n<1:
  n = int(input("Введіть значення n більше 0: "))
print ("Значення виразу n = ", an2sa(n))
