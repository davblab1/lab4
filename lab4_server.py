import ssl
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))  # Вказати порт і хост
    server_socket.listen(5)

    # Завантажуємо серверний сертифікат і ключ для шифрування
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server_cert.pem", keyfile="server_key.pem")

    print("Сервер чекає на з'єднання...")
    while True:
        client_socket, addr = server_socket.accept()
        with context.wrap_socket(client_socket, server_side=True) as secure_socket:
            print(f"Підключення від: {addr}")
            while True:
                data = secure_socket.recv(1024)  # Отримуємо повідомлення від клієнта
                if not data:
                    break  # Якщо немає даних (клієнт закрив з'єднання), виходимо з циклу
                print(f"Отримано від клієнта: {data.decode()}")  # Виводимо отримане повідомлення
                secure_socket.send(f"Ви надіслали: {data.decode()}".encode('utf-8'))  # Відправляємо відповідь
            secure_socket.close()

if __name__ == "__main__":
    start_server()
