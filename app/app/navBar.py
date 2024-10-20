import reflex as rx

def navbar_searchbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logoTextClear.png",
                        width="15em",
                        height="0.01px",
                        border_radius="100%",
                        align="centre",
                    ),
                    rx.image(
                        src="/logoText.png",
                        width="40em",
                        height="auto",
                        border_radius="25%",
                        align="centre",
                    ),
                    justify="center",  # Centers the content horizontall
                ),
            ),
        ),
        bg="beige",
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )