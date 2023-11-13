import textual.app
from textual.widget import Widget
from textual.widgets import Static

class MyApp(textual.app.App):

    async def on_load(self) -> None:
        self.bind("b", self.action_view)  # Corrected line

    async def on_mount(self) -> None:
        self.canvas = Static()

    async def action_view(self) -> None:
        width, height = self.screen.size

        self.canvas.update(
            "<roundrect x='0' y='0' height='{height}' width='{width}' rx='20' ry='20' fill='none' stroke='black' stroke-width='2' />".format(
                width=width,
                height=int(height * 2 / 3)
            )
        )

app = MyApp()
app.run()
