# 8. База данных «Студенты».
# Функционал приложения:
# - добавление информации в основную таблица;
# - удалении информации из основной таблицы;
# - отображение информации из основной таблицы.

import sqlite3


def connect_db():
    conn = sqlite3.connect('students.db')
    return conn


def init_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE students")
    cursor.execute("DROP TABLE groups")
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                group_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                group_id INTEGER NOT_NULL,
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
    print(f"Группа {name} добавлена.")


def display_groups():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM groups')
    groups = cursor.fetchall()

    print("Список групп:")
    for group in groups:
        print(f"ID: {group[0]} Название группы: {group[1]}")

    conn.close()


def group_exists(group_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM groups WHERE group_id = ?', (group_id,))
    exists = cursor.fetchone()[0] > 0

    conn.close()
    return exists


def add_student(name, age, group_id):
    if group_id is not None and not group_exists(group_id):
        print(f"Группа с ID {group_id} не существует. Студент не добавлен.")
        return
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, group_id) VALUES (?, ?, ?)', (name, age, group_id))
    conn.commit()
    conn.close()
    print("Студент добавлен.")


def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM students WHERE id = ?', (student_id,))
    exists = cursor.fetchone()[0] > 0
    if not exists:
        print(f"Студент с ID = {student_id} не найден. Удалить невозможно")
        return
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    print(f"Студент с ID = {student_id} удален.")


def display_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT students.id, students.name, students.age, groups.name 
        FROM students LEFT JOIN groups ON students.group_id = groups.group_id
    ''')

    students = cursor.fetchall()

    print("Список студентов:")
    for student in students:
        print(f"ID: {student[0]} Имя: {student[1]} Возраст: {student[2]} Группа: {student[3]}")

    conn.close()


def main():
    init_tables()

    while True:
        print("Меню:")
        print("1. Добавить студента")
        print("2. Удалить студента")
        print("3. Отобразить студентов")
        print("4. Добавить группу")
        print("5. Отобразить группы")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            try:
                name = input("Введите имя студента: ")
                age = int(input("Введите возраст студента: "))
                group_id = int(input("Введите ID группы: "))
                add_student(name, age, group_id)
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            try:
                student_id = int(input("Введите ID студента для удаления: "))
                delete_student(student_id)
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '3':
            display_students()

        elif choice == '4':
            group_name = input("Введите название группы: ")
            add_group(group_name)

        elif choice == '5':
            display_groups()

        elif choice == '6':
            break

        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
