from colorama import Fore, Style
import cv2
import numpy as np
from os import walk

IMAGE_DIR = './image'
TEMPLATE_IMAGE = IMAGE_DIR + '/' + 'template.png'


# Turn a value from a range of [-1, 1] into a percentage string,
# with colors indicating a pass or fail
def range_to_percent_pretty(value: float) -> str:
    percentage_val = (50 * (value + 1))
    return "%s%.2f%%%s" % (
        (Fore.GREEN if percentage_val >= 50 else Fore.RED),
        percentage_val,
        Style.RESET_ALL
    )


# Check if a given image file name is similar to or different to the original
def check_img(matching_image_name: str):
    img = cv2.imread(matching_image_name, 0)

    print("\nChecking", matching_image_name)

    res = cv2.matchTemplate(template_img, img, cv2.TM_CCOEFF_NORMED)

    corr = res[0][0]
    print("corr:", range_to_percent_pretty(corr))

    corr2 = np.amax(res)
    print("corr2:", range_to_percent_pretty(corr2))
    if corr2 > 0.4:
        print(Fore.GREEN + "PASS")
    else:
        print(Fore.RED + "FAIL")
    print(Style.RESET_ALL, end='')


if __name__ == '__main__':
    # Open the template image
    template_img = cv2.imread(TEMPLATE_IMAGE, 0)

    # A list of files in the image directory
    (_, _, image_list) = next(walk(IMAGE_DIR))

    print(f"Scanning through {image_list}")

    # Check the correlation of each image in the list
    for image in image_list:
        check_img(f"{IMAGE_DIR}/{image}")
