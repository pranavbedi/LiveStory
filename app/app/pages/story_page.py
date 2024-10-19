import reflex as rx
from reflex.state import State

class StoryState(rx.State):
    current_page: int = 0
    story_pages = [
        "Once upon a time, in a faraway land...",
        "A brave knight set out on a quest...",
        "He faced many challenges and adventures...",
        "Finally, he found the treasure and returned home.",
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

def story():
    return rx.container(
        # Main background image
        rx.image(
            src="../pigsBackGround.png",
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            object_fit="cover",
            z_index="-1",
        ),
        rx.link(
            rx.button("Back to Lobby"),
            href="/",
            position="fixed",
            top="15px",
            left="15px",
            z_index="10",
        ),
        rx.flex(
            rx.box(
                # Left navigation area (transparent)
                rx.box(
                    position="absolute",
                    left="0",
                    top="0",
                    width="50%",
                    height="100%",
                    on_click=StoryState.previous_page,
                    cursor="pointer",
                    z_index="1",
                ),
                # Right navigation area (transparent)
                rx.box(
                    position="absolute",
                    right="0",
                    top="0",
                    width="50%",
                    height="100%",
                    on_click=StoryState.next_page,
                    cursor="pointer",
                    z_index="1",
                ),
                # Content
                rx.vstack(
                    rx.image(
                        src="../wolf.png",
                        width="auto",
                        height="30vh",
                        z_index="2",
                        object_fit="contain",
                    ),
                    rx.box(
                        StoryState.story_pages[StoryState.current_page],
                        background_color="white",
                        padding="10px",
                        font_size="2.5vh",
                        font_family="serif",
                        text_align="center",
                        z_index="2",
                        height="30vh",
                        overflow="hidden",
                    ),
                    width="100%",
                    height="100%",
                    justify="center",
                    align_items="center",
                    spacing="2vh",
                    z_index="2",
                ),
                width="90%",
                height="90",
                background_color="white",
                border="2px solid green",
                overflow="hidden",
                position="relative",
            ),
            width="100vw",
            height="100vh",
            justify="center",
            align_items="center",
        ),
    )