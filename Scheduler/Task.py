from datetime import datetime

class Task:
    def __init__(self, id) -> None:
        self.id = id

        self.data_time = datetime.now()
        self.creator = Task.set_creator()
        self.text_task = Task.set_text_task()
        self.deadline = Task.set_deadline()

    def set_creator():
        creator = input("Введите ФИО автора задания ")
        return creator

    def set_text_task():
        text_task = input("Введите текст задания ")
        return text_task

    def set_deadline():
        # Вводится время дедлайна (до которого задание действительно)
        print("Введите срок до которого задание действительно (месяц, число, год, час, минуты и секунды)")
        str = input("В формате mm/dd/yy hh:mm:ss --> ")
        temp = datetime.strptime(str, "%x %X")
        return temp

    def check_deadline(task):
        # Проверка времени дедлайна с текущим временем
        current_time = datetime.now()
        if (current_time > task.deadline):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"id: {self.id} Дата и время: {self.data_time} Автор задания: {self.creator} Текст задания: {self.text_task} Задание действительно до: {self.deadline}"