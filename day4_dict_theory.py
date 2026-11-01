user = {"name": "Felix", "age": 25, "skills": ["Python", "Git"]}

user["city"] = "Minsk"            # добавить новый ключ
user["age"] = 26                   # обновить существующий
del user["city"]                   # удалить ключ
user.get("email")                  # None (безопасно, если ключа нет)
print(user.get("email", "not defined"))     # "не указан" — значение по умолчанию
"name" in user                     # True — проверка ключа

for key in user:                   # ключи
    print(key)
print()
for value in user.values():        # значения
    print(value)
print()
for key, value in user.items():    # пары ключ-значение
    print(f"{key}: {value}")