from Task import Task


class TaskLow(Task):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.priority = "Low"

    def __str__(self) -> str:
        return super().__str__() + " Приоритет: " + self.priority