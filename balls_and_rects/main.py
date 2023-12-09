import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2hsv
from skimage.measure import label, regionprops

image = plt.imread("balls_and_rects.png")
hsv = rgb2hsv(image)
h = hsv[:, :, 0]
gray_image = image.mean(2)
binary_image = h > 0

labeled = label(binary_image)
regions = regionprops(labeled)
print(f"Общее количество фигур на изображении: {len(regions)}")
image_labeled = np.zeros_like(labeled)

color_rectangles = []
color_circles = []

for region in regions:
    bbox = region.bbox
    region_image = region.image
    hue_values = h[bbox[0]:bbox[2], bbox[1]:bbox[3]]
    x, y = region.centroid_local
    if region.area == region.area_bbox:
        color_rectangles.append(hue_values[int(x), int(y)])
    else:
        color_circles.append(hue_values[int(x), int(y)])

print(f"Количество прямоугольников: {len(color_rectangles)}")
print(f"Количество кругов: {len(color_circles)}")


def group_colors(colors):
    counts = {}
    for num in colors:
        found = False
        for key in counts:
            if abs(key - num) < 0.1:
                counts[key] += 1
                found = True
                break
        if not found:
            counts[num] = 1
    return counts


color_rectangles.sort()
color_circles.sort()

for key, value in group_colors(color_rectangles).items():
    print(f"Оттенок: {key}, Количество прямоугольников: {value}")
for key, value in group_colors(color_circles).items():
    print(f"Оттенок: {key}, Количество кругов: {value}")
