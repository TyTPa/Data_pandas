import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=6)

#Кастомизируем график:

plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма")

# Показываем график:

plt.show()

x= np.random.rand(5)  # массив из 5 случайных чисел
y= np.random.rand(5)
print(x)
plt.scatter(x, y)

#Кастомизируем график:

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")

#Показываем график:

plt.show()