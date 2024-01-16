import numpy as np
import cv2


pos_start = [280, 508]
pos_adder = [240, 190]
pos_limit = [5, 4]

f = np.zeros(pos_limit)

# 像素标识
"""
向日葵 -> 26 72 154
豌豆射手 -> 22 172 166
寒冰射手 -> 159 173 86
> 检测背景 不准确
地刺 -> 76 75 15
"""


# (1440, 2560, 3)
def read_image(imn, imp='./example_images/'):
    image = cv2.imread(imp + imn)
    return image


def inference_formation(image):
    for h_l in range(pos_limit[0]):
        h = pos_start[0] + h_l * pos_adder[0]
        for w_l in range(pos_limit[1]):
            w = pos_start[1] + w_l * pos_adder[1]
            b, g, r = image[h: h+1, w: w+1][0][0]
            if b < 40:
                if g < 100:
                    f[h_l][w_l] = 1
                else:
                    f[h_l][w_l] = 2
            elif b > 120 and r > 50:
                f[h_l][w_l] = 3
            else:
                f[h_l][w_l] = 4


def draw_point_in_position(image, r=0):
    for h_l in range(pos_limit[0]):
        h = pos_start[0] + h_l * pos_adder[0]
        for w_l in range(pos_limit[1]):
            w = pos_start[1] + w_l * pos_adder[1]
            if h_l == 0:
                print(image[h-r: h+r+1, w-r: w+r+1])
            image[h-r: h+r+1, w-r: w+r+1] = [0, 0, 255]
    cv2.imshow('', image)
    cv2.waitKey()
    cv2.destroyAllWindows()


image = read_image('pvz_1.png')
# draw_point_in_position(image)
inference_formation(image)
print(f)

# accuracy: 100%

  