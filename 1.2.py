a = int(input("Введите количество секунд: "))
hour = a // 3600
min = (a % 3600) // 60
sec = a % 60
print(f"{hour}:{min}:{sec}")
