from werk.models import TaskStatus


TASK_STATUS = {
    "done": TaskStatus(label="Done", color_scheme="cyan"),
    "pending": TaskStatus(label="Pending", color_scheme="orange"),
}
