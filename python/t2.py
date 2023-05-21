import os
import cv2
from matplotlib import pyplot as plt

imgPath = os.path.join('textures', 'goomba.png')
# Load the image
img = cv2.imread(imgPath)

# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Use plt.imshow() to add the image to the matplotlib plot
plt.imshow(img_rgb)

# Display the plot with the image
plt.show()
