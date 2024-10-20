import reflex as rx
from reflex.state import State
from ..characterComponent import InteractableCharacter
from ..getPages import get_page
from typing import List, Union

from dotenv import load_dotenv
import os

load_dotenv()
VAPI_KEY = os.getenv("VAPI_KEY")
if VAPI_KEY is None:
    raise ValueError("VAPI_KEY environment variable is not set")

class StoryState(rx.State):
    current_page: int = 1
    story_content: str = "Once upon a time, there is three little pigs and a big bad wolf."
    background_image: str = "../backgrounds/1.jpg"
    background_opacity: float = 0.5
    clicked_character: str = ""
    

    page_data: List[List[List[Union[str, int]]]] = [
        [["wolf"], [0, 0], [0, 0]],  # dummy data, since current_page starts at 1
        [["first-pig", "second-pig", "third-pig"], [300, 300, 300], [200, 450, 700]],
        [["first-pig"], [300], [300]],
        [["second-pig"], [260], [240]],
        [["third-pig"], [300], [300]],
        [["wolf"], [300], [300]],
        [["wolf"], [150], [600]],
        [["wolf"], [150], [600]],
        [["wolf"], [300], [100]],
        [["first-pig"], [300], [400]],
        [["wolf"], [250], [50]],
        [["first-pig", "second-pig"], [300, 300], [400, 550]],
        [["wolf"], [300], [300]],
        [["wolf"], [80], [500]],
        [["third-pig"], [320], [350]],
        [["first-pig", "second-pig", "third-pig", "wolf"], [320, 310, 300, 350], [200, 300, 400, 600]]
    ]

    character_positions: List[str] = page_data[current_page][0]
    tops: List[int] = page_data[current_page][1]
    lefts: List[int] = page_data[current_page][2]

    async def set_page_content(self):
        page_data = await get_page(self.current_page)
        self.story_content = page_data["story"]

        self.character_positions = self.page_data[self.current_page][0]
        self.tops = self.page_data[self.current_page][1]
        self.lefts = self.page_data[self.current_page][2]
        self.clicked_character = ""

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
    
    def character_clicked(self, char_id):
        if self.clicked_character == char_id:
            self.clicked_character = ""
        else:
            self.clicked_character = char_id

def moveableCharacter(charID, top, left):
    is_clicked = StoryState.clicked_character == charID
    return rx.box(
        InteractableCharacter(
            passedVapiKey=VAPI_KEY,
            storyID="threeLittlePigs",
            page=StoryState.current_page,
            character=charID
        ),
        position="absolute",
        top=f"{top}px",
        left=f"{left}px",
        z_index=rx.cond(
            is_clicked,
            "20",
            "10",
        ),
        on_click=lambda: StoryState.character_clicked(charID),
        filter=rx.cond((StoryState.clicked_character != "") & (StoryState.clicked_character != charID), "blur(10px)", "none"),
        transform=rx.cond(is_clicked, "scale(2)", "scale(1)"),
        transition="transform 0.75s ease-in-out",
    )

def story():
    is_blurred = StoryState.clicked_character != ""
    return rx.container(
        rx.foreach(
            StoryState.character_positions,
            lambda character, index: moveableCharacter(character, StoryState.tops[index], StoryState.lefts[index])
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
                filter=rx.cond(is_blurred, "blur(10px)", "none"),
            )
        )
    )
