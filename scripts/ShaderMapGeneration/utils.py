import random
from IPython.display import display
from PIL import Image


def show(img):
    pilImage = Image.fromarray(img)
    display(pilImage)


q = 10  # quantization
offset = 5
range = 255 - q - offset


def getQuantizedColor(i):
    r = range - int(i / (range/q))*q
    g = range - (i*q) % range
    b = q
    return (r, g, b)


def getHexRandomColor(i):
    colors = [
        "#F6A2AC",
        "#94B0E0",
        "#FDE79D",
        "#A6E0E7",
        "#E6A5F1",
        "#D2A2F6",
        "#A1D9B9",
        "#F6A2AC",
        "#A7DAA2",
        "#8BA9E6",
        "#FCF0A1",
        "#F4B0A7",
        "#FAC8D9",
        "#C6D8F5",
        "#FFF1C9",
        "#D7F1D4",
        "#F2D9EB",
        "#F6A2AC",
        "#94B0E0",
        "#FDE79D",
    ]
    return colors[i % len(colors)]


def getRandomColor(i):
    color = getHexRandomColor(i)
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    return (r, g, b)


def generateRandomName():
    n1 = [
        'Swift', 'Brave', 'Bright', 'Zesty', 'Fancy', 'Jolly', 'Sunny', 'Merry', 'Slick', 'Zippy',
        'Max', 'Lily', 'Alex', 'Emma', 'Jack', 'Lucy', 'Finn', 'Ruby', 'Noah', 'Ava',
        'Dusk', 'Pearl', 'Skye', 'Sage', 'River', 'Storm', 'Basil', 'Luna', 'Jade', 'Cleo',
        'Axel', 'Ivy', 'Kai', 'Zara', 'Tate', 'Mika', 'Coco', 'Neo', 'Jinx', 'Nova',    'Bold', 'Calm', 'Dazz', 'Epic', 'Free', 'Glad', 'Hazy', 'Misty', 'Nifty', 'Plum',
        'Ripe', 'Sage', 'True', 'Wavy', 'Zest', 'Keen', 'Jade', 'Tall', 'Fine', 'Lush'
    ]
    n2 = [
        'Adia', 'Bela', 'Cora', 'Duna', 'Elba', 'Fira', 'Gala', 'Hela', 'Idra', 'Jara',
        'Kora', 'Lida', 'Mira', 'Nora', 'Orla', 'Pira', 'Qara', 'Rada', 'Sina', 'Tara',
        'Usha', 'Vada', 'Wela', 'Xena', 'Yara', 'Zara',
        'Alba', 'Bora', 'Ceta', 'Dara', 'Elda', 'Fita', 'Gita', 'Hema', 'Inca', 'Jeta',
        'Kala', 'Lena', 'Mena', 'Neva', 'Oria', 'Peta', 'Qila', 'Risa', 'Sera', 'Tesa',
        'Una', 'Vera', 'Wina', 'Xola', 'Yona', 'Zeta'
    ]

    adjective = random.choice(n1)
    noun = random.choice(n2)

    random_name = f"{adjective}-{noun}"
    return random_name


QUANTIZATION_PRECISENESS = 15
QUANTIZATION_LEVEL_COUNT = 17


def getQuantizedValue(color):
    r = color[0]
    g = color[1]
    b = color[2]
    r = int(r / QUANTIZATION_PRECISENESS)
    g = int(g / QUANTIZATION_PRECISENESS)
    b = int(b / QUANTIZATION_PRECISENESS)

    if r == 0 or g == 0 or g == QUANTIZATION_LEVEL_COUNT or b != 1:
        return 0

    quantization = g + (QUANTIZATION_LEVEL_COUNT - r) * 100

    return quantization


class ProvinceDataView:
    def __init__(self, name, color, id, hash, fixed_position):
        self.name = name
        self.color = color
        self.id = id
        self.hash = hash
        self.fixed_position = fixed_position


def convertProvinceDataViewArrayToJson(my_objects):
    # Print keys and values
    # for obj in my_objects:
    #     print(obj)
    return [
        {
            "name": obj.name,
            "color": obj.color,
            "id": obj.id,
            "hash": obj.hash,
            "fixedPosition": obj.fixed_position
        }
        for obj in my_objects
    ]
