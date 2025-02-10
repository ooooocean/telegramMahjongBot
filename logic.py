import random

winds_dict = {
    "east_wind": {
        "tile_unicode": "🀀",
        "name": "East Wind",
        "type": "wind",
        "num_val": "",
        "direction": "east"
    },
    "south_wind": {
        "tile_unicode": "🀁",
        "name": "South Wind",
        "type": "wind",
        "num_val": "",
        "direction": "south"
    },
    "west_wind": {
        "tile_unicode": "🀂",
        "name": "West Wind",
        "type": "wind",
        "num_val": "",
        "direction": "west"
    },
    "north_wind": {
        "tile_unicode": "🀃",
        "name": "North Wind",
        "type": "wind",
        "num_val": "",
        "direction": "north"
    },
}

dragons_dict = {
    "white_dragon": {
        "tile_unicode": "🀄",
        "name": "White Dragon",
        "type": "dragon",
    },
    "green_dragon": {
        "tile_unicode": "🀅",  # Using a placeholder, as the green dragon might not have a standard emoji
        "name": "Green Dragon",
        "type": "dragon",
    },
    "red_dragon": {
        "tile_unicode": "🀆",  # Using a placeholder, as the red dragon might not have a standard emoji
        "name": "Red Dragon",
        "type": "dragon",
    },
}

flowers_dict = {
    "plum": {
        "tile_unicode": "🀢",
        "name": "plum",
        "num_val": 1
    },
    "orchid": {
        "tile_unicode": "🀣",
        "name": "orchid",
        "num_val": 2
    },
    "chrysanthemum": {
        "tile_unicode": "🀥",
        "name": "chrysanthemum",
        "num_val": 3
    },
    "bamboo": {
        "tile_unicode": "🀤",
        "name": "bamboo",
        "num_val": 4
    },
    "spring": {
        "tile_unicode": "🀦",
        "name": "spring",
        "num_val": 1,
    },
    "summer": {
        "tile_unicode": "🀧",
        "name": "summer",
        "num_val": 2
    },
    "autumn": {
        "tile_unicode": "🀨",
        "name": "autumn",
        "num_val": 3
    },
    "winter": {
        "tile_unicode": "🀩",
        "name": "winter",
        "num_val": 4
    },
}

animals_dict = {
    "cat": {
        "tile_unicode": "🐈",
        "name": "cat",
    },
    "mouse": {
        "tile_unicode": "🐁",
        "name": "mouse",
    },
    "rooster": {
        "tile_unicode": "🐓",
        "name": "rooster",
    },
    "centipede": {
        "tile_unicode": "🐛",
        "name": "centipede",
    }
}

dots_dict = {
    "one_dot": {
        "tile_unicode": "🀙",
        "name": "one dot",
        "type": "dot",
        "num_val": 1
    },
    "two_dots": {
        "tile_unicode": "🀚",
        "name": "two dots",
        "type": "dot",
        "num_val": 2
    },
    "three_dots": {
        "tile_unicode": "🀛",
        "name": "three dots",
        "type": "dot",
        "num_val": 3
    },
    "four_dots": {
        "tile_unicode": "🀜",
        "name": "four dots",
        "type": "dot",
        "num_val": 4
    },
    "five_dots": {
        "tile_unicode": "🀝",
        "name": "five dots",
        "type": "dot",
        "num_val": 5
    },
    "six_dots": {
        "tile_unicode": "🀞",
        "name": "six dots",
        "type": "dot",
        "num_val": 6
    },
    "seven_dots": {
        "tile_unicode": "🀟",
        "name": "seven dots",
        "type": "dot",
        "num_val": 7
    },
    "eight_dots": {
        "tile_unicode": "🀠",
        "name": "eight dots",
        "type": "dot",
        "num_val": 8
    },
    "nine_dots": {
        "tile_unicode": "🀡",
        "name": "nine dots",
        "type": "dot",
        "num_val": 9
    },
}

character_dict = {
    "one_character": {
        "tile_unicode": "🀇",
        "name": "one character",
        "type": "character",
        "num_val": 1
    },
    "two_characters": {
        "tile_unicode": "🀈",
        "name": "two characters",
        "type": "character",
        "num_val": 2
    },
    "three_characters": {
        "tile_unicode": "🀉",
        "name": "three characters",
        "type": "character",
        "num_val": 3
    },
    "four_characters": {
        "tile_unicode": "🀊",
        "name": "four characters",
        "type": "character",
        "num_val": 4
    },
    "five_characters": {
        "tile_unicode": "🀋",
        "name": "five characters",
        "type": "character",
        "num_val": 5
    },
    "six_characters": {
        "tile_unicode": "🀌",
        "name": "six characters",
        "type": "character",
        "num_val": 6
    },
    "seven_characters": {
        "tile_unicode": "🀍",
        "name": "seven characters",
        "type": "character",
        "num_val": 7
    },
    "eight_characters": {
        "tile_unicode": "🀎",
        "name": "eight characters",
        "type": "character",
        "num_val": 8
    },
    "nine_characters": {
        "tile_unicode": "🀏",
        "name": "nine characters",
        "type": "character",
        "num_val": 9
    },
}

bamboo_dict = {
    "one_bamboo": {
        "tile_unicode": "🀐",
        "name": "one bamboo",
        "type": "bamboo",
        "num_val": 1
    },
    "two_bamboos": {
        "tile_unicode": "🀑",
        "name": "two bamboos",
        "type": "bamboo",
        "num_val": 2
    },
    "three_bamboos": {
        "tile_unicode": "🀒",
        "name": "three bamboos",
        "type": "bamboo",
        "num_val": 3
    },
    "four_bamboos": {
        "tile_unicode": "🀓",
        "name": "four bamboos",
        "type": "bamboo",
        "num_val": 4
    },
    "five_bamboos": {
        "tile_unicode": "🀔",
        "name": "five bamboos",
        "type": "bamboo",
        "num_val": 5
    },
    "six_bamboos": {
        "tile_unicode": "🀕",
        "name": "six bamboos",
        "type": "bamboo",
        "num_val": 6
    },
    "seven_bamboos": {
        "tile_unicode": "🀖",
        "name": "seven bamboos",
        "type": "bamboo",
        "num_val": 7
    },
    "eight_bamboos": {
        "tile_unicode": "🀗",
        "name": "eight bamboos",
        "type": "bamboo",
        "num_val": 8
    },
    "nine_bamboos": {
        "tile_unicode": "🀘",
        "name": "nine bamboos",
        "type": "bamboo",
        "num_val": 9
    },
}


def create_deck():
    winds = 4 * [wind["tile_unicode"] for wind in winds_dict.values()]
    dragons = 4 * [dragon["tile_unicode"] for dragon in dragons_dict.values()]
    flowers = [flower["tile_unicode"] for flower in flowers_dict.values()]
    animals = [animal["tile_unicode"] for animal in animals_dict.values()]
    dots = 4 * [dot["tile_unicode"] for dot in dots_dict.values()]
    characters = 4 * [character["tile_unicode"] for character in character_dict.values()]
    bamboo = 4 * [bamboo["tile_unicode"] for bamboo in bamboo_dict.values()]

    deck = winds + dragons + flowers + animals + dots + characters + bamboo
    random.shuffle(deck)
    return deck