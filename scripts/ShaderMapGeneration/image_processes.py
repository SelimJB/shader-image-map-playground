from skimage import feature, morphology
import numpy as np
import cv2
import os
import numpy as np
from skimage import morphology
from skimage.morphology import medial_axis
from skimage.util import invert
from skimage.io import imread
import json
import os
import random
from IPython.display import display
from PIL import Image


def convertToRGB(img,  display=False, size=None):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if (size != None):
        imgRGB = cv2.resize(imgRGB, size)
    if display:
        show(imgRGB)
    return imgRGB


# 0 - 255
def convertToGray(img,  display=False, size=None):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if (size != None):
        imgGray = cv2.resize(imgGray, size)
    if display:
        show(imgGray)
    return imgGray


def threshold(grayImg, grayThreshold, display=False):
    _, thresholded = cv2.threshold(
        grayImg, grayThreshold, 255, cv2.THRESH_BINARY)
    if display:
        show(thresholded)
    return thresholded


def canny(grayImg, grayThreshold, sigma, display=False):
    sigma = 4
    _, thresholded = cv2.threshold(
        grayImg, grayThreshold, 255, cv2.THRESH_BINARY)
    canny = feature.canny(thresholded, sigma=sigma)
    if display:
        show(canny)
    return canny


def imreadGrayNormalized(imgPath, size=None):
    gray_normalized = imread(imgPath, as_gray=True)  # -> 0-1
    if size != None:
        gray_normalized = cv2.resize(gray_normalized, size)
    return gray_normalized


