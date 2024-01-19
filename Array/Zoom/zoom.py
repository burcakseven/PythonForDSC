import matplotlib.pyplot as plt
from load_image import load_image

def zoom(path):
    img = load_image(path)
    print(img)
    cropped_img = img[:400, :400, :1]
    plt.imshow(cropped_img)
    print(f"New shape after slicing: {cropped_img.shape}")
    plt.show()
    return cropped_img

def main():
    print(zoom("animal.jpeg"))

if __name__ == "__main__":
    main()