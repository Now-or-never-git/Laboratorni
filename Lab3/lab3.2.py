text = str(input("Введіть слово, в якому більше ніж 3 символи: "))

while (len(text) <4):
  text = str(input("Введіть ще раз слово, так як в ньому менше ніж 3 символи: "))
count=0

for i in range (len(text)):
  if text[i] == "_":
    count += 1
if count>0:
  print("В заданому слові символ '_' зустрічаеться разів: ", count)
else:
  print("В заданому слові символ '_' відсутній")
