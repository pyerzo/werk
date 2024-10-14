import reflex as rx

from rxconfig import config
from werk.pages.index import index
from werk.pages.task.index import tasks


app = rx.App()

app.add_page(index)
app.add_page(tasks)
