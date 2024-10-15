from typing import Dict, List
import reflex as rx
from werk.models import TASK_STATUS, Task, TaskStatus
from werk.template import template


class State(rx.State):
    items: List[Task] = [
        Task(
            title="Complete Project Report",
            subtitle="Finalize the details and submit by Friday",
            status="pending",
        ),
        Task(
            title="Data Analysis",
            subtitle="Get data for 2024 sell reports",
            status="done",
        ),
    ]

    @staticmethod
    def status(task: Task):
        return TASK_STATUS.get(task.status) or TaskStatus(
            label="Undefined", color_scheme="gray"
        )


@rx.page(route="tasks", title="Werk - Tasks")
@template
def tasks() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                rx.icon(
                    tag="plus",
                    size=18,
                ),
                "Add",
            ),
            rx.input(
                rx.input.slot(
                    rx.icon(
                        tag="search",
                        size=18,
                    ),
                ),
                placeholder="Search",
                width=270,
                on_blur=rx.console_log("SEARCH"),
            ),
            justify="between",
            width="99%",
        ),
        rx.flex(
            rx.foreach(
                State.items,
                lambda item: rx.card(
                    rx.heading(item.title, size="5"),
                    rx.text(item.subtitle),
                    rx.badge(
                        State.status(item).label,
                        color_scheme=State.status(item).color_scheme,
                    ),
                    width=270,
                    style=rx.Style(
                        {
                            "padding": "1.8em",
                            "paddingTop": "1.1em",
                            "paddingBottom": "1.1em",
                        }
                    ),
                ),
            ),
            rx.foreach(
                list(range(0, 4)),
                lambda _: rx.box(
                    width=270,
                ),
            ),
            spacing="4",
            width="100%",
            flex_wrap="wrap",
            justify="center",
        ),
        spacing="5",
        justify="center",
        align="center",
    )
