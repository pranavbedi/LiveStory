from reflex.components.component import Component
import reflex as rx
from typing import List

class InteractableCharacter(Component):
    library = "/public/CharacterComponent"
    tag = "CharacterComponent"
    is_default = True
    lib_dependencies: List[str] = ["lottie-react", "lottie-web", "@vapi-ai/web"]

    # Arguments
    vapiKey: rx.Var[str]
    storyID: rx.Var[str]
    page: rx.Var[int]
    character: rx.Var[str]
    is_talking: rx.Var[bool]
    on_talking_start: rx.EventHandler
    on_talking_end: rx.EventHandler

interactable_character = InteractableCharacter.create