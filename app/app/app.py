import reflex as rx
from rxconfig import config
from .pages.story_page import story
from .getPages import get_page
from .navBar import navbar_searchbar

from .characterComponent import InteractableCharacter

class State(rx.State):

    talking: bool = False

    def start_talking(self):
        self.talking = True

    def stop_talking(self):
        self.talking = False




def index() -> rx.Component:
    # Landing page
    return rx.vstack(
        navbar_searchbar(),
        rx.hstack(
            rx.link(
                rx.image(
                    src="ThreeLittlePigs.jpg",
                    width="auto",
                    height="200px",
                    margin="5px",
                    border = " 3px solid green",
                    border_radius="10px 50px 50px 10px",
                ),
                href="/story",
            ),
            rx.link(  # Place the block before the width argument
                rx.image(
                    src="WeAreAll.png",
                    width="auto",
                    height="200px",
                    border = " 3px solid brown",
                    margin="5px",
                    border_radius="10px 50px 50px 10px",
                ),
                href="/404",
            ),
            rx.link(  # Place the block before the width argument
                rx.image(
                    src="muddle.jpg",
                    width="auto",
                    height="200px",
                    border = " 3px solid purple",
                    margin="5px",
                    border_radius="10px 50px 50px 10px",
                ),
                href="/404",
            ),
            
        ),
        rx.hstack(
            rx.link(
                rx.image(
                    src="caterpillar.png",
                    width="auto",
                    height="200px",
                    margin="5px",
                    border = " 3px solid red",
                    border_radius="10px 50px 50px 10px",
                ),
                href="/404",
            ),
            rx.link(  # Place the block before the width argument
                rx.image(
                    src="ribbit.jpg",
                    width="auto",
                    height="200px",
                    margin="5px",
                    border = " 3px solid green",
                    border_radius="10px 50px 50px 10px",
                ),
                href="/404",
            ),
            rx.link(  # Place the block before the width argument
                rx.image(
                    src="bear.jpeg",
                    width="auto",
                    height="200px",
                    margin="5px",
                    border = " 3px solid yellow",
                    border_radius="10px 50px 50px 10px",
                ),
                href="/404",
            ),
            
        ),
        spacing="5",
        align="center",
        justify="center",
        height="100vh",
        bg="beige",
    )

app = rx.App()
app.add_page(index)
app.add_page(story, route="/story") 
app.api.add_api_route("/getPages/{pageIndex}", get_page)