from Task import Task


class TaskMiddle(Task):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.priority = "Middle"

    def __str__(self) -> str:
        return super().__str__() + " Приоритет: " + self.priority