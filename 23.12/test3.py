import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops


def has_vline(arr):
    return 1. in arr.mean(1)


def recognize(prop):
    euler_number = prop.euler_number
    if euler_number == 0:
        if has_vline(prop.image):
            return "R"
        else:
            return "D"
    elif euler_number == 1:
        if not has_vline(prop.image):
            return "K"
        else:
            if prop.image[0, -1] == 0:
                return "J"
            else:
                return "L"


image = plt.imread('task3.png')

image = image.mean(2)
image = image > 0.25

labeled = label(image)
print(len(np.unique(labeled)) - 1)

props = regionprops(labeled)
result = {}
for prop in props:
    symbol = recognize(prop)
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1

print(result)
