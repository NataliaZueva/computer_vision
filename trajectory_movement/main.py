import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops

x_1, y_1, y_2, x_2 = [], [], [], []
for i in range(100):
    image = np.load(f"out/h_{i}.npy")
    labeled = label(image)
    regions = sorted(regionprops(labeled), key=lambda region: region.area)

    (x1, y1) = regions[1].centroid
    (x2, y2) = regions[0].centroid

    x_1.append(x1)
    y_1.append(y1)
    x_2.append(x2)
    y_2.append(y2)

plt.plot(x_1, y_1)
plt.plot(y_2, x_2)
plt.show()
