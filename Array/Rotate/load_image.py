import matplotlib.pyplot as plt
import numpy as np

def load_image(path: str) -> np.array:
    try:
        img = plt.imread(path)
    except Exception as e:
        print(e)
        exit()
    
    img = plt.imread(path)
    cropped_img = img[:400, :400, :1]
    print(f"The shape of image is: {cropped_img.shape}")
    print(img)
    return cropped_img.tolist()
