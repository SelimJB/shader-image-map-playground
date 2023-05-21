import os
import cv2

imgPath = os.path.join('textures', 'goomba.png')
img = cv2.imread(imgPath)

# Display the image in a window
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()