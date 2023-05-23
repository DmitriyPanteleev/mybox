from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class LayoutExample(App):
    CSS_PATH = "simple.css"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Static("One", classes="box"),
                Static("Two", classes="box"),
                classes="column",
            ),
            Vertical(
                Static("Three"),
                Static("Four"),
                classes="column",
            ),
        )

if __name__ == "__main__":
    app = LayoutExample()
    app.run()
