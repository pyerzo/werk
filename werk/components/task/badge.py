import reflex as rx


def task_badge(task) -> rx.Component:
    return rx.box(
        rx.match(
            task["status"],
            ("done", rx.badge("Done", color_scheme="grass")),
            ("pending", rx.badge("Pending", color_scheme="amber")),
            rx.badge("Undefined", color_scheme="gray"),
        )
    )
