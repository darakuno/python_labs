# Разработать клиент-серверное приложение для вычисления выражений.
# Требования к клиенту:
# - отправка на сервер введенного пользователем выражения (числа в
# шестнадцатеричном представлении, знаки «+» и «-»), например: «F11+E8-8+10»;
# - получение результата вычисления выражения;
# - удобный графический интерфейс.
# Требования к серверу:
# - вычисление полученного от клиента выражения и отправка результата клиенту.

import socket
import tkinter as tk
from tkinter import messagebox


def send_expression():
    expression = entry.get()
    if not expression:
        messagebox.showwarning("Внимание", "Введите выражение.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        client_socket.send(expression.encode())
        result = client_socket.recv(1024).decode()
        messagebox.showinfo("Результат", f"Результаты вычисления: {result}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {e}")
    finally:
        client_socket.close()


host = "localhost"
port = 12345

root = tk.Tk()
root.title("Клиент вычисления выражений")

label = tk.Label(root, text="Введите выражение (шестнадцатеричное):")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

send_button = tk.Button(root, text="Отправить", command=send_expression)
send_button.pack(pady=20)

exit_button = tk.Button(root, text="Выход", command=root.quit)
exit_button.pack(pady=5)

root.mainloop()
