import reflex as rx
from rxconfig import config
from werk.template import template


class State(rx.State):

    def login(self):
        return rx.redirect("/tasks")


@rx.page(route="/", title="Werk")
@template
def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Werk", size="8"),
        rx.text(
            "Tasks Queue",
            size="5",
        ),
        rx.input(
            placeholder="Username",
            width="100%",
        ),
        rx.input(
            placeholder="Password",
            type="password",
            width="100%",
        ),
        rx.button(
            "Login",
            on_click=State.login,
            width="100%",
        ),
        justify="center",
    )
