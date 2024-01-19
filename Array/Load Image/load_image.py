import matplotlib.pyplot as plt
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        img = plt.imread(path)
    except Exception as e:
        print(e)
        exit(2)
    print(f"The shape of image is: {img.shape}")
    return img