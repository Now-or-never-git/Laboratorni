import matplotlib.pyplot as plt

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


percentages = {}
for student, subjects in students.items():
    total_points = sum(sum(subjects["Предмети"][subject]) for subject in subjects["Предмети"])
    total_subjects = sum(len(subjects["Предмети"][subject]) for subject in subjects["Предмети"])
    average_percentage = (total_points / (total_subjects * 5)) * 100
    percentages[student] = average_percentage


plt.figure(figsize=(8, 8))
labels = list(percentages.keys())
plt.pie(list(percentages.values()), labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Відсоткові показники студентів за середнім балом')
plt.show()