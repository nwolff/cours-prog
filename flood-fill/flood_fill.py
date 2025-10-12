import time

import matplotlib.pyplot as plt
import numpy as np
from skimage.draw import disk, rectangle


def display_image(image, title="Flood Fill Progress"):
    plt.imshow(image, cmap="gray", vmin=0, vmax=1)
    plt.title(title)
    plt.axis("off")
    plt.show(block=False)
    plt.pause(0.001)
    plt.clf()


border_color = 1


def flood_fill(image, start_coords, target_color=0.4):
    height, width = image.shape
    x, y = start_coords
    original_color = image[x, y]  # We detect this automatically

    todo = {(x, y)}

    def mark(x, y):
        if (0 <= x < width) and (0 <= y < height):
            if image[x, y] == original_color:
                todo.add((x, y))
                image[x, y] = border_color

    round = 0
    while todo:
        x, y = todo.pop()

        if image[x, y] in (original_color, border_color):
            image[x, y] = target_color

            # Add neighboring pixels
            mark(x + 1, y)
            mark(x, y + 1)
            mark(x - 1, y)
            mark(x, y - 1)

        # For visualization
        round += 1
        if round % 100 == 0:
            display_image(image)

    return image


def create_complex_image(shape=(200, 200)):
    img = np.zeros(shape)

    # Add rectangles
    rr, cc = rectangle(start=(20, 20), extent=(60, 40), shape=img.shape)
    img[rr, cc] = 1

    rr, cc = rectangle(start=(100, 50), extent=(50, 100), shape=img.shape)
    img[rr, cc] = 1

    # Add circles
    rr, cc = disk((50, 150), 20, shape=img.shape)
    img[rr, cc] = 1

    rr, cc = disk((150, 150), 30, shape=img.shape)
    img[rr, cc] = 1

    # Punch some holes (black spots)
    rr, cc = disk((50, 150), 10, shape=img.shape)
    img[rr, cc] = 0

    rr, cc = rectangle(start=(110, 60), extent=(20, 20), shape=img.shape)
    img[rr, cc] = 0

    return img


def create_simple_image():
    # Create a black and white image (0 = black, 1 = white)
    img = np.zeros((100, 100))
    img[20:80, 20:80] = 1  # White square in the middle
    return img


# Example usage
if __name__ == "__main__":
    img = create_complex_image()

    # Make a "hole" in the square
    img[40:60, 40:60] = 0

    display_image(img, title="Original Image")
    time.sleep(1)

    # Start flood fill inside the hole
    filled_image = flood_fill(img, start_coords=(50, 50))

    display_image(filled_image, title="Flood Fill Complete")
    time.sleep(100)