# Need a 0-255 array -> li
def getContours(grayImg, grayThreshold):
    _, thresh = cv2.threshold(grayImg, grayThreshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    points = []
    for i, contour in enumerate(contours):
        points.append(contour[0])
    return contours, points


# To test contours
def drawContours(skeletonImg, contours, display=False):
    skeleton_uint8 = (skeletonImg * 255).astype(np.uint8)
    filled_image = cv2.cvtColor(skeleton_uint8, cv2.COLOR_GRAY2BGR)
    for i, contour in enumerate(contours):
        color = (np.random.randint(0, 255), np.random.randint(
            0, 255), np.random.randint(0, 255))
        cv2.drawContours(filled_image, contours, i, color, -1)
    if display:
        show(filled_image)
    return filled_image


# To test contours filling
def fillContours(skeletonImg, contoursImg, points, display=False):
    skeleton_uint8 = (skeletonImg * 255).astype(np.uint8)
    copy = cv2.cvtColor(invert(skeleton_uint8), cv2.COLOR_GRAY2BGR)
    for point in points:
        x, y = point[0]
        color = tuple(contoursImg[y, x])
        color = (int(color[0]), int(color[1]), int(color[2]))
        cv2.floodFill(copy, None, (x, y), color)
    if display:
        show(copy)


# A gaussian blur can be used to smooth the image and improve the skeletonization process
# The kernel size must be positive and odd
# The image is normalized between 0-1 to be given to the skeletonization function
def gaussianBlur(img, kernel=(5, 5), display=False):
    res = cv2.GaussianBlur(img, kernel, 0)
    if display:
        show(res)
    return res / 255


# Need a 0-1 array -> bool array
def skeletonize(grayNormalizedImg, sensitivity, display=False, shouldInvert=True):
    binary_image = grayNormalizedImg > sensitivity
    binary_image = invert(binary_image)
    skeleton, distance = medial_axis(binary_image, return_distance=True)
    if (shouldInvert):
        skeleton = invert(skeleton)
    if display:
        show(skeleton)
    return skeleton


def hex_to_rgba(hex_color):
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    if len(hex_color) == 6:
        r, g, b = int(hex_color[:2], 16), int(
            hex_color[2:4], 16), int(hex_color[4:6], 16)
        return [r/255.0, g/255.0, b/255.0, 1.0]


def show(img):
    pilImage = Image.fromarray(img)
    display(pilImage)


def printArrayType(img):
    if len(img.shape) == 2:
        if img.dtype == bool:
            print("Bool Array")
        elif img.dtype == np.uint8:
            print("0-255 Gray")
        elif img.dtype == np.float64:
            print("0-1 Gray")
    elif len(img.shape) == 3:
        if img.dtype == np.uint8:
            print("0-255 RGB")
        elif img.dtype == np.float64:
            print("0-1 RGB")
    else:
        raise Exception("Unknown image type")


# Alpha SUBTRACTION
def alphaSubtraction(image, subtractionImage, display=False):
    res = image.copy()
    res[:, :, 3][subtractionImage[:, :, 3] > 0] = 0
    if (display):
        show(res)
    return res


def alphaSubstractionWithThreshold(image, subtractionImage, threshold=254, display=False):
    res = image.copy()
    res[:, :, 3][subtractionImage[:, :, 3] > threshold] = 0
    if (display):
        show(res)
    return res


def createBlankImage(width, height, color=(255, 255, 255, 255)):
    blank_image = np.zeros((height, width, 4), np.uint8)
    blank_image[:, :] = color
    return blank_image


# Thickening
def dilatation(img, kernelSize, display=False):
    kernel = np.ones((kernelSize, kernelSize), np.uint8)
    img_dilated = cv2.dilate(img, kernel, iterations=1)
    if display:
        show(img_dilated)
    return img_dilated


def blur(img, kernelSize, display=False):
    kernel = np.ones((kernelSize, kernelSize), np.float32) / (kernelSize**2)
    img_blurred = cv2.filter2D(img, -1, kernel)
    if display:
        show(img_blurred)
    return img_blurred


# Funny use of DILATATION to remove borders
def removeLines(img, kernelSize, display=False):
    kernel = np.ones((kernelSize, kernelSize), np.uint8)
    dil = cv2.dilate(img, kernel, iterations=3)
    if display:
        show(dil)


def toRgba(img):
    color_channel = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    # color_channel only white pixels
    color_channel[color_channel > 0] = 255
    alpha_channel = img.copy()  # Use grayscale image as alpha channel
    alpha_channel = alpha_channel.astype(
        img.dtype)  # Ensure data type consistency
    black_pixels_mask = cv2.inRange(img, 0, 20)
    alpha_channel[black_pixels_mask == 255] = 0
    res = cv2.merge((color_channel, alpha_channel))
    return res


def normalizeBlurredImage(img, percentilTreshold, display=False):
    # Filter out black pixels
    non_black_pixels = img[img > 0]
    # mean_color = np.mean(non_black_pixels)
    threshold = np.percentile(non_black_pixels, percentilTreshold)
    # Each pixel above this threshold are white
    normalized_pixels = np.where(
        non_black_pixels > threshold, 255, non_black_pixels / threshold * 255)
    img_normalized = img.copy()
    img_normalized[img_normalized > 0] = normalized_pixels.astype(np.uint8)
    blur_rgba = toRgba(img_normalized)
    if display:
        print("Threshold:", threshold)
        show(blur_rgba)
    return blur_rgba


def superpose(background, foreground):
    copied_image = background.copy()

    # Get the alpha channel of the target image
    target_alpha = foreground[:, :, 3] / 255.0

    # Replace the pixels in the copied image
    copied_image[target_alpha != 0] = foreground[target_alpha != 0]

    return copied_image


def test(skeleton, kernelSize, display=False):
    def dilate(binary_image, alpha, kernelSize):
        img = (binary_image * alpha).astype(np.uint8)
        kernel = np.ones((kernelSize, kernelSize), np.uint8)
        return cv2.dilate(img, kernel, iterations=1)
    dilatation1 = toRgba(dilate(skeleton, 255, 3))
    dilatation2 = toRgba(dilate(skeleton, 153, 4))
    dilatation3 = toRgba(dilate(skeleton, 91, 5))
    dilatation4 = toRgba(dilate(skeleton, 55, 6))
    composition = superpose(dilatation4, superpose(
        dilatation3, superpose(dilatation2, dilatation1)))
    if display:
        show(composition)
    return composition


# The best formula I found was base on dilatation + blur
def thickening(skeleton, dilatationKernelSize, blurKernelSize, normalizationPercentilThreshold, color=[1, 1, 1, 1], display=False, displayIntermediateSteps=False):
    skeleton_uint8 = (skeleton * 255).astype(np.uint8)
    dilatationImg = dilatation(
        skeleton_uint8, dilatationKernelSize, displayIntermediateSteps)
    blurImg = blur(dilatationImg, blurKernelSize, displayIntermediateSteps)
    norm = normalizeBlurredImage(
        blurImg, normalizationPercentilThreshold, displayIntermediateSteps)
    colored_norm = norm * color
    colored_norm = colored_norm.astype(np.uint8)
    if display:
        show(colored_norm)
    return colored_norm
