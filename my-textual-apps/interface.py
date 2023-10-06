from rich import print
from rich.panel import Panel
from rich.text import Text

# Создаем текст, который хотим поместить в рамку
text = Text("Hello, World!", justify="center")

# Создаем панель (рамку) вокруг текста со скругленными углами
panel = Panel(text, border_style="blue", padding=(1, 2), expand=False)

# Выводим панель в консоль
print(panel)
