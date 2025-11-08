import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)

client_socket.connect(server_address)


message = "Как дела?"

client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()

print(response)
# Закрываем соединение
client_socket.close()