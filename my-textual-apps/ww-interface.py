#!/usr/bin/env python3

from textual.app import App
from textual.scene import Scene
from textual.widgets import Frame, Label

class MyScene(Scene):
    async def on_mount(self):
        await super().on_mount()
        self.add_widget(Frame(bg="white", rounded=10, border_width=5, border_color="black", width="75%", height="75%", center=True))
        self.add_widget(Label("My Window", font_size=14, x=20, y=20))

if __name__ == "__main__":
    app = App(scenes=[MyScene])
    app.run()
