import numpy as np
import cv2
from colorama import Fore, Style

# def negative_range_to_percentage()

def check_img(matching_image_name: str):
    img = cv2.imread(matching_image_name, 0)

    print("\nChecking", matching_image_name)

    corr = cv2.matchTemplate(template_img, img, cv2.TM_CCOEFF_NORMED)[0][0]
    print("corr:", corr)
    # print("correlation: %.2f%%" % (50 * (corr + 1)))

    res = cv2.matchTemplate(img, template_img, cv2.TM_CCOEFF_NORMED)


    corr2 = np.amax(res)
    print("corr2:", corr2)
    if corr2 > 0.4:
        print(f"{Fore.GREEN}PASS")
    else:
        print(f"{Fore.RED}FAIL")
    print(Style.RESET_ALL)


if __name__ == '__main__':
    template_img = cv2.imread('image/template.png', 0)
    image_list = [
        'russian-flag.png',
        'img2.png',
        'us_black.png',
        'template-copy.png',
        'img2.png',
        'soldier.jpg'
    ]

    for image in image_list:
        check_img(f"image/{image}")
