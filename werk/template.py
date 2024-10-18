from typing import Callable

import reflex as rx


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.container(
            page(),
            height="80vh",
            style=rx.Style({"marginTop": "5vh"}),
        ),
        rx.logo(),
        height="100vh",
        width="100%",
    )
