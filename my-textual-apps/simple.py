from textual.app import App, ComposeResult
from textual.widgets import Static


TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain."""


class BoxSizing(App):
    def compose(self) -> ComposeResult:
        self.widget1 = Static(TEXT)
        yield self.widget1
        self.widget2 = Static(TEXT)
        yield self.widget2

    def on_mount(self) -> None:
        self.widget1.styles.background = "purple"
        self.widget2.styles.background = "darkgreen"
        self.widget1.styles.height = "50%"
        self.widget2.styles.height = "30%"
        self.widget1.styles.border = ("round", "white")
        self.widget2.styles.border = ("round", "white")
        self.widget1.border_title = "Map"
        self.widget2.border_title = "Information"
        self.widget1.styles.border_title_align = "center"
        self.widget2.styles.border_title_align = "left"

if __name__ == "__main__":
    app = BoxSizing()
    app.run()
