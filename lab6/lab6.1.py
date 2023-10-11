arr = []

while True:
    item = input("Введіть елемент масиву (або введіть 'stop' щоб завершити): ")
    if item == 'stop':
        break 
    arr.append(item) 
print("Кількість елементів списку: ", len(arr))

print("Елементи списку в зворотньому порядку: ", arr[::-1])
