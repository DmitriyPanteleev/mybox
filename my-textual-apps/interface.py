#!/bin/python3

from textual.app import App
from textual.widgets import Placeholder

class MyApp(App):
    async def on_mount(self, event):
        await self.view.dock(Placeholder(), edge="top")

MyApp.run(log="textual.log")
