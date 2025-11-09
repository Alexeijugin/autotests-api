import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.json())


data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью



headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())  # Заголовки включены в ответ
print(response.url)




try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")




client = httpx.Client(headers={"Auth": "secret-code"})

