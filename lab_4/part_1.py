import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from lab_3.part_1 import Student


def print_students(students_list):
    students_info = ""
    for i in range(0, len(students_list)):
        students_info += "=" * 10 + f" студент №{i} " + "=" * 10 + '\n'
        students_info += "Номер зачетки: " + students_list[i].number_zatch + '\n'
        students_info += "Фамилия: " + students_list[i].surname + '\n'
        students_info += "Имя: " + students_list[i].name + '\n'
        students_info += "Отчество: " + students_list[i].patronymic + '\n'
        students_info += "Пол: " + students_list[i].gender + '\n'
        students_info += "Дата рождения: " + students_list[i].birthday_date + '\n'
        students_info += "Телефон: " + students_list[i].phone_number + '\n'
        students_info += "Адрес: " + students_list[i].address + '\n'
        students_info += "Группа: " + students_list[i].group + '\n'

    messagebox.showinfo("Список студентов", students_info)


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление студентами")

        self.students_list = []

        labels = ["Номер зачетки", "Фамилия", "Имя", "Отчество", "Пол", "Дата рождения", "Телефон", "Адрес", "Группа"]
        self.entries = {}

        for i, label in enumerate(labels):
            if label != "Пол":
                tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
                entry = tk.Entry(root)
                entry.grid(row=i, column=1)
                self.entries[label] = entry
            else:
                tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
                self.gender_var = tk.StringVar()
                tk.Radiobutton(root, text="М", variable=self.gender_var, value="М").grid(row=4, column=1, sticky="nw")
                tk.Radiobutton(root, text="Ж", variable=self.gender_var, value="Ж").grid(row=4, column=1, sticky="ne")

        tk.Button(root, text="Добавить студента", command=self.add_student).grid(row=9, column=0, padx=10, pady=5)
        tk.Button(root, text="Показать студентов", command=self.show_students).grid(row=9, column=1, padx=10, pady=5)
        tk.Button(root, text="Поиск по группе", command=self.search_by_group).grid(row=9, column=2, padx=10, pady=5)
        tk.Button(root, text="Удалить студента", command=self.del_student).grid(row=9, column=3, padx=10, pady=5)

    def add_student(self):
        student_data = {
            'number_zatch': next((entry.get() for label, entry in self.entries.items() if label == 'Номер зачетки'), None),
            'surname': next((entry.get() for label, entry in self.entries.items() if label == 'Фамилия'), None),
            'name': next((entry.get() for label, entry in self.entries.items() if label == 'Имя'), None),
            'patronymic': next((entry.get() for label, entry in self.entries.items() if label == 'Отчество'), None),
            'gender': self.gender_var.get(),
            'birthday_date': next((entry.get() for label, entry in self.entries.items() if label == 'Дата рождения'), None),
            'phone_number': next((entry.get() for label, entry in self.entries.items() if label == 'Телефон'), None),
            'address': next((entry.get() for label, entry in self.entries.items() if label == 'Адрес'), None),
            'group': next((entry.get() for label, entry in self.entries.items() if label == 'Группа'), None)
        }

        new_student = Student(**student_data)
        self.students_list.append(new_student)
        messagebox.showinfo("Успех", "Студент добавлен!")

    def show_students(self):
        if not self.students_list:
            messagebox.showinfo("Информация", "Список студентов пуст.")
            return
        print_students(self.students_list)

    def del_student(self):
        if not self.students_list:
            messagebox.showinfo("Информация", "Список студентов пуст.")
            return
        position = simpledialog.askinteger("Удаление студента", "Введите № cтудента в списке для удаления:")
        if position is None:
            return
        try:
            self.students_list.pop(position)
            messagebox.showinfo("Успех", "Студент удален!")
        except IndexError:
            messagebox.showerror("Ошибка", "Студент не найден.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def search_by_group(self):
        if not self.students_list:
            messagebox.showinfo("Информация", "Список студентов пуст.")
            return
        unique_groups = set(student.group for student in self.students_list)
        search_window = tk.Toplevel(self.root)
        search_window.title("Поиск по группе")

        tk.Label(search_window, text="Выберите группу:").pack(padx=10, pady=10)
        group_combobox = ttk.Combobox(search_window, values=list(unique_groups))
        group_combobox.pack(padx=10, pady=10)

        def on_search():
            group_name = group_combobox.get()
            if not group_name:
                messagebox.showerror("Ошибка", "Выберите группу.")
                return
            found_students = [student for student in self.students_list if student.group == group_name]
            if not found_students:
                messagebox.showinfo("Результаты поиска", f"Студенты в группе '{group_name}' не найдены.")
            else:
                print_students(found_students)

            search_window.destroy()

        tk.Button(search_window, text="Поиск", command=on_search).pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
