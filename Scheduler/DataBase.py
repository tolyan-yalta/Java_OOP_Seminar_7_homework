from Task import Task

class DataBase():
    def __init__(self) -> None:
        self.low = []
        self.middle = []
        self.high = []
        self.lastId = 0

    def add_task(list, task):
        # Добавление задач в списки
        list.append(task)

    def show_data(db):
        # Вывод в консоль заданий в порядке приоритета с удалением просроченных заданий
        for i in db.high:
            if (Task.check_deadline(i)):
                index = db.high.index(i)
                db.high.pop(index)
            else:
                print(i.__str__())
        for i in db.middle:
            if (Task.check_deadline(i)):
                index = db.middle.index(i)
                db.middle.pop(index)
            else:
                print(i.__str__())
        for i in db.low:
            if (Task.check_deadline(i)):
                index = db.low.index(i)
                db.low.pop(index)
            else:
                print(i.__str__())
