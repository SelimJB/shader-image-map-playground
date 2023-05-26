import cv2
import utils as ut
import numpy as np
from skimage.morphology import medial_axis
from skimage.util import invert
from skimage.io import imread
import posixpath


class ProvinceDataView:
    def __init__(self, name, color, id, hash, fixed_position):
        self.name = name
        self.color = color
        self.id = id
        self.hash = hash
        self.fixed_position = fixed_position


def doMapQuantization(skeleton, points, display=False, debug=False):
    skeleton_uint8 = (invert(skeleton) * 255).astype(np.uint8)
    mapColor = cv2.cvtColor(skeleton_uint8, cv2.COLOR_GRAY2BGR)
    provinceDataViews = [ProvinceDataView(
        "", "#000000", 0, 0, {"x": 0, "y": 0})]
    shiftedPoints = points[1:]  # points are shifted by 1

    for j, point in enumerate(points):
        if (j == len(points)-1):
            x, y = 0, 0
        else:
            x, y = shiftedPoints[j][0]
        index = j+1
        color = getQuantizedColor(index)
        provinceDataView = ProvinceDataView(ut.generateRandomName(
        ), ut.getHexRandomColor(index), index, getQuantizedValue(color), {"x": int(x), "y": int(y)})
        # print(j, ut.getQuantizedValue(color), x, y)
        provinceDataViews.append(provinceDataView)
        cv2.floodFill(mapColor, None, (x, y), color)

    mapDebug = None
    if debug:
        mapDebug = mapColor.copy()
        for j, point in enumerate(points):
            if (j == len(points)-1):
                x, y = 0, 0
            else:
                x, y = shiftedPoints[j][0]
            index = j+1
            cv2.putText(mapDebug, str(index), (x-30, y+30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
        ut.show(mapDebug)

    if display:
        ut.show(mapColor)

    return provinceDataViews, mapColor, mapDebug


q = 10  # quantization
offset = 5
range = 255 - q - offset


QUANTIZATION_PRECISENESS = 10
QUANTIZATION_LEVEL_COUNT = 26


def getQuantizedColor(i):
    r = range - int(i / (range/q))*q
    g = range - (i*q) % range
    b = q
    return (r, g, b)


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
    # print(f"r: {r}, g: {g}, b: {b}, quantization: {quantization}")
    return quantization


def createMapJson(mapName, quantizationPrecision, provinceDataViews, width, height):
    mapData = generateMapData()
    provinceDataViewsJson = convertProvinceDataViewArrayToJson(
        provinceDataViews)
    mapData["key"] = mapName
    mapData["name"] = mapName
    mapData["route"] = mapName
    mapData["quantizationPrecision"] = quantizationPrecision
    mapData["provinces"] = provinceDataViewsJson
    mapData["sceneSize"] = {"width": width, "height": height}
    mapData["mapViewTextures"] = getMapViewTextures(mapName)

    return mapData


def convertProvinceDataViewArrayToJson(my_objects):
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


def generateMapData():
    return {
        "key": "conquest",
        "name": "Conquest",
        "route": "conquest",
        "description": "The conquest map",
        "initializationUniforms": {
            "uGlowRadius": 0.016,
            "uGlowPulsationRadius": 0.004,
            "uGlowPulsationPeriod": 4.5,
            "uMouseIlluminationRadius": 0.19
        },
        "quantizationPrecision": 10,
        "textureScale": 1,
        "sceneSize": {"width": 4096, "height": 4096},
        "useFixedPosition": True,
        "mapViewTextures": {
            "map": {"key": "Map", "url": "game/conquest/map/Map2048.png"},
            "bitmap": {"key": "Bitmap", "url": "game/conquest/map/Map2048_colors.png"},
            "mapBorders": {"key": "MapBorders", "url": "game/conquest/map/Map2048_nobackground.png"},
            "mapGlow": {"key": "MapGlow", "url": "game/conquest/map/Map2048_glow.png"},
            "debugMap": {"key": "DebugMap", "url": "game/conquest/map/Map2048_debug.png"}
        },
        "provinces": []
    }


def getMapViewTextures(projectName):
    path = posixpath.join("game/conquest/map", projectName)
    return {
        "map": {
            "key": "Map",
            "url": posixpath.join(path, "input.png")
        },
        "bitmap": {
            "key": "Bitmap",
            "url": posixpath.join(path, "map_colors.png")
        },
        "mapBorders": {
            "key": "MapBorders",
            "url": posixpath.join(path, "map_borders.png")
        },
        "mapGlow": {
            "key": "MapGlow",
            "url": posixpath.join(path, "map_glow.png")
        },
        "debugMap": {
            "key": "DebugMap",
            "url": posixpath.join(path, "map_debug.png")
        }
    }
