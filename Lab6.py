def funk1(arr):
  print("Кількість елементів списку: ", len(arr))
  print("Елементи списку в зворотньому порядку: ", arr[::-1])
  
def funk2(arr):
  varr = arr[1::2]
  print("Список в якому кожен другий елемент першого списку : ", varr)

def funk3():
  text = input("Введіть текст: ") 
  Mtext=set()  
  for i in text:
     if text.count(i) == 1:
       Mtext.add(i) 
  print("Унікальні символи, які входять в текст лише один раз:")
  print(Mtext)


arr = [] 
while True:
  item = input("Введіть елемент списку (або введіть 'stop' щоб завершити): ")
  if item == 'stop':
      break 
  arr.append(item)


funk1(arr)
funk2(arr)
funk3()
