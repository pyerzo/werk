from typing import Literal
import reflex as rx
from reflex.components.radix.themes.base import LiteralAccentColor


class TaskStatus(rx.Base):
    label: str
    color_scheme: LiteralAccentColor


class Task(rx.Base):
    title: str
    subtitle: str
    status: str
