import flet
from flet import (
    Column,
    Row,
    Container,
    Icon,
    Page,
    Text,
    TextField,
    AlertDialog,
    ElevatedButton,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
    theme,
)
from board import Board
from app_layout import AppLayout
from data_store import DataStore
from memory_store import store


class TrelloApp:
    def __init__(self, page: Page):
        self.store: DataStore = store
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("Trolli", font_family="Pacifico",
                       size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.layout = AppLayout(
            self, self.page, tight=True, expand=True, vertical_alignment="start")

    def initialize(self):
        self.page.add(self.layout)
        self.page.update()

    def add_board(self, e):
        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Cancel") or type(e.control) is TextField:
                self.create_new_board(dialog_text.value)
            dialog.open = False
            self.page.update()
        dialog_text = TextField(label="New Board Name", on_submit=close_dlg)
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column([
                dialog_text,
                Row([
                    ElevatedButton(
                        text="Cancel", on_click=close_dlg),
                    ElevatedButton(
                        text="Create", bgcolor=colors.BLUE_200, on_click=close_dlg)
                ], alignment="spaceBetween")
            ], tight=True),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def create_new_board(self, board_name):
        new_board = Board(self, board_name)
        self.store.add_board(new_board)
        self.current_board = new_board
        self.layout.active_view = new_board
        self.layout.hydrate_all_boards_view()

    def delete_board(self, e):
        self.store.remove_board(e.control.data)
        self.layout.set_all_boards_view()


if __name__ == "__main__":

    def main(page: Page):

        page.title = "Flet Trello clone"
        page.padding = 0
        page.theme = theme.Theme(
            font_family="Verdana")
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {
            "Pacifico": "/Pacifico-Regular.ttf"
        }
        page.bgcolor = colors.BLUE_GREY_200
        page.update()
        app = TrelloApp(page)
        app.initialize()

    flet.app(target=main, assets_dir="../assets", view=flet.WEB_BROWSER)
