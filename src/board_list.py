import itertools
from flet import (
    UserControl,
    Column,
    Row,
    Text,
    Icon,
    PopupMenuButton,
    PopupMenuItem,
    Container,
    TextButton,
    TextField,
    icons,
    border_radius,
    alignment,
    border,
    colors,
    padding,
)
from item import Item
from data_store import DataStore
from memory_store import store


class BoardList(UserControl):
    id_counter = itertools.count()

    def __init__(self, remove_list, title: str, color: str = ""):
        super().__init__()
        self.store: DataStore = store
        self.board_list_id = next(BoardList.id_counter)
        self.remove_list = remove_list
        self.title = title
        self.color = color
        self.items = Column([], tight=True, spacing=4)

    def build(self):

        self.new_item_field = TextField(
            label="new card name", height=50, bgcolor=colors.WHITE)

        self.edit_field = Row([
            TextField(value=self.title, width=150, height=40,
                      content_padding=padding.only(left=10, bottom=10)),
            TextButton(text="Save", on_click=self.save_title)
        ])
        self.header = Row(
            controls=[
                Text(value=self.title, style="titleMedium",
                     text_align="left", overflow="clip", expand=True),

                Container(
                    PopupMenuButton(
                        items=[
                            PopupMenuItem(
                                content=Text(value="Edit", style="labelMedium",
                                             text_align="center", color=self.color),
                                text="Edit", icon=icons.CREATE_ROUNDED, on_click=self.edit_title),
                            PopupMenuItem(),
                            PopupMenuItem(
                                content=Text(value="Delete", style="labelMedium",
                                             text_align="center", color=self.color),
                                text="Delete", icon=icons.DELETE_ROUNDED, on_click=self.delete_list),
                            PopupMenuItem(),
                            PopupMenuItem(
                                content=Text(value="Move List", style="labelMedium",
                                             text_align="center", color=self.color))
                        ],
                    ),
                    padding=padding.only(right=-10)
                )
            ],
            alignment="spaceBetween"

        )

        self.view = Container(
            content=Column([
                self.header,
                self.new_item_field,
                TextButton(content=Row([Icon(icons.ADD), Text("add card", color=colors.BLACK38)], tight=True),
                           on_click=self.add_item_handler),
                self.items,
            ], spacing=4, tight=True, data=self.title),
            width=250,
            border=border.all(2, colors.BLACK12),
            border_radius=border_radius.all(5),
            bgcolor=self.color if (
                self.color != "") else colors.BACKGROUND,
            padding=padding.only(
                bottom=10, right=10, left=10, top=5)
        )

        return self.view

    def delete_list(self, e):
        self.remove_list(self, e)

    def edit_title(self, e):
        self.header.controls[0] = self.edit_field
        self.header.controls[1].visible = False
        self.update()

    def save_title(self, e):
        self.title = self.edit_field.controls[0].value
        self.header.controls[0] = Text(value=self.title, style="titleMedium",
                                       text_align="left", overflow="clip", expand=True)

        self.header.controls[1].visible = True
        self.update()

    def add_item_handler(self, e):
        if self.new_item_field.value == "":
            return
        self.add_item()

    def add_item(self, item: str = None):
        new_item = Item(self, item) if item else Item(
            self, self.item_name.value)

        self.items.controls.append(new_item)
        self.store.add_item(self.board_list_id, new_item)
        self.item_name.value = ""

        self.view.update()
        self.page.update()

    def remove_item(self, item):
        self.items.controls.remove(item)
        self.view.update()
