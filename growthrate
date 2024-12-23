import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из Excel-файла
file_path = 'datasett.xlsx'  # Укажите путь к вашему файлу
data = pd.read_excel(file_path)

# Переименование колонок для удобства
data.rename(columns={'Unnamed: 0': 'Регион'}, inplace=True)

# Вычисление прироста населения за последние 5 лет (2019–2024)
data['Прирост (2019-2024)'] = data[2024] - data[2019]

# Сортировка данных по приросту
data_sorted = data.sort_values('Прирост (2019-2024)', ascending=False)

# Выделение регионов с наибольшим ростом и спадом
leaders = data_sorted.head(5)
losers = data_sorted.tail(5)

# Визуализация прироста населения
plt.figure(figsize=(14, 8))
plt.bar(data_sorted['Регион'], data_sorted['Прирост (2019-2024)'], color='steelblue')
plt.title('Прирост численности населения (2019-2024)', fontsize=16)
plt.xlabel('Регион', fontsize=12)
plt.ylabel('Прирост населения', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Вывод регионов с наибольшим приростом и спадом
print("Регионы с наибольшим приростом населения за 2019–2024 годы:")
print(leaders[['Регион', 'Прирост (2019-2024)']])

print("\nРегионы с наибольшим спадом населения за 2019–2024 годы:")
print(losers[['Регион', 'Прирост (2019-2024)']])

# Построение графиков для лидеров и аутсайдеров
fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Лидеры
axes[0].bar(leaders['Регион'], leaders['Прирост (2019-2024)'], color='green')
axes[0].set_title('Топ-5 регионов с наибольшим приростом населения', fontsize=14)
axes[0].set_ylabel('Прирост населения', fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Аутсайдеры
axes[1].bar(losers['Регион'], losers['Прирост (2019-2024)'], color='red')
axes[1].set_title('Топ-5 регионов с наибольшим спадом населения', fontsize=14)
axes[1].set_xlabel('Регион', fontsize=12)
axes[1].set_ylabel('Прирост населения', fontsize=12)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
