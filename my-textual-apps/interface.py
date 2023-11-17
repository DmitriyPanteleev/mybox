import os
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static

def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

class MyApp(App):
    CSS_PATH = "simple.css"

    def compose(self) -> ComposeResult:
        rows, columns = get_terminal_size()
        yield Container(
            Static("Hello, World!", classes="panel"),
            classes="panel-container",
        )

    def on_mount(self) -> None:
        self.query_one(".panel-container").styles.width = str(get_terminal_size()[1])
        self.query_one(".panel-container").styles.height = str(int(get_terminal_size()[0] * 2/3))

if __name__ == "__main__":
    app = MyApp()
    app.run()