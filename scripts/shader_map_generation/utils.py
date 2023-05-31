import json
import os
import random
from IPython.display import display
from PIL import Image
import cv2
import numpy as np


def show(img):
    pilImage = Image.fromarray(img)
    display(pilImage)


def saveCVImage(path, fileName, img, code=cv2.COLOR_BGR2RGBA):
    cv2.imwrite(os.path.join(path, fileName),
                cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))


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


def saveBinaryImage(path, image):
    cv2.imwrite(path, (image * 255).astype(np.uint8))


def writeJson(data, outputPath, projectName):
    json_data = json.dumps(data,   indent=4)
    jsonPath = os.path.join(outputPath, projectName + '.json')
    with open(jsonPath, 'w') as file:
        file.write(json_data)
