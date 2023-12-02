import json

def read_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
        return None

def write_json(file_name, data):
  with open(file_name, 'w', encoding='utf-8') as file:
      json.dump(data, file, indent=2, ensure_ascii=False)

def print_json_content(file_name):
    data = read_json(file_name)
    if data:
        print(json.dumps(data, indent=2, ensure_ascii=False))

def add_record(file_name, student_name, subject, grades):
    data = read_json(file_name)
    if data:
        if student_name not in data:
            data[student_name] = {"Предмети": {}}
        data[student_name]["Предмети"][subject] = grades
        write_json(file_name, data)
        print(f"Запис для {student_name} успішно додано.")

def delete_record(file_name, student_name):
    data = read_json(file_name)
    if data and student_name in data:
        del data[student_name]
        write_json(file_name, data)
        print(f"Запис для {student_name} успішно видалено.")
    else:
        print(f"Запис для {student_name} не знайдено.")

def search_by_subject(file_name, subject):
    data = read_json(file_name)
    if data:
        matching_students = [student for student, values in data.items() if subject in values["Предмети"]]
        if matching_students:
            print(f"Студенти, які мають предмет {subject}:")
            for student in matching_students:
                print(student)
        else:
            print(f"Предмет {subject} не знайдено у жодного студента.")

def calculate_average_grades(data):
    averages = {}
    class_average = 0

    for student, subjects in data.items():
        total_grades = 0
        total_subjects = 0
        for subject, grades in subjects["Предмети"].items():
            total_grades += sum(grades)
            total_subjects += len(grades)

        if total_subjects > 0:
            student_average = total_grades / total_subjects
            averages[student] = student_average
            class_average += student_average

    if len(data) > 0:
        class_average /= len(data)
        return averages, class_average
    else:
        return None, None

def high_achievers(file_name, output_file):
  data = read_json(file_name)
  if data:
      averages, class_average = calculate_average_grades(data)
      if averages and class_average:
          print(f"Середня оцінка по класу: {class_average:.2f}")
          high_achievers_list = {student: average for student, average in averages.items() if average > class_average}
          write_json(output_file, high_achievers_list)
          print(f"Учні в яких середня оцінка вища середньої в класі записані в файл {output_file}")
      else:
          print("Немає даних для розрахунку середніх оцінок.")

# Головна функція для виклику інших функцій у діалоговому режимі
def main():
    json_file = "students.json"
    json_result = "result.json"
    while True:
        print("\nМеню:")
        print("1. Виведення на екран вмісту JSON файлу")
        print("2. Додавання нового запису у JSON файл")
        print("3. Видалення запису з JSON файлу")
        print("4. Пошук даних у JSON файлі за предметом")
        print("5. Розрахунок середніх оцінок та виведення студентів з вищою середньою")
        print("6. Вихід")

        choice = input("Оберіть опцію (1-6): ")

        if choice == "1":
            print_json_content(json_file)
        elif choice == "2":
            student_name = input("Введіть ім'я студента: ")
            subject = input("Введіть предмет: ")
            grades_str = input("Введіть оцінки через кому: ")
            grades = [int(grade) for grade in grades_str.split(',')]
            add_record(json_file, student_name, subject, grades)
        elif choice == "3":
            student_name = input("Введіть ім'я студента для видалення: ")
            delete_record(json_file, student_name)
        elif choice == "4":
            subject = input("Введіть предмет для пошуку: ")
            search_by_subject(json_file, subject)
        elif choice == "5":
            high_achievers(json_file, json_result)
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
  students = {
   "Сидоренко Олександр Віталійович": {
   "Предмети": {
   "Математика": [5, 4, 3, 4, 5],
   "Програмування": [4, 4, 4, 4, 3],
   "Фізика": [3, 5, 3, 4, 5],
   "Іноземна мова": [5, 4, 5, 4, 3],
   "Фізкультура": [5, 4, 4, 4, 3]
   }
   },
   "Коваленко Анна Ігорівна": {
   "Предмети": {
   "Математика": [4, 3, 3, 3, 4],
   "Програмування": [5, 5, 4, 4, 5],
   "Фізика": [3, 4, 4, 3, 3],
   "Іноземна мова": [5, 5, 4, 4, 5],
    "Фізкультура": [3, 3, 4, 4, 3]
   }
   },
   "Петренко Максим Васильович": {
   "Предмети": {
   "Математика": [4, 3, 2, 3, 5],
   "Програмування": [5, 3, 4, 4, 3],
   "Фізика": [3, 4, 5, 3, 4],
   "Іноземна мова": [2, 3, 4, 4, 3],
    "Фізкультура": [5, 4, 5, 5, 3]
  }
   },
   "Іванова Юлія Петрівна": {
   "Предмети": {
   "Математика": [3, 3, 4, 3, 5],
   "Програмування": [5, 4, 4, 4, 3],
   "Фізика": [3, 4, 5, 5, 3],
   "Іноземна мова": [5, 3, 4, 4, 3],
   "Фізкультура": [4, 4, 4, 3, 3]
  }
   }
  }
  jsonData = json.dumps(students)
  with open("students.json", "wt") as file:
    file.write(jsonData)
  main()
