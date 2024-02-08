from textual.app import App, ComposeResult
from textual.widgets import Static

DISPLAY_MAP = "    *  X  *   "

class GameApp(App):
    """Wonderworld game interface."""

    CSS_PATH = "interface.tcss"

    def compose(self) -> ComposeResult:
        mapscreen = Static(id="map")
        mapscreen.border_title = "Map"
        paramscreen = Static(id="params")
        paramscreen.border_title = "Parameters"
        yield mapscreen
        yield paramscreen

    def on_key(self, event):
        if event.key == "q":
            self.exit()

if __name__ == "__main__":
    app = GameApp()
    app.run()
