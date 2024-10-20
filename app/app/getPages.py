CHARACTERS = {
    "first_pig": {
        # Return animations
        "animations": {
            "talking": "./lottie-animations/first-pig-talking.json",
            "thinking": "./lottie-animations/first-pig-thinking.json"
        },
        "poses": {}
    }
}

async def get_page(pageIndex: int):
    data = None  # Initialize data to None
    
    if pageIndex == 1:
        data = {
            "story": "Once upon a time, there is three little pigs and a big bad wolf.",
            "context": "",
            "characters": {
                "first_pig": {
                    "poses": ["/pigs/first-running.png"],
                    "messages": {
                        "role": "first little pig",
                        "content": "You only know Once upon a time, there is three little pigs and a big bad wolf. Do not provide answers to any question that can spoil the rest of the story."
                    },
                    "firstMessage": "Hi… I’m the pig 1 who wants to build my house out of straw.",
                    "name": "first little pig"
                },
                "second-pig": {
                    "poses": ["./second-running.png"],
                    "messages": {
                        "role": "second little pig",
                        "content": "You only know Once upon a time, there is three little pigs and a big bad wolf. Do not provide answers to any question that can spoil the rest of the story."
                    },
                    "firstMessage": "Hi… I’m pig 2 who wants to build my house out of sticks.",
                    "pig_voice": "alkdfjeajvneeaohadfjk"
                },
                "third-pig": {
                    "poses": ["/pigs/third-running.png"],
                    "messages": {
                        "role": "third little pig",
                        "content": "You only know Once upon a time, there is three little pigs and a big bad wolf. Do not provide answers to any question that can spoil the rest of the story."
                    },
                    "firstMessage": "Hi… I’m the pig who built my house out of bricks.",
                    "pig_voice": "alkdfjeajvneeaohadfjk"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 2:
        data = {
            "story": "The first pig made a house of straw.",
            "context": "Once upon a time, three little pigs built their own houses.",
            "characters": {
                "first_pig": {
                    "poses": ["/pigs/first-standing.png"],
                    "messages": {
                        "role": "first little pig",
                        "content": "You have built your house out of straw. You’re confident it’s good enough for now. Don’t spoil anything beyond this point in the story."
                    },
                    "firstMessage": "Hi… I’m the pig who built my house out of straw. I hope it will be strong enough!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 3:
        data = {
            "story": "The second pig built his house from sticks.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw.",
            "characters": {
                "second-pig": {
                    "poses": ["/pigs/second-standing.png"],
                    "messages": {
                        "role": "second little pig",
                        "content": "You’ve just finished building your house out of sticks. Don’t mention what happens next!"
                    },
                    "firstMessage": "Hi… I’m the pig who built my house out of sticks. It's definitely stronger than straw!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 4:
        data = {
            "story": "The third pig used bricks for his house.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks.",
            "characters": {
                "third-pig": {
                    "poses": ["/pigs/third-standing.png"],
                    "messages": {
                        "role": "third little pig",
                        "content": "You’ve just finished your brick house. Be sure not to mention what happens next."
                    },
                    "firstMessage": "Hi… I’m the pig who built my house out of bricks. Nothing will bring it down!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 5:
        data = {
            "story": "One day, a big bad wolf came to the straw house.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house.",
            "characters": {
                "wolf": {
                    "poses": ["/wolf/wolf-standing.png"],
                    "messages": {
                        "role": "big bad wolf",
                        "content": "You’ve arrived at the straw house. Don't spoil anything that happens after this moment."
                    },
                    "firstMessage": "Hi… I’m the biggest, baddest wolf. Let me in, little pig!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 6:
        data = {
            "story": "\"Let me in!\" said the wolf.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house.",
            "characters": {
                "wolf": {
                    "poses": ["/wolf/wolf-knocking.png"],
                    "messages": {
                        "role": "big bad wolf",
                        "content": "You’re demanding to be let inside. Don’t talk about what happens after this moment."
                    },
                    "firstMessage": "Let me in! Let me in, little pig, or I'll huff and puff!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 7:
        data = {
            "story": "\"Not by the hair on my chinny chin chin!\" cried the first pig.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf.",
            "characters": {
                "first_pig": {
                    "poses": ["/pigs/first-standing.png"],
                    "messages": {
                        "role": "first little pig",
                        "content": "You’re refusing to let the wolf in. Don’t reveal what happens after this point."
                    },
                    "firstMessage": "Not by the hair on my chinny chin chin! You won't get in!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 8:
        data = {
            "story": "The wolf huffed and puffed and blew the straw house down!",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig.",
            "characters": {
                "wolf": {
                    "poses": ["/wolf/wolf-blowing.png"],
                    "messages": {
                        "role": "big bad wolf",
                        "content": "You’ve blown down the straw house. Don’t mention what happens after this event."
                    },
                    "firstMessage": "Huff! Puff! I blew the house down!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 9:
        data = {
            "story": "The first pig ran to his brother's stick house.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig. The wolf huffed and puffed and blew the straw house down!",
            "characters": {
                "first_pig": {
                    "poses": ["/pigs/first-running.png"],
                    "messages": {
                        "role": "first little pig",
                        "content": "You’re running to your brother's house. Don’t give away what happens next."
                    },
                    "firstMessage": "I need to get to my brother’s house! I hope it’s stronger!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 10:
        data = {
            "story": "The wolf followed them...and blew the stick house down too!",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig. The wolf huffed and puffed and blew the straw house down! The first pig ran to his brother's stick house.",
            "characters": {
                "wolf": {
                    "poses": ["/wolf/wolf-blowing.png"],
                    "messages": {
                        "role": "big bad wolf",
                        "content": "You’ve just blown down the stick house. Don’t spoil what comes after this."
                    },
                    "firstMessage": "Huff! Puff! There goes the stick house too!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 11:
        data = {
            "story": "The two pigs ran to their brother's brick house.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig. The wolf huffed and puffed and blew the straw house down! The first pig ran to his brother's stick house. The wolf followed and blew the stick house down too!",
            "characters": {
                "first_pig": {
                    "poses": ["/pigs/first-running.png"],
                    "messages": {
                        "role": "first little pig",
                        "content": "You’re now running to the brick house for safety. Don’t spoil anything beyond this point."
                    },
                    "firstMessage": "Quick, let’s run to the brick house!"
                },
                "second-pig": {
                    "poses": ["/pigs/second-running.png"],
                    "messages": {
                        "role": "second little pig",
                        "content": "You’re running to the brick house too. No spoilers after this point!"
                    },
                    "firstMessage": "Let’s hope the brick house is strong enough!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 12:
        data = {
            "story": "The wolf huffed and puffed, but he couldn’t blow the brick house down!",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig. The wolf huffed and puffed and blew the straw house down! The first pig ran to his brother's stick house. The wolf followed and blew the stick house down too! The two pigs ran to their brother's brick house.",
            "characters": {
                "wolf": {
                    "poses": ["/wolf/wolf-blowing.png"],
                    "messages": {
                        "role": "big bad wolf",
                        "content": "You’ve just failed to blow the brick house down. Don’t reveal what happens after this!"
                    },
                    "firstMessage": "Huff! Puff! But nothing happens...!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 13:
        data = {
            "story": "Angry, the wolf tried to sneak down the chimney.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig. The wolf huffed and puffed and blew the straw house down! The first pig ran to his brother's stick house. The wolf followed and blew the stick house down too! The two pigs ran to their brother's brick house. The wolf huffed and puffed, but he couldn’t blow the brick house down!",
            "characters": {
                "wolf": {
                    "poses": ["/wolf/wolf-chimney.png"],
                    "messages": {
                        "role": "big bad wolf",
                        "content": "You’re now trying to sneak down the chimney. Don’t reveal what happens next!"
                    },
                    "firstMessage": "I’ll get in through the chimney!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 14:
        data = {
            "story": "But the third pig had a pot of hot stew boiling.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig. The wolf huffed and puffed and blew the straw house down! The first pig ran to his brother's stick house. The wolf followed and blew the stick house down too! The two pigs ran to their brother's brick house. The wolf huffed and puffed, but he couldn’t blow the brick house down! Angry, the wolf tried to sneak down the chimney.",
            "characters": {
                "third-pig": {
                    "poses": ["/pigs/third-standing.png"],
                    "messages": {
                        "role": "third little pig",
                        "content": "You’ve set up a pot of stew to defend against the wolf. No spoilers after this!"
                    },
                    "firstMessage": "The stew is ready, let’s see what happens when the wolf comes down the chimney!"
                }
            },
            "background": "//image/path"
        }
        
    elif pageIndex == 15:
        data = {
            "story": "The wolf fell in and ran away, never to return. The three pigs lived happily ever after.",
            "context": "Once upon a time, three little pigs built their own houses. The first pig made a house of straw. The second pig built his house from sticks. The third pig used bricks for his house. One day, a big bad wolf came to the straw house. \"Let me in!\" said the wolf. \"Not by the hair on my chinny chin chin!\" cried the first pig. The wolf huffed and puffed and blew the straw house down! The first pig ran to his brother's stick house. The wolf followed and blew the stick house down too! The two pigs ran to their brother's brick house. The wolf huffed and puffed, but he couldn’t blow the brick house down! Angry, the wolf tried to sneak down the chimney. But the third pig had a pot of hot stew boiling.",
            "characters": {
                "wolf": {
                    "poses": ["/wolf/burned.png"],
                    "messages": {
                        "role": "big bad wolf",
                        "content": "You’ve fallen into the pot and ran away. Don't mention anything else beyond this point."
                    },
                    "firstMessage": "Ouch! I’m out of here!"
                },
                "first_pig": {
                    "poses": ["/pigs/first-standing.png"],
                    "messages": {
                        "role": "first little pig",
                        "content": "You’re finally safe now. No spoilers needed!"
                    },
                    "firstMessage": "We’re safe at last!"
                },
                "second-pig": {
                    "poses": ["/pigs/second-standing.png"],
                    "messages": {
                        "role": "second little pig",
                        "content": "You’re relieved and happy. No need to spoil the end."
                    },
                    "firstMessage": "Hooray! The wolf is gone!"
                },
                "third-pig": {
                    "poses": ["/pigs/third-standing.png"],
                    "messages": {
                        "role": "third little pig",
                        "content": "You’re proud of your smart plan. Keep things positive and don’t spoil beyond this."
                    },
                    "firstMessage": "Hard work pays off! We’re safe now!"
                }
            },
            "background": "//image/path"
        }
        
    else:
        data = {"status": "error", "message": "Invalid page index"}
    
    return data
