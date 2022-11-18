import flet
from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
    theme
)
from app_layout import AppLayout


class TrelloApp:

    def __init__(self, page: Page):
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
        self.page.add(self.layout)
        self.page.update()


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

    flet.app(target=main, assets_dir="assets", view=flet.WEB_BROWSER)
