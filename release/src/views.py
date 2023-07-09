import flet as ft

# core
from src.core.router import RoutePath

# page
from src.pages.home import Home
from src.pages.guideline import Guideline
from src.pages.login import Login


def views_handler(page):
    return {
        RoutePath.home: ft.View(
            route=RoutePath.home,
            controls=[
                Home(page)
            ]
        ),
        RoutePath.guideline: ft.View(
            route=RoutePath.guideline,
            controls=[
                Guideline(page)
            ]
        ),
        RoutePath.login: ft.View(
            route=RoutePath.login,
            controls=[
                Login(page)
            ]
        ),
    }
