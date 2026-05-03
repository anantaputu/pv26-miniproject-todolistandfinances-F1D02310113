from dataclasses import dataclass

@dataclass
class TodoItem:
    title: str
    category: str
    priority: str
    due_date: str
    status: str
    notes: str