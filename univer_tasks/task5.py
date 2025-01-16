import numpy as np

# Haroratlar vektori (masalan, tasodifiy qiymatlar)
t = np.random.rand(365) * 30  # 0 dan 30 gacha bo'lgan tasodifiy haroratlar

# Oylik kunlar
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
          "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]

# Oylik o'rtacha haroratlarni hisoblash
monthly_avg_temps = []
start_day = 0

for days in days_in_month:
    month_data = t[start_day:start_day + days]
    monthly_avg_temps.append(np.mean(month_data))
    start_day += days

# Eng katta o'rtacha harorat va uning oyini aniqlash
max_avg_temp = max(monthly_avg_temps)
max_month_index = monthly_avg_temps.index(max_avg_temp)
max_month_name = months[max_month_index]

print(f"Eng katta oylik o'rtacha harorat: {max_avg_temp:.2f} °C, Oyi: {max_month_name}")
