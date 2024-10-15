from typing import Literal
import reflex as rx
from pydantic import BaseModel


class TaskStatus(rx.Base):
    label: str
    color_scheme: Literal["cyan", "orange", "gray"]


class Task(rx.Base):
    title: str
    subtitle: str
    status: Literal["pending", "done"]


TASK_STATUS = {
    "done": TaskStatus(label="Done", color_scheme="cyan"),
    "pending": TaskStatus(label="Pending", color_scheme="orange"),
}
