import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)
from skimage.measure import label

stars = np.load(r"stars.npy")

struct = np.ones((3, 3))
plt.imshow(label(stars))
print(np.max(label(stars)) - np.max(label(binary_erosion(stars, struct))))
plt.show()
