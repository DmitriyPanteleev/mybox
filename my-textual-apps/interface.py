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
        text-align: left;
        content-align: left top;
        width: 100%;
        height: 65%;
    }

    #params {
        border: round white;
        text-align: center;
        content-align: center middle;
        width: 100%;
        height: 25%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Map", title="Map", id="map")
        yield Static("Parameters", id="params")

if __name__ == "__main__":
    app = CenterApp()
    app.run()
