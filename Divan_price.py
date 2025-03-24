#Код, написанный с использованием  Selenium.
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/divany"
driver.get(url)
time.sleep(10)

divans = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

parsed_data = []

for divan in divans:
    try:
        price = divan.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([price])

driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])
    writer.writerows(parsed_data)


def clean_price(price):

        # Удаляем "руб." и преобразуем в число
    return int(price.replace('руб.', '').replace(' ', ''))


# Чтение данных из исходного CSV файла и их обработка
input_file = 'divan.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                      encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

 # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

        # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")
# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'Цена'
prices = data['Цена']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')


# Показать гистограмму
plt.show()