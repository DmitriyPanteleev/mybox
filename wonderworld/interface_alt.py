from textual.app import App, ComposeResult
from textual.widgets import Static

DISPLAY_MAP = "    *  X  *   "
DISPLAY_PARAMS = "Health: 100\nMana: 100\nStamina: 100"

class GameApp(App):
    """Wonderworld game interface."""

    def __init__(self):
        super().__init__()
        self.title = "Wonderworld"
        self.hero_coord_x = 0
        self.hero_coord_y = 0

    def compose(self) -> ComposeResult:
        self.widget1 = Static(DISPLAY_MAP)
        yield self.widget1
        self.widget2 = Static(DISPLAY_PARAMS)
        yield self.widget2

    def on_mount(self) -> None:
        self.widget1.styles.background = "black"
        self.widget2.styles.background = "black"
        self.widget1.styles.height = "2fr"
        self.widget2.styles.height = "1fr"
        self.widget1.styles.border = ("round", "yellow")
        self.widget2.styles.border = ("round", "green")
        self.widget1.border_title = "Map"
        self.widget2.border_title = "Parameters"
        self.widget1.styles.border_title_align = "left"
        self.widget2.styles.border_title_align = "right"

    def on_key(self, event):
        if event.key == "q":
            self.exit()

if __name__ == "__main__":
    app = GameApp()
    app.run()
