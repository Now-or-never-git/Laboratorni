N = 30
a = 0
s = 0
for i in range(1, N + 1) :
  s += 1 / i
  a += 1
print("Сума ряду: ", round(s, 4))
print("Кількість членів ряду: ", a)

