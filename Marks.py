import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('dz.csv')
print(df.head())
#print(df.describe())
df['Subject'] = df['Subject'].astype('category')
math_df = df[df['Subject'] == 'Математика']

# Вычисляем среднюю оценку по предмету 'Math'
mark_by_math = math_df['Mark'].mean()
print('Средняя оценка по Математике:', mark_by_math)

# Вычисляем медиану по предмету 'Math'
median_by_math = math_df['Mark'].median()
print('Медиана как оценка по Математике:', median_by_math)

# Вычисляем квартили и межквартильный размах для оценок по математике
Q1_math = math_df['Mark'].quantile(0.25)
Q3_math = math_df['Mark'].quantile(0.75)
IQR = Q3_math - Q1_math
print('Первый квартиль:', Q1_math, 'Третий квартиль:', Q3_math, 'Межквартильный размах:', IQR)
std = df['Mark'].std()
print(f"Стандартное отклонение: {std}")