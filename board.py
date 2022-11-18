import itertools
from flet import (
    UserControl,
    Column,
    Row,
    FloatingActionButton,
    Container,
    Container,
    icons,
    border_radius,
    colors,
    padding,
    alignment,
    margin
)
from board_list import BoardList
from data_store import DataStore
from memory_store import store


class Board(UserControl):
    id_counter = itertools.count()

    def __init__(self, app, name: str):
        super().__init__()
        self.board_id = next(BoardList.id_counter)
        self.store: DataStore = store
        self.app = app
        self.name = name
        self.add_list_button = FloatingActionButton(
            icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)

        self.board_lists = [
            self.add_list_button
        ]
        for l in self.store.get_lists_by_board(self.board_id):
            self.add_list(l)

        self.list_wrap = Row(
            controls=[
                self.board_lists,
                self.add_list_button
            ],
            vertical_alignment="start",
            visible=True,
            scroll="auto",
            width=(self.app.page.width - 310),
            height=(self.app.page.height - 95)
        )

    def build(self):
        self.view = Container(
            content=Column(
                controls=[
                    self.list_wrap
                ],
                scroll="auto",
                expand=True
            ),
            data=self,
            margin=margin.all(0),
            padding=padding.only(top=10, right=0),
            height=self.app.page.height,
        )
        return self.view

    def remove_list(self, list: BoardList, e):
        self.board_lists.remove(list)
        self.store.remove_list(self.board_id, list.board_list_id)
        self.update()

    def add_list(self, list: BoardList):
        self.board_lists.insert(-1, list)
        self.store.add_list(self.board_id, list)
