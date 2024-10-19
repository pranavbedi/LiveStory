import reflex as rx
from rxconfig import config
from .pages.story_page import story

class State(rx.State):
    """The app state."""
    ...

def index() -> rx.Component:
    # Landing page
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.image(
                src="background.jpg",
                width="1920x",
                height="auto",
            ),
            rx.link(rx.button("Switch to Story"), href="/story"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

app = rx.App()
app.add_page(index)
app.add_page(story, route="/story") 