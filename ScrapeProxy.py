import requests
import random

# Генерация случайного прокси
proxy = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}:{random.randint(80, 60000)}"

# Настройка прокси в параметрах запроса
while True:
    proxy = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}:{random.randint(80, 60000)}"
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
        }
    try:
        url = requests.get("https://google.com", proxies=proxies)
        # Дальнейшая обработка ответа от сервера
        print(proxy)
    except requests.exceptions.RequestException as e:
        # Обработка ошибки при отправке запроса
        print(e)
