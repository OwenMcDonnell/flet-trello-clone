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


class Board(UserControl):
    id_counter = itertools.count()

    def __init__(self, app, name: str):
        super().__init__()
        self.board_id = next(BoardList.id_counter)
        self.app = app
        self.name = name
        self.add_list_button = FloatingActionButton(
            icon=icons.ADD, text="add a list", height=30, on_click=self.addListDlg)

        self.board_lists = [
            self.add_list_button
        ]

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
        self.update()

    def add_list(self, list: BoardList):
        self.board_lists[-1] = list
