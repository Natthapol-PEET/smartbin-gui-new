from flet import *
from src.core.router import RoutePath
from src.views import views_handler


def main(page: Page):
    # page.window_height = 480
    # page.window_width = 800
    # page.window_resizable = False
    # # page.window_full_screen = True
    # page.update()

    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )

    page.on_route_change = route_change
    page.go(RoutePath.home)


if __name__ == '__main__':
    app(target=main)
