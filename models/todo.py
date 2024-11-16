from uuid import uuid4
from pydantic import BaseModel


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

    def add_new(self, content: str):
        new_id = str(uuid4())
        item = ToDoItem(id=new_id, content=content)
        self.__item_list.append(item)

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
