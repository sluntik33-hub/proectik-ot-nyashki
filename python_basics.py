# Практика №12 — базовый Python (примеры для скриншотов)

# 1. Переменные и типы данных
name = "Агент"            # строка (текст)
limit = 10                # число
has_access = True         # логическое значение (да / нет)
tools = ["калькулятор", "поиск по файлам", "планировщик"]   # список
tool_params = {"name": "калькулятор", "input": "числа"}       # словарь

print("Имя:", name)
print("Лимит запросов:", limit)
print("Есть доступ:", has_access)
print("Инструменты:", tools)
print("Параметры инструмента:", tool_params)

# 2. Условие
if has_access:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

# 3. Цикл
for tool in tools:
    print("Доступен инструмент:", tool)

# 4. Функция: получает данные и возвращает результат
def percent(number, p):
    return number * p / 100

print("17% от 125000 =", percent(125000, 17))

# 5. Импорт библиотеки
import math
print("Корень из 16 =", math.sqrt(16))
