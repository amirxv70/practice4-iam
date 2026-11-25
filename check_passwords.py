"""ПР. Задание 2: проверка 1000 сгенерированных паролей по политике варианта."""

from iam import check_password, generate_password
from store import load_json

policy = load_json("config.json")["password_policy"]
passwords = [generate_password(policy) for _ in range(1000)]
bad = [p for p in passwords if check_password(p, "x.test", policy)]

print(f"Политика варианта: {policy}")
print(f"Пример пароля: {passwords[0]}")
print(f"Паролей с нарушениями: {len(bad)} из {len(passwords)}")
