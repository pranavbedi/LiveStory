
async def get_page(pageIndex: int):
    # Define data for different pages

    if pageIndex == 3:
        data = {
            "content": "Once upon a time, there lived three little pigs.",
            "characters": [
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path"
        }

    elif pageIndex == 4:
        data = {
            "content": "One day, they decided to leave home and build houses of their own.",
            "characters": [
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path2"
        }


    elif pageIndex == 5:
        data = {
            "content": "The first little pig thought that straw would make a good house.",
            "characters": [
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"person": "JSON stuff",
                 "person_voice": ""}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 6:
        data = {
            "content": "He built the house very quickly and he was very pleased with it.",
            "characters": [
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 7:
        data = {
            "content": "The second little pig thought that sticks would make a fine house.",
            "characters": [
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"person": "JSON stuff",
                 "person_voice": ""}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 8:
        data = {
            "content": "He built the house very quickly and he was very pleased with it.",
            "characters": [
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 9:
        data = {
            "content": "The third little pig thought that bricks would make a strong house.",
            "characters": [
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"person": "JSON stuff",
                 "person_voice": ""}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 10:
        data = {
            "content": "It took him a long time to build the house but he was very pleased with it.",
            "characters": [
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 11:
        data = {
            "content": "One day, a big bad wolf came along.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                }
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 12:
        data = {
            "content": "He saw the first little pig in his house of straw.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                }
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 13:
        data = {
            "content": "“Little pig, little pig, let me come in,” he snarled. “Not by the hair on my chinny, chin, chin!” cried the first little pig.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 14:
        data = {
            "content": "“Then I’ll huff and I’ll puff and I’ll blow your house down!” growled the big bad wolf.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 15:
        data = {
            "content": "“Little pig, little pig, let me come in,” he snarled. “Not by the hair on my chinny, chin, chin!” cried the first little pig.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 16:
        data = {
            "content": "The first little pig escaped and ran to join his brother in the house made of sticks.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 17:
        data = {
            "content": "The big bad wolf followed the little pig to the house made of sticks.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                }
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 18:
        data = {
            "content": "“Little pig, little pig, let me come in,” he snarled. “Not by the hair on my chinny, chin, chin!” cried the second little pig.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    elif pageIndex == 19:
        data = {
            "content": "“Then I’ll huff and I’ll puff and I’ll blow your house down!” growled the big bad wolf.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    elif pageIndex == 20:
        data = {
            "content": "So he huffed and he puffed and he blew the house down! ",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    elif pageIndex == 21:
        data = {
            "content": "The two little pigs escaped and ran to join their brother in the house made of bricks. ",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 22:
        data = {
            "content": "The big bad wolf followed the pigs to the house made of bricks.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                }
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 23:
        data = {
            "content": "“Little pig, little pig, let me come in,” he snarled. “Not by the hair on my chinny, chin, chin!” cried the third little pig.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 24:
        data = {
            "content": "“Then I’ll huff and I’ll puff and I’ll blow your house down!” growled the big bad wolf.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    elif pageIndex == 25:
        data = {
            "content": "He huffed and he puffed, but the house was too strong. He could not blow it down!",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    elif pageIndex == 26:
        data = {
            "content": "This made the big bad wolf very angry. He climbed onto the roof of the house so he could crawl down the chimney.",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 27:
        data = {
            "content": "The big bad wolf was in for a big surprise!",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                 {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                 {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 28:
        data = {
            "content": "The third little pig had been cooking a big pot of stew and SPLASH! The wolf fell right into the pot!",
            "characters": [
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                 {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                 {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    elif pageIndex == 29:
        data = {
            "content": "The wolf was very shocked. He jumped out of the pot and ran straight out of the house. He never came back again. ",
            "characters": [
                {
                    "wolf_assets": "JSON stuff",
                    "wolf_voice": "f9cd08ce-38a0-4809-b666-10d4c6254f9d"
                },
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }

    elif pageIndex == 30:
        data = {
            "content": "The little pigs lived happily ever after in the house made of bricks.",
            "characters": [
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    elif pageIndex == 31:
        data = {
            "content": "",
            "characters": [
                {"pig_1": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                 {"pig_2": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"},
                 {"pig_3": "JSON stuff",
                 "pig_voice": "alkdfjeajvneeaohadfjk"}
            ],
            "background": "//image/path3"
        }


    else:
        # Default content if pageIndex doesn't match
        data = {
            "content": "Page not found.",
            "characters": [],
            "background": "//image/default"
        }
        
    return data


