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
        border-title-align: left;
        text-align: left;
        content-align: left top;
        width: 100%;
        height: 65%;
    }

    #params {
        border: round white;
        border-title-align: right;
        text-align: center;
        content-align: center middle;
        width: 100%;
        height: 25%;
    }
    """

    def compose(self) -> ComposeResult:
        mapscreen = Static(id="map")
        mapscreen.border_title = "Map"
        paramscreen = Static(id="params")
        paramscreen.border_title = "Parameters"
        yield mapscreen
        yield paramscreen

if __name__ == "__main__":
    app = CenterApp()
    app.run()
