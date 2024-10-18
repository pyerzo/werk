import reflex as rx


def task_add_dialog(button: rx.Component) -> rx.Component:
    return rx.box(
        rx.dialog(
            rx.dialog.trigger(button),
            rx.dialog.content(
                rx.dialog.title("Add Task"),
                rx.dialog.description(
                    "Describe a to do task", size="2", margin_bottom="16px"
                ),
                rx.form(
                    rx.flex(
                        rx.text(
                            "Title",
                            as_="div",
                            size="2",
                            margin_bottom="4px",
                            weight="bold",
                            required=True,
                        ),
                        rx.input(
                            placeholder="Enter title",
                        ),
                        rx.text(
                            "Description",
                            as_="div",
                            size="2",
                            margin_bottom="4px",
                            weight="bold",
                        ),
                        rx.text_area(
                            placeholder="Enter description",
                            rows="5",
                        ),
                        rx.text(
                            "Due date",
                            as_="div",
                            size="2",
                            margin_bottom="4px",
                            weight="bold",
                        ),
                        rx.input(
                            type="date",
                            placeholder="Enter due date",
                            height="50px",
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                color_scheme="gray",
                                variant="soft",
                            ),
                        ),
                        rx.dialog.close(
                            rx.button("Save"),
                        ),
                        spacing="3",
                        margin_top="16px",
                        justify="end",
                    ),
                ),
            ),
        )
    )
