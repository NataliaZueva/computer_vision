import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion)
from skimage.measure import label

wires = np.load(r"wires5.npy")
struct = np.ones((3, 1))
plt.imshow(label(wires))
labeled = label(wires)
for lb in range(1, np.max(labeled) + 1):
    new_image = np.zeros_like(wires)
    new_image[labeled == lb] = 1
    wi = label(binary_erosion(new_image, struct))
    num = np.max(label(wi))
    print(f"В проводе №{lb}: {num} части - {('Провод это разрыв') if num == 0 else ('Провод цел') if num == 1 else (f'имеется {num-1} разрыва')}")

plt.show()

