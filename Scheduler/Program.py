from DataBase import DataBase
from TaskLow import TaskLow
from TaskMiddle import TaskMiddle
from TaskHigh import TaskHigh


db = DataBase()
id = 0

cycle = True
while (cycle):
    print(".....................")
    print("\t1 - Показать текущие задания")
    print("\t2 - Добавить задание с низким приоритетом")
    print("\t3 - Добавить задание с средним приоритетом")
    print("\t4 - Добавить задание с высоким приоритетом")
    print("\t5 - Выйти из программы")
    print(".....................")
    print("Выберите действие: ")
    selection = int(input())
    match (selection):
        case 1:
            db.show_data()
        case 2:
            tl = TaskLow(id)
            DataBase.add_task(db.low, tl)
            print(tl)
            id += 1
        case 3:
            tm = TaskMiddle(id)
            DataBase.add_task(db.middle, tm)

            id += 1
        case 4:
            th = TaskHigh(id)
            DataBase.add_task(db.high, th)
            id += 1
        case 5:
            cycle = False
