import reflex as rx
from reflex.state import State
from ..characterComponent import InteractableCharacter
from ..getPages import get_page

class StoryState(rx.State):
    current_page: int = 1
    story_content: str = ""
    background_image: str = "../backgrounds/1.jpg"
    background_opacity: float = 0.5

    async def set_page_content(self):
        page_data = await get_page(self.current_page)
        self.story_content = page_data["story"]
        self.background_image = f"/backgrounds/{self.current_page}.jpg"

    async def next_page(self):
        if self.current_page < 15:  # 15 pages total
            self.current_page += 1
            await self.set_page_content()

    async def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            await self.set_page_content()

    def is_last_page(self) -> bool:
        return self.current_page >= 15  # 15 pages total

    def is_first_page(self) -> bool:
        return self.current_page == 1

    @rx.var
    def progress(self) -> int:
        return int((self.current_page / 15) * 100)

def story():
    return rx.container(
        rx.hstack(
            rx.box(
                InteractableCharacter(
                    storyID="threeLittlePigs",
                    page=StoryState.current_page,
                    character="third-pig"

                ),
                
            ),
            rx.box(
                InteractableCharacter(
                    storyID="threeLittlePigs",
                    page=StoryState.current_page,
                    character="third-pig"

                ),
                
            ),
            rx.box(
                InteractableCharacter(
                    storyID="threeLittlePigs",
                    page=StoryState.current_page,
                    character="third-pig"

                ),
                
            ),
            on_mount=StoryState.set_page_content,
            position="absolute",
            z_index="4",
            top="45%",
            left="25%",
            transform="translateX(-50%)",
            width="30vw",
            height="auto"
        ),
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
                background_color=f"rgba(255, 255, 255, {StoryState.background_opacity})",
            ),
            position="fixed",
            top="0",
            left="0",
            width="100vw",
            height="100vh",
            z_index="-1",
        ),
        rx.link(
            rx.button("Back to Lobby", font_weight="bold", font_size="1em", font_family="Comic Sans MS"),
            href="/",
            position="fixed",
            top="30px",
            left="20px",
            height="10px",
            z_index="10",
            color_scheme="brown",
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
                        src=StoryState.background_image,
                        width="95%",
                        height="auto",
                        margin_top="20px",
                        object_fit="contain",
                        border_radius="1.5em",
                    ),
                    rx.vstack(
                        rx.progress(value=StoryState.progress, width="100%", color_scheme="brown"),
                        width="95%",
                    ),
                    rx.text(
                        StoryState.story_content,
                        font_size="3.5vh",
                        font_family="serrif",
                        text_align="center",
                        color="black",
                        background_color="rgba(255, 255, 255, 0.7)",
                        padding="25px",
                    ),
                    direction="column",
                    align="center",
                    justify="space-between",
                    width="100%",
                    height="100%",
                ),
                width="85vw",
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
