import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops


def has_vline(arr):
    return 1. in arr.mean(0)


def recognize(prop):
    euler_number = prop.euler_number
    if euler_number == -1:      # Определяем по кругам: 8 или B
        if has_vline(prop.image):
            return "B"
        else:
            return "8"
    elif euler_number == 0:      # Если 1 круг: A 0 P D
        if has_vline(prop.image):  # P D
            if prop.eccentricity > 0.6:
                return "P"
            else:
                return "D"
        else:
            y, x = prop.centroid_local
            y /= prop.image.shape[0]
            x /= prop.image.shape[1]
            if np.isclose(x, y, 0.04):
                return "0"
            else:
                return "A"
    else:
        if prop.image.mean() == 1.0:    # нет кругов, то символы:  :\ ) 1 W X * - /
            return "-"
        else:
            if has_vline(prop.image) and has_vline(prop.image.T):
                return "1"
            else:
                tmp = prop.image.copy()
                tmp[[0, -1], :] = 1
                tmp[:, [0, -1]] = 1
                tmp_labeled = label(tmp)
                tmp_props = regionprops(tmp_labeled)
                tmp_euler = tmp_props[0].euler_number
                if tmp_euler == -3:
                    return "X"
                elif tmp_euler == -1:
                    return "/"
                else:
                    if prop.eccentricity > 0.5:
                        return "W"
                    else:
                        return "*"
    return "_"


# image = plt.imread(r"alphabet-ext.png")
image = plt.imread(r"symbols.png")
# print(image)

image = image.mean(2)
image = image > 0
# print(image.shape)

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
print((1 - result.get("_", 0) / np.max(labeled)) * 100)
