import reflex as rx
from werk.template import template
from werk.components.task_badge import task_badge


class State(rx.State):
    tasks: list[dict] = []

    @rx.background
    async def fetch(self):
        async with self:
            # with rx.session() as session:
            #     self.card_data = session.exec(select(model)).all()
            self.tasks = [
                {
                    "title": "Complete Project Report",
                    "subtitle": "Finalize the details and submit by Friday",
                    "status": "pending",
                },
                {
                    "title": "Data Analysis",
                    "subtitle": "Scrap, clean and show data",
                    "status": "done",
                },
            ]


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
                State.tasks,
                lambda item: rx.card(
                    rx.heading(item.title, size="4"),
                    task_badge(item),
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
        on_mount=State.fetch,
    )
