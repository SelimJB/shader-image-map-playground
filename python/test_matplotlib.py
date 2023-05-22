import os
import cv2
from matplotlib import pyplot as plt

imgPath = os.path.join('textures', 'goomba.png')
img = cv2.imread(imgPath)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)

plt.show()
