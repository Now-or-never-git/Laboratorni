arr = []

while True:
    item = input("Введіть елемент масиву (або введіть 'stop' щоб завершити): ")
    if item == 'stop':
        break 
    arr.append(item) 

varr = arr[1::2]
print("Список в якому кожен другий елемент першого списку : ", varr)
