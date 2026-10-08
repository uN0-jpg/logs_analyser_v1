### Открываем файл лога
file = open("logs.txt", "w")
file.close()
file = open("logs.txt", "r")


### Задаем списки
rows_original = file.readlines()
rows_new = []
rows_counter = {}
ips = []
ips_counter = {}
methods = []
methods_counter = {}
paths = []
paths_counter = {}
statuses = []
statuses_counter = {}
i = ""


### Функция для отладки
def show_both_rows():
    print()
    for row in rows_new:
        print(row)

    print()
    print("*" * 20)
    print()

    for row in rows_original:
        print(row)

    print()


def translation(a, b, c):
    for a in b:
        if a not in c:
            c[a] = 0
        c[a] += 1


### Формируем содержимое списков
for string in rows_original:
    rows_new.append(string.split())

for value in rows_new:
    ips.append(value[0])
    methods.append(value[1])
    paths.append(value[2])
    statuses.append(value[3])


### Считаем содержимое списков (Через словари, думаю, будет лучше всего)

for ip in ips:
    if ip not in ips_counter:
        ips_counter[ip] = 0
    ips_counter[ip] += 1
# Не хочу грузить весь код этой фигней, мб сделать для этих нужд отдельную функцию.
translation(i, methods, methods_counter)
translation(i, paths, paths_counter)
translation(i, statuses, statuses_counter)
# Получилось, лол

### Вывод на экран
# Название
print("\nANALYSER-1", end="\n\n")
# IP
print("IPs", f"total: {sum(ips_counter.values())}", sep="\n")
print()
counter = 1
print(f"{"№":<3} | {"ip":<15} | {"count":<100}")
print(f"{("-" * 3):<3} | {("-" * 15):<15} | {("-" *15):<100}")
for name, value in ips_counter.items():
    print(f"{counter:<3} | {name:<15} | {value:<100}")
    counter += 1
print("\n", f"{"***":^15}", end="\n\n")

# METHODS
print("Methods", f"total: {sum(methods_counter.values())}", sep="\n")
counter = 1
print(f"{"№":<3} | {"method":<15} | {"count":<100}")
print(f"{("-" * 3):<3} | {("-" * 15):<15} | {("-" * 15):<100}")
for name, value in methods_counter.items():
    print(f"{counter:<3} | {name:<15} | {value:<100}")
    counter += 1
print("\n", f"{"***":^15}", end="\n\n")

# PATHS
print("Paths", f"total: {sum(paths_counter.values())}", sep="\n"),
counter = 1
print(f"{"№":<3} | {"path":<15} | {"count":<100}")
print(f"{("-" * 3):<3} | {("-" * 15):<15} | {("-" * 15):<100}")
for name, value in paths_counter.items():
    print(f"{counter:<3} | {name:<15} | {value:<100}")
    counter += 1
print("\n", f"{"***":^15}", end="\n\n")

print("Statuses", f"total: {sum(statuses_counter.values())}", sep="\n")
counter = 1
print(f"{"№":<3} | {"status":<15} | {"count":<100}")
print(f"{("-" * 3):<3} | {("-" * 15):<15} | {("-" * 15):<100}")
for name, value in statuses_counter.items():
    print(f"{counter:<3} | {name:<15} | {value:<100}")
    counter += 1
print("\n", f"{"*end*":^15}", end="\n\n")

### Закрываем файл
file.close()
