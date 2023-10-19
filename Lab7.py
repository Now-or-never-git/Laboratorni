students = {
    "Ivanov": [5, 4, 3, 4, 5, 3, 4, 4, 5, 3, 4, 5],
    "Petrov": [4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 4, 3],
    "Cudorov": [3, 5, 3, 4, 5, 4, 3, 5, 3, 4, 5, 3],
    "Ocmenko":[5, 4, 5, 4, 3, 4, 5, 5, 4, 4, 4, 5],
    "Lubich": [4, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 4],
    "Stroganov": [5, 5, 4, 5, 5, 5, 4, 4, 5, 5, 5, 4],
    "Nikolaenko": [3, 4, 4, 3, 3, 4, 4, 4, 3, 4, 4, 4],
    "Prikhodko": [5, 5, 5, 4, 5, 5, 4, 5, 4, 4, 5, 5],
    "Derizemlya": [4, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 3],
    "Zhuk": [3, 4, 5, 5, 3, 5, 5, 5, 3, 3, 4, 4]
}

def printS(spusok):
    for key, grades in spusok.items():
        print(f"{key}: {grades}")

def addS(spusok, name, grades):
    if name in spusok:
        print("Учень з таким іменем вже існує.")
    else:
        spusok[name] = grades
        print(f"Запис для {name} додано до словника.")

def removeS(spusok, name):
    if name in spusok:
        del spusok[name]
        print(f"Запис для {name} видалено зі словника.")
    else:
        print("Учень з таким іменем не знайдений.")

def sort(spusok):
  sorted_dict = {key: spusok[key] for key in sorted(spusok)}
  print("Відсортований словник:")
  for key, grades in sorted_dict.items():
      print(f"Оцінки {key} - {grades}")

def average(grades):
    return sum(grades) / len(grades)

def main():
    while True:
        print("\nОберіть дію:")
        print("1. Вивести всі оцінки учнів")
        print("2. Додати запис у словник")
        print("3. Видалити запис із словника")
        print("4. Вивести відсортовані записи із словника")
        print("5. Вивести середні оцінки")  
        print("6. Вийти з програми")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print("\nСписок учнів та їх оцінок:")
            printS(students)
        elif choice == "2":
            name = input("Введіть прізвище учня: ")
            grades = [int(x) for x in input("Введіть оцінки учня через пробіл:").split()]
            addS(students, name, grades)
        elif choice == "3":
            name = input("Введіть прізвище учня, якого бажаєте видалити: ")
            removeS(students, name)
        
        elif choice == "4":
            print("\nВміст словника, відсортований за ключами:")
            sort(students)
        elif choice == "5":
            averageM = average(
              [average(grades) for grades in students.values()]
            )
            print(f"Середня оцінка в класі: {averageM:.2f}")
            print("Учні з вищою середньою оцінкою:")
            for name, grades in students.items():
                averageS = average(grades)
                if averageS > averageM:
                    print(f"{name}: {averageS:.2f}")      
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
