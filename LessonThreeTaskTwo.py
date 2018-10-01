class Group:
    def __init__(self):
        self.group = []

    def search(self, surname):
        for element in self.group:
            if surname in element:
                print(element)
                return element
            else:
                print("This student is not found")
                return None

    def add(self, *person):
        try:  # Ловим исключение (попытку добавить студента в заполненную группу
            if len(self.group) >= 10:  # Проверяем условие заполненности группы
                # тут изменил условие с ">" на ">=", иначе в группу помещалось 11 человек, что неправильно :-)
                raise AddGroupException("The group is full!")  # Возбуждаем исключение с определённым текстом
            else:
                self.group.append(person)
        except AddGroupException as agerr:  # Перехватываем возбуждённое исключение и присваиваем ему псевдоним
            print(agerr.get_exception_message())  # Выводим на экран то, что выдаёт метод из класса пользовательского
            # исключения после того, как в него уйдёт текст сообщения из 18-ой строки
        return self.group

    def remove(self, surname):
        for i in range(len(self.group)):
            if surname == self.group[i][1]:
                del (self.group[i])
                return self.group[i]
            else:
                print("This student is not found")
                return 0

    def __str__(self):
        temp = ""
        for i in range(len(self.group)):
            for j in range(len(self.group[i])):
                temp += str(self.group[i][j]) + ', '
        return f"Group is: {temp}"


# Создание класса пользовательского исключения
class AddGroupException(ArithmeticError):  # Наследник
    def __init__(self, message):
        super().__init__()
        self.message = message  # Для вывода собственного сообщения при срабатывании исключения

    def get_exception_message(self):  # Метод для этого же самого
        return self.message
