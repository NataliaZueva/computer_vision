from skimage.measure import label
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import cv2


def area(labeled, label=1):
    return (labeled[labeled == label] / label).sum()


image = np.load(r"coins.npy.txt")
label_image = label(image)

denominations = [1, 2, 5, 10]
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
areas = []
for contour in contours:
    area = cv2.contourArea(contour)
    areas.append(area)
dictionary = dict(sorted(dict(Counter(areas)).items(), key=lambda x: x[0]))


square = {}
for a in (1, np.max(label(label_image)) + 1):
    new_image = np.zeros_like(label_image)
    new_image[label_image == a] = 1
    plt.imshow(label(new_image))
    plt.show()
    is_area = area(new_image)
    if is_area in square.keys():
        square[is_area] += 1
    else:
        square = {is_area, 1}
print(dictionary)
print(square)


total_sum = 0
k = 0
for i in dictionary:
    total_sum += dictionary[i] * denominations[k]
    k += 1
print(total_sum)