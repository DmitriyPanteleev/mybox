from textual.app import App, ComposeResult
from textual.widgets import Static


class CenterApp(App):
    """How to center things."""

    CSS = """
    Screen {
        align: center top;
    }

    #map {
        border: round white;
        text-align: center;
        content-align: center middle;
        width: 100%;
        height: 70%;
    }

    #params {
        border: round white;
        text-align: center;
        content-align: center middle;
        width: 100%;
        height: 30%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Hero!", id="map")
        yield Static("Parameters", id="params")

if __name__ == "__main__":
    app = CenterApp()
    app.run()
