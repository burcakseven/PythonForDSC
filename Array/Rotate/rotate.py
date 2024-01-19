from load_image import load_image
import matplotlib.pyplot as plt
import numpy as np

def rotate(path: str):
    img = load_image(path)
    plt.imshow(img)
    plt.show()
    img_t= (list(zip(*img)))
    print(f"New shape after Transpose: {np.shape(img_t)}")
    plt.imshow(img_t)
    plt.show()
    print(img_t)

def main():
    rotate("animal.jpeg")

if __name__ == "__main__":
    main()