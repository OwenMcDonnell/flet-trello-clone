import textwrap
import flet
from flet import (
    DragTarget,
    Draggable,
    Container,
    Checkbox,
    Column,
    Row,
    UserControl,
    Card,
    icons,
    border_radius,
    border,
    alignment,
    colors,
    padding,
)
#from main import app


class Item(UserControl):
    def __init__(self, list, item_text: str):
        super().__init__()
        self.list = list
        self.item_text = item_text
        self.card_item = Card(
            content=Row(
                [Container(
                    content=Checkbox(label=f"{self.item_text}", width=200),
                    border_radius=border_radius.all(5))],
                width=200,
                wrap=True
            ),
            elevation=1,
            data=self.list
        )

    def build(self):
        return self.card_item
