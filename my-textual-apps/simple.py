from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class LayoutExample(App):
    CSS_PATH = "simple.css"

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(classes="column"):
                yield Static("One")
                yield Static("Two")
            with Vertical(classes="column"):
                yield Static("Three")
                yield Static("Four")

if __name__ == "__main__":
    app = LayoutExample()
    app.run()
