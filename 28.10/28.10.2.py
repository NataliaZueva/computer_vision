from skimage.measure import label
import numpy as np


def area(labeled, label=1):
    return (labeled[labeled == label] / label).sum()


image = np.load(r"coins.npy.txt")
label_image = label(image)

denominations = [1, 2, 5, 10]

square = {}
for a in range(1, np.max(label(label_image)) + 1):
    new_image = np.zeros_like(label_image)
    new_image[label_image == a] = 1
    is_area = area(new_image)
    # print(f"is_area {is_area}")
    if is_area in square.keys():
        square[is_area] += 1
    else:
        square[is_area] = 1

dictionary = dict(sorted(square.items(), key=lambda x: x[0]))

total_sum, k = 0, 0
for i in dictionary:
    total_sum += dictionary[i] * denominations[k]
    k += 1
print(total_sum)
