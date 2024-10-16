from typing import Any
import reflex as rx

from werk.constants import TASK_STATUS
from werk.models import Task, TaskStatus


def task_badge(task) -> rx.Component:
    return rx.box(
        rx.match(
            task["status"],
            ("done", rx.badge("Done", color_scheme="grass")),
            ("pending", rx.badge("Pending", color_scheme="amber")),
            rx.badge("Undefined", color_scheme="gray"),
        )
    )
