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
        self.__item_list.sort(key=sort_descriptor, reverse=False)
        return self.__item_list

    def add_new(self, item: TodoItemContent):
        new_id = str(uuid4())
        todo_item = ToDoItem(id=new_id, content=item.content)
        self.__item_list.append(todo_item)

    def update_status(self, id: str, new_status: bool):
        items: list[ToDoItem] = [item for item in self.__item_list if item.id == id]
        if not items:
            raise Exception(message="Item Not Found")
        if len(items) == 0:
            raise Exception(message="Item Not Found")

        item = items[0]
        item.is_completed = new_status

    def remove_item(self, id: str):
        items: list[ToDoItem] = [item for item in self.__item_list if item.id == id]
        if not items:
            raise Exception(message="Item Not Found")
        if len(items) == 0:
            raise Exception(message="Item Not Found")

        item = items[0]
        self.__item_list.remove(item)
