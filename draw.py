import xml, os
from xml.dom import minidom

import cv2, re, math, sys
import numpy as np


colors = np.array(((220, 236, 201), (179, 221, 204), (138, 205, 206), (98, 190, 210), (70, 170, 206), (61, 145, 190), (53, 119, 174), (45, 94, 158), (36, 68, 142)))
colors = colors[:, [2, 1, 0]]
temp = ['265_60_luov_str_walk.txt', '265_60_luov_str_walk_anti.txt', 'VID_20210803_103233.txt', 'VID_20210803_103343.txt', 'VID_20210803_103442.txt', 'VID_20210803_103551.txt']


def draw_micro_block(file, output_path, block_type):
    frame_number = 1
    with open(file, "r") as f:
        cur_file_name = file.split("/")[-1].split(".")[0]
        image = np.zeros((480, 270, 3), np.uint8)
        image.fill(255)
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            line = re.sub(' +', ' ', line)
            res = line.split(" ")
            if os.path.exists(output_path + "/" + cur_file_name + "_" + str(res[-2]) + '.jpg'):
                print(output_path + "/" + cur_file_name + "_" + str(res[-2]) + '.jpg')
                # print("continue")
                continue
            local_x = int(float(res[2])) // 4
            local_y = int(float(res[3])) // 4
            mb_width = int(float(res[4])) // 4
            mb_height = int(float(res[5])) // 4
            mb_type = int(int(res[-1]))
            if mb_type != block_type:
                continue
            else:
                print(res[2], res[3], res[4], res[5])
            color = colors[8 - int(math.log2(mb_width * mb_height)) - 2]
            for j in range(mb_width):
                for k in range(mb_height):
                    image[local_x + j - 4][local_y + k - 4] = color
            if int(res[-2]) != frame_number:
                cv2.imwrite(output_path + "/" + cur_file_name + "_" + str(frame_number) + '.jpg', image)
                frame_number = int(res[-2])
                if not res:
                    break
                image = np.zeros((480, 270, 3), np.uint8)
                image.fill(255)
    print(file + "done!")


if __name__ == "__main__":
    # print(str(sys.argv))
    # sys.argv[1] = "265_60_luov_str_walk.txt"
    # draw_micro_block(sys.argv[1], sys.argv[2])

    # draw_micro_block(r"E:\temp.txt", r"E:\Project\PycharmProjects\pythonProject\output\0", 0)
    draw_micro_block(r"/home/zxc/TC/mtmi0.txt", r"/home/zxc/TC/mtout", 0)
    # draw_micro_block(r"E:\temp.txt", r"E:\Project\PycharmProjects\pythonProject\output\1", 1)
    # draw_micro_block(r"E:\temp.txt", r"E:\Project\PycharmProjects\pythonProject\output\3", 3)
    # draw_micro_block(r"E:\Project\PycharmProjects\pythonProject\temp.txt", r"E:\Project\PycharmProjects\pythonProject\output\debug", 0)


