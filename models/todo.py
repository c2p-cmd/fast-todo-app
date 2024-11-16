from uuid import uuid4
from pydantic import BaseModel

class TodoItemContent(BaseModel):
    content: str

class ToDoItem(BaseModel):
    id: str
    content: str
    is_completed: bool = False


class ItemManager:
    def __init__(self):
        self.__item_list: list[ToDoItem] = []

    def get_all(self) -> list[ToDoItem]:
        sort_descriptor = lambda e: e.is_completed
        self.__item_list.sort(key=sort_descriptor, reverse=True)
        return self.__item_list

    def add_new(self, item: TodoItemContent):
        new_id = str(uuid4())
        todo_item = ToDoItem(id=new_id, content=item.content)
        self.__item_list.append(todo_item)

    def toggle_status(self, id: str):
        items: list[ToDoItem] = [item for item in self.__item_list if item.id == id]
        if not items:
            raise Exception("Item Not Found")
        if len(items) == 0:
            raise Exception("Item Not Found")

        item = items[0]
        item.is_completed = not item.is_completed

    def remove_item(self, id: str):
        items: list[ToDoItem] = filter(lambda e: e.id == id, self.__item_list)
        if not items:
            raise Exception("Item Not Found")
        if len(items) == 0:
            raise Exception("Item Not Found")
