from typing import Callable

import reflex as rx


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.container(
            page(),
            min_height="85vh",
            style=rx.Style({"marginTop": "5vh"}),
        ),
        rx.logo(),
        width="100%",
    )
