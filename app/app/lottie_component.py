from reflex.components.component import Component
from typing import List

class LottieExample(Component):
    library = "/public/lottie"
    tag = "CharacterComponent"
    is_default = True
    lib_dependencies: List[str] = ["lottie-react", "lottie-web", "@vapi-ai/web"]

lottie_example = LottieExample.create