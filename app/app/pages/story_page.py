import reflex as rx
from reflex.state import State

class StoryState(rx.State):
    current_page: int = 0
    story_pages = [
    "Once upon a time, three little pigs built their own houses.",
    "The first pig made a house of straw.",
    "The second pig built his house from sticks.",
    "The third pig used bricks for his house.",
    "One day, a big bad wolf came to the straw house.",
    "“Let me in!” said the wolf.",
    "“Not by the hair on my chinny chin chin!” cried the first pig.",
    "The wolf huffed and puffed and blew the straw house down!",
    "The first pig ran to his brother's stick house.",
    "The wolf followed and blew the stick house down too!",
    "The two pigs ran to their brother's brick house.",
    "The wolf huffed and puffed, but he couldn’t blow the brick house down!",
    "Angry, the wolf tried to sneak down the chimney.",
    "But the third pig had a pot of hot stew boiling.",
    "The wolf fell in and ran away, never to return.",
    "The three pigs lived happily ever after."
    ]


    def next_page(self):
        if self.current_page < len(self.story_pages) - 1:
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1

    def is_last_page(self) -> bool:
        return self.current_page >= len(self.story_pages) - 1

    def is_first_page(self) -> bool:
        return self.current_page == 0

    @rx.var
    def progress(self) -> int:
        return int((self.current_page / (len(self.story_pages) - 1)) * 100)

def story():
    return rx.container(
        rx.box(
            rx.image(
                src="../pigsBackGround.png",
                width="100%",
                height="100%",
                object_fit="cover",
            ),
            rx.box(
                position="absolute",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background_color="rgba(255, 255, 255, 0.5)",  # Adjust the opacity as needed
            ),
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="-1",
        ),
        rx.link(
            rx.button("Back to Lobby"),
            href="/",
            position="fixed",
            top="30px",
            left="15px",
            height="10px",
            z_index="10",
            color_scheme="brown",
        ),
        rx.image(
            src="../wolf.png",
            width="auto",
            height="10vh",  # Adjust this value as needed
            position="absolute",
            z_index="1",  # This ensures the wolf appears on top
            align="center",
            transform="translateX(-50%)",
        ),
        rx.flex(
            rx.box(
                position="fixed",
                left="0",
                top="0",
                width="50%",
                height="100%",
                on_click=StoryState.previous_page,
                cursor="pointer",
                z_index="1",
            ),
            rx.box(
                position="fixed",
                right="0",
                top="0",
                width="50%",
                height="100%",
                on_click=StoryState.next_page,
                cursor="pointer",
                z_index="1",
            ),
            rx.box(
                rx.flex(
                    rx.image(
                        src="../threePigs.png",
                        width="90%",
                        height="auto",
                        margin_top="20px",
                        object_fit="contain",
                        border_radius="1.5em",
                    ),
                    rx.vstack(
                        rx.progress(value=StoryState.progress, width="100%", color_scheme="brown"),
                        width="90%",
                    ),
                    rx.text(
                        StoryState.story_pages[StoryState.current_page],
                        font_size="2.5vh",
                        font_family="Comic Sans MS",
                        text_align="center",
                        background_color="rgba(255, 255, 255, 0.7)",
                        padding="15px",
                    ),
                    direction="column",
                    align="center",
                    justify="space-between",
                    width="100%",
                    height="100%",
                ),
                width="70vw",
                height="85vh",
                align="center",
                justify="center",
                background_color="white",
                border_radius="20px",
                overflow="hidden",
                position="fixed",
                top="10%",
                left="50%",
                transform="translateX(-50%)",
            )
        )
    )
