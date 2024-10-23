import socket


def calculate_expression(expression):
    expression = expression.replace('F', '0xF').replace('E', '0xE').replace('D', '0xD').replace('C', '0xC').replace('B', '0xB').replace('A', '0xA')
    try:
        result = eval(expression)
        if hex(result)[0] == "-":
            return "-" + hex(result).upper()[3:]
        return hex(result).upper()[2:]
    except Exception as e:
        return f"Ошибка: {e}"


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Сервер запущен на {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключен клиент на {addr}")
        data = client_socket.recv(1024).decode()
        print(f"Получено выражение: {data}")
        result = calculate_expression(data)
        client_socket.send(result.encode())
        client_socket.close()


if __name__ == "__main__":
    start_server("localhost", 12345)
