from textual.app import App
from textual.widget import Widget
from textual.events import Mount

class CustomWidget(Widget):
    async def on_mount(self) -> None:
        await self.canvas.print("X", x=5, y=5)  # Вы можете выбрать свои координаты

class MyApp(App):
    async def on_mount(self, event: Mount) -> None:
        await self.display(CustomWidget())

app = MyApp()
app.run()
