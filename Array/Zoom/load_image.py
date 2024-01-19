import matplotlib.pyplot as plt
import numpy as np

def load_image(path: str) -> np.array:
    try:
        img = plt.imread(path)
    except Exception as e:
        print(e)
        exit()
    print(f"The shape of image is: {img.shape}")
    return img