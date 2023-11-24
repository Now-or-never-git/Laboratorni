import csv
import os

def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            for row in csv_reader:
                data.append(row)
        return headers, data
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено!")
        return None, None

def display_csv(headers, data):
    if headers and data:
        print(','.join(headers))
        for row in data:
            print(','.join(row))
    else:
        print("Немає даних для відображення.")

def search_csv(input_countries, headers, data, output_file):
    if not headers or not data:
        print("Немає даних для пошуку.")
        return

    result_data = [headers]
    flag = False

    for country in input_countries:
        for row in data:
            if country.lower() in row[2].lower(): 
                result_data.append(row)
                flag = True

    if flag:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(result_data)
        print(f"\nРезультати пошуку для країн {', '.join(input_countries)} записані у файл {output_file}.")
    else:
        print(f"\nДля країн {', '.join(input_countries)} не знайдено відповідних записів.")

if __name__ == "__main__":
    input_file_path = 'Data.csv'
    output_file_path = 'sata.csv'

    headers, data = read_csv(input_file_path)

    print("\nЗміст вхідного CSV-файлу:")
    display_csv(headers, data)

    if headers and data:
        input_countries = input("Введіть назви країн (через кому): ").split(',')
        search_csv(input_countries, headers, data, output_file_path)
