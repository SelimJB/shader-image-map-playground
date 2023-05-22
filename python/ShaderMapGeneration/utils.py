from IPython.display import display
from PIL import Image


def show(img):
    pilImage = Image.fromarray(img)
    display(pilImage)

q = 10 # quantization
offset = 5
range = 255 - q - offset

def getColor(i):
    r = range - int(i / (range/q))*q
    g = range - (i*q)%range
    b = q
    return (r,g,b)
