from sys import argv

script_name, wkd_hours, perh_rate, bonus = argv

wage = int(wkd_hours) * int(perh_rate) + int(bonus)

print(f"Отработанные часы: {wkd_hours}")
print(f"Ставка в час: {perh_rate}")
print(f"Премия: {bonus}")
print(f"Зп: {wage}")
