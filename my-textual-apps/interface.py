import asyncio
from rich import print
from rich.panel import Panel

def render_box():
    print(Panel("Hello, World!", style="blue on white"))

loop = asyncio.get_event_loop()
loop.run_in_executor(None, render_box)
loop.run_forever()
