import reflex as rx
from rxconfig import config
from .pages.story_page import story
from .getPages import get_page

from .characterComponent import InteractableCharacter

class State(rx.State):
    """The app state."""
    ...


def index() -> rx.Component:
    # Landing page
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.text("Story Book",
            font_size="5vh",
            font_family="Comic Sans MS",
            text_align="center",
            padding="10px"
        ),
        rx.center(
            rx.link(
                rx.image(
                    src="ThreeLittlePigs.png",
                    width="60%",
                    height="auto",
                    margin="auto",
                    border_radius="1.5em",
                ),
                href="/story",
            ),
            width="100%",
        ),
        spacing="5",
        align="center",
        justify="center",
        height="100vh",
    )

app = rx.App()
app.add_page(index)
app.add_page(story, route="/story") 
app.api.add_api_route("/getPages/{pageIndex}", get_page)