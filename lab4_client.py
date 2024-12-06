import ssl
import socket

def start_client():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations("server_cert.pem")

    with socket.create_connection(('localhost', 65432)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as secure_sock:
            while True:
                message = input("Введіть повідомлення для сервера: ")  # Клієнт вводить текст
                if message.lower() == 'exit':  # Якщо клієнт вводить 'exit', з'єднання закривається
                    break
                secure_sock.send(message.encode('utf-8'))  # Надсилаємо повідомлення серверу
                data = secure_sock.recv(1024)  # Отримуємо відповідь від сервера
                print(f"Отримано від сервера: {data.decode()}")

if __name__ == "__main__":
    start_client()
