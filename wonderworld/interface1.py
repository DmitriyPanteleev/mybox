from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input

class Map(Widget):
    """Generates a greeting."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_title = "Map"

    map_string = "press key"
    map = reactive(map_string)

    def step_left(self):
        self.map_string = "a pressed"
        self.map = self.map_string

    def step_right(self):
        self.map_string = "d pressed"
        self.map = self.map_string

    def step_up(self):
        self.map_string = "w pressed"
        self.map = self.map_string
    
    def step_down(self):
        self.map_string = "s pressed"
        self.map = self.map_string

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
            self.query_one(Map).step_left()
        if event.key == "d":
            self.query_one(Map).step_right()
        if event.key == "q":
            self.exit()

if __name__ == "__main__":
    app = GameApp()
    app.run()
