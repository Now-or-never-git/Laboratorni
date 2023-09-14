a = int(input("Введіть значення а: "))
while (a <= 1 or a >= 9) :
    a = int(input("Введіть значення а: "))
for i in range(1, a + 1) :
  for j in range(1, a + 1) :
    if j < i :
      print(" ", end = " ")
    else :
      print(j, end = " ")
  print("")