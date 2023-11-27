from textual.app import App
from textual.widget import Widget

class FullWidthWidget(Widget):
    def render(self):
        return self.style(f"{' ' * self.size[0]}", "on blue")

class MyApp(App):
    async def on_mount(self) -> None:
        # Get the dimensions of the screen
        width, height = self.view.dimensions

        # Calculate the height for the widget
        widget_height = int(2/3 * height)

        # Create a widget with the calculated dimensions
        widget = FullWidthWidget(width=width, height=widget_height)

        # Add the widget to the root view
        await self.view.dock(widget)

app = MyApp()  # Create an instance of MyApp
app.run()  # Run the instance, not the class

