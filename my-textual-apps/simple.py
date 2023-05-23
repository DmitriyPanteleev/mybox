from textual.app import App, ComposeResult
from textual.widgets import Static


class LayoutExample(App):
    CSS_PATH = "simple.css"

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")
        yield Static("Four", classes="box")
        yield Static("Five", classes="box")
        yield Static("Six", classes="box")

if __name__ == "__main__":
    app = LayoutExample()
    app.run()
