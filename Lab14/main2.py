import matplotlib.pyplot as plt
import numpy as np

# Дані
years = np.arange(2000, 2016)

ukraine_data = [0.716183762, 1.238759547, 1.873885116, 3.148127588, 3.489477881, 3.749764415, 4.506124564, 6.55, 11, 17.9, 23.3, 28.70826284, 35.27, 40.954129, 46.23597546, 48.88464368]

uk_data = [26.82175435, 33.48109487, 56.48, 64.82, 65.61, 70, 68.82, 75.09, 78.39, 83.56, 85, 85.37999855, 87.47999842, 89.8441, 91.61, 92.0003]

# Графік
plt.figure(figsize=(10, 5))
plt.plot(years, ukraine_data, label='Ukraine')
plt.plot(years, uk_data, label='United Kingdom')
plt.title('Динаміка показника "Internet users" за роками')
plt.xlabel('Рік')
plt.ylabel('Internet users (per 100 people)')
plt.legend()
plt.show()

# Стовпчаста діаграма
country_input = input('Введіть країну для побудови стовпчастої діаграми (Ukraine або United Kingdom): ')
selected_country_data = ukraine_data if country_input.lower() == 'ukraine' else uk_data
selected_country_label = 'Ukraine' if country_input.lower() == 'ukraine' else 'United Kingdom'

plt.figure(figsize=(8, 5))
plt.bar(years, selected_country_data, color='skyblue')
plt.title(f'Internet users в {selected_country_label} за роками')
plt.xlabel('Рік')
plt.ylabel('Internet users (per 100 people)')
plt.show()