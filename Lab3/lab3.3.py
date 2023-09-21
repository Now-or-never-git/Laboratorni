text = str(input("Введіть слово, в якому більше ніж 3 символи: "))

while (len(text) <4):
  text = str(input("Введіть ще раз слово, так як в ньому менше ніж 3 символи: "))
  
words = text.split()
maswords = []

for word1 in words:
  if word1 not in maswords:
    maswords.append(word1)


print("Унікальні слова у реченні:")
for i in range (len(maswords)):
  print(maswords[i])
