from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input

class Map(Widget):
    """Generates a greeting."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_title = "Map"

    map_string = "              X               "
    map = reactive(map_string, layout=True)

    def step_left(self):
        # Find the index of the X and move it one to the left
        x = self.map_string.index("X")
        if x > 0:
            self.map_string = self.map_string[:x - 1] + "X" + self.map_string[x:]

    def step_right(self):
        # Find the index of the X and move it one to the right
        x = self.map_string.index("X")
        if x < len(self.map_string) - 1:
            self.map_string = self.map_string[:x] + "X" + self.map_string[x + 1:]

    def render(self) -> str:
        return f"{self.map}"

class Parameters(Widget):
    """Generates a greeting."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_title = "Parameters"

    params = reactive("Health: 100\nMana: 100\nStamina: 100", layout=True)

    def render(self) -> str:
        return f"{self.params}"

class GameApp(App):
    CSS_PATH = "interface1.tcss"

    def compose(self) -> ComposeResult:
        yield Map()
        yield Parameters()

    def on_key(self, event) -> None:
        if event.key == "a":
            self.query_one(Map).map_string = "  X     "
        if event.key == "s":
            self.query_one(Map).map_string = "    X   "
        if event.key == "q":
            self.exit()

if __name__ == "__main__":
    app = GameApp()
    app.run()
