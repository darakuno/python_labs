class Student:
    number_zatch = None
    surname = None
    name = None
    patronymic = None
    gender = None
    birthday_date = None
    phone_number = None
    address = None
    group = None

    def to_dict(self):
        return {
            'number_zatch': self.number_zatch,
            'surname': self.surname,
            'name': self.name,
            'patronymic': self.patronymic,
            'gender': self.gender,
            'birthday_date': self.birthday_date,
            'phone_number': self.phone_number,
            'address': self.address,
            'group': self.group
        }

    def __init__(self, number_zatch, surname, name, patronymic, gender, birthday_date, phone_number, address, group):
        self.number_zatch = number_zatch
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.gender = gender
        self.birthday_date = birthday_date
        self.phone_number = phone_number
        self.address = address
        self.group = group

    def __str__(self):
        return (f"Номер зачетки: {self.number_zatch}\n"
                f"Фамилия: {self.surname}\n"
                f"Имя: {self.name}\n"
                f"Отчество: {self.patronymic}\n"
                f"Пол: {self.gender}\n"
                f"Дата рождения: {self.birthday_date}\n"
                f"Телефон: {self.phone_number}\n"
                f"Адрес: {self.address}\n"
                f"Группа: {self.group}\n")

    def __del__(self):
        print(f"Удален студент с номером зачетки {self.name}")


def add_student(students_list):
    number_zatch = input(f"Введите номер зачетки: ")
    surname = input(f"Введите фамилию: ")
    name = input(f"Введите имя: ")
    patronymic = input(f"Введите отчество: ")
    gender = input(f"Введите пол: ")
    birthday_date = input(f"Введите дату рождения: ")
    phone_number = input(f"Введите телефон: ")
    address = input(f"Введите адрес: ")
    group = input(f"Введите группу: ")

    new_student = Student(number_zatch, surname, name, patronymic, gender, birthday_date, phone_number, address, group)
    students_list.append(new_student)
    print("Студент добавлен :)")


def show_students(students_list):
    if students_list:
        for i in range(0, len(students_list)):
            print("=" * 10 + f" студент №{i} " + "=" * 10)
            print(students_list[i])
    else:
        print(f"Список пуст")


def del_student(students_list):
    try:
        position = int(input("Введите позицию удаляемого студента в списке: "))
        students_list.pop(position)
    except IndexError:
        print("Ошибка: элемент не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


def find_student_by_group(students_list):
    group = input("Введите группу, студентов которой необходимо найти: ")
    flag_found = False
    for i in range(0, len(students_list)):
        if students_list[i].group == group:
            flag_found = True
            print("=" * 10 + f" студент №{i} " + "=" * 10 + f" в группе {group}")
            print(students_list[i])
    if not flag_found:
        print(f"Студентов в группе {group} не найдено")


def main():
    students_list = []

    while True:
        char = input(f"1 - добавить студента,\n"
                     f"2 - удалить информацию о студенте,\n"
                     f"3 - отобразить всех студентов,\n"
                     f"4 - поиск студентов по группе, \n"
                     f"5 - выйти из программы\n")
        if char == '1':
            add_student(students_list)
        elif char == '2':
            del_student(students_list)
        elif char == '3':
            show_students(students_list)
        elif char == '4':
            find_student_by_group(students_list)
        elif char == '5':
            return 0


if __name__ == "__main__":
    main()




