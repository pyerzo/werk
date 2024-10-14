from typing import List
import reflex as rx


class State(rx.State):
    data: List = [
        ["Lionel", "Messi", "PSG"],
        ["Christiano", "Ronaldo", "Al-Nasir"],
    ]
    columns: List[str] = ["First Name", "Last Name"]


@rx.page(route="tasks", title="Werk - Tasks")
def tasks() -> rx.Component:
    return rx.container(
        rx.data_table(
            data=State.data,
            columns=State.columns,
        )
    )
