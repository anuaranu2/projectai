import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
years = np.arange(2000, 2025).reshape(-1, 1)  # Годы с 2000 по 2024
population = np.array([
    14901641, 14865610, 14851059, 14866837, 14951200, 15074767, 15219291,
    15396878, 15571506, 15982370, 16203274, 16440470, 16673933, 16910246,
    17160855, 17415715, 17669896, 17918214, 18157337, 18395567, 18631779,
    18879552, 19503159, 19766807, 20033842
])
model = LinearRegression()
model.fit(years, population)
# Прогноз на следующие 5 лет (2025–2029)
future_years = np.arange(2025, 2030).reshape(-1, 1)
future_population = model.predict(future_years)
# Полиномиальная регрессия
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(years, population)
future_population_poly = poly_model.predict(future_years)
results = pd.DataFrame({
    "Год": future_years.flatten(),
    "Прогнозируемое население": future_population_poly.astype(int)
})
print(results)
plt.figure(figsize=(10, 6))
plt.plot(years, population, marker='o', label='Исторические данные')
plt.plot(future_years, future_population_poly, marker='x', linestyle='--', label='Прогноз (полиномиальная регрессия)')
plt.title("Прогноз численности населения Казахстана на 2025–2029 годы")
plt.xlabel("Год")
plt.ylabel("Численность населения")
plt.legend()
plt.grid(True)
plt.show()
