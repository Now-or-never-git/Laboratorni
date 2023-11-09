def Open(file_name, mode):
  """Відкриває файл."""
  try:
    file = open(file_name, mode)
  except IOError:
    print("Файл", file_name, "не було відкрито!")
    return None
  else:
    print("Файл", file_name, "було відкрито!")
    return file


def create(file_name):
  file = Open(file_name, 'w')
  if (file !=None):
      strings = ["Hel1lo", "12345", "Python", "559", "World", "22fGhIjK", "9843210"]
      for string in strings:
          file.write(string + '\n')
      file.close()
      print("Файл було закрито.")


def sort(input_file, output_file, temp_file):
  input_file=Open(input_file, 'r')
  if (input_file !=None):
      content = input_file.read().replace('\n', '')

      digits = ''.join([char for char in content if char.isdigit()])
      other_chars = ''.join([char for char in content if not char.isdigit()])

      temp_file= Open(temp_file, 'w')
      if (temp_file !=None):
          temp_file.write(digits[:10] + '\n')
          for i in range(10, len(digits), 10):
              temp_file.write(digits[i:i+10] + '\n')
          for i in range(0, len(other_chars), 10):
              temp_file.write(other_chars[i:i+10] + '\n')
          input_file.close()
          temp_file.close()
          print("Файли було закрито.")

          temp_file = Open(str(temp_file.name), 'r') 
          if (temp_file !=None):
              sorted_content = temp_file.readlines()

              output_file=Open(output_file, 'w')
              if (output_file !=None):
                  output_file.writelines(sorted_content)
                  output_file.close()
                  temp_file.close()
                  print("Файли було закрито.")


def print_file(file_name):
  file = Open(file_name, 'r')
  if (file !=None):
    print("Вміст файлу",file_name, ": ")
    content = file.readlines()
    for line in content:
      print(line.strip())
    file.close()
    print("Файл було закрито.")


TF17_1 = "TF17_1.txt"
TF17_2 = "TF17_2.txt"
TF17_3 = "TF17_3.txt"

create(TF17_1)
sort(TF17_1, TF17_2, TF17_3)
print_file(TF17_2)
