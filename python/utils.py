from IPython.display import display
from PIL import Image


def show(img):
    pilImage = Image.fromarray(img)
    display(pilImage)

def getColor(i):
    r = 240 - int(i / 16)*15
    g = 240 - (i*15)%240
    b = 0
    return (r,g,b)
