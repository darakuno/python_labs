import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


def connect_db():
    conn = sqlite3.connect('students.db')
    return conn


def init_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("DROP TABLE IF EXISTS groups")
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                group_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                group_id INTEGER NOT NULL,
                FOREIGN KEY (group_id) REFERENCES groups(group_id)
            )
        ''')
    conn.commit()
    conn.close()


def add_group(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Информация", f"Группа {name} добавлена.")


def display_groups():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM groups')
    groups = cursor.fetchall()
    conn.close()
    return groups


def group_exists(group_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM groups WHERE group_id = ?', (group_id,))
    exists = cursor.fetchone()[0] > 0
    conn.close()
    return exists


def add_student(name, age, group_id):
    if group_id is not None and not group_exists(group_id):
        messagebox.showerror("Ошибка", f"Группа с ID {group_id} не существует. Студент не добавлен.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, group_id) VALUES (?, ?, ?)', (name, age, group_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Информация", "Студент добавлен.")


def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM students WHERE id = ?', (student_id,))
    exists = cursor.fetchone()[0] > 0
    if not exists:
        messagebox.showerror("Ошибка", f"Студент с ID = {student_id} не найден. Удалить невозможно")
        return
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Информация", f"Студент с ID = {student_id} удален.")


def display_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT students.id, students.name, students.age, groups.name FROM students LEFT JOIN groups ON students.group_id = groups.group_id
    ''')
    students = cursor.fetchall()
    conn.close()
    return students


class StudentApp:
    def __init__(self):
        self.tree = None
        self.root = tk.Tk()
        self.root.title("База данных Студенты")
        self.root.geometry("500x300")
        self.init_ui()
        init_tables()

    def init_ui(self):
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Имя', 'Возраст', 'Группа'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Имя', text='Имя')
        self.tree.heading('Возраст', text='Возраст')
        self.tree.heading('Группа', text='Группа')
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.column('ID', width=100)
        self.tree.column('Имя', width=100)
        self.tree.column('Возраст', width=100)
        self.tree.column('Группа', width=100)

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X)

        add_student_btn = tk.Button(button_frame, text="Добавить студента", command=self.add_student)
        add_student_btn.pack(side=tk.LEFT)

        delete_student_btn = tk.Button(button_frame, text="Удалить студента", command=self.delete_student)
        delete_student_btn.pack(side=tk.LEFT)

        add_group_btn = tk.Button(button_frame, text="Добавить группу", command=self.add_group)
        add_group_btn.pack(side=tk.LEFT)

        display_groups_btn = tk.Button(button_frame, text="Отобразить группы", command=self.display_groups)
        display_groups_btn.pack(side=tk.LEFT)


    def add_student(self):
        name = simpledialog.askstring("Имя студента", "Введите имя студента:")
        age = simpledialog.askinteger("Возраст студента", "Введите возраст студента:")
        group_id = simpledialog.askinteger("ID группы", "Введите ID группы:")
        if name and age is not None:
            add_student(name, age, group_id)
            self.display_students()

    def delete_student(self):
        student_id = simpledialog.askinteger("ID студента", "Введите ID студента для удаления:")
        if student_id is not None:
            delete_student(student_id)
            self.display_students()

    def add_group(self):
        group_name = simpledialog.askstring("Название группы", "Введите название группы:")
        if group_name:
            add_group(group_name)

    def display_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        students = display_students()
        for student in students:
            self.tree.insert('', 'end', values=student)

    def display_groups(self):
        groups = display_groups()
        if groups:
            group_names = "\n".join([f"ID: {group[0]} Название группы: {group[1]}" for group in groups])
            messagebox.showinfo("Список групп", group_names)
        else:
            messagebox.showinfo("Список групп", "Список групп пуст")


if __name__ == "__main__":
    app = StudentApp()
    app.root.mainloop()
