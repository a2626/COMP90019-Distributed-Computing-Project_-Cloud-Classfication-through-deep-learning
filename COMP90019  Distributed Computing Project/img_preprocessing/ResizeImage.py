# Author: JIA_NENG CHEN
# USAGE: images Resize under 300kb and add a new method to support the Mac OS file system.
# REFERENCE:https://github.com/ClarkYang91/Computing_Project_90055_Cloud-Classification-Through-Deep-Learning
import cv2
import os
import argparse
import math

parser = argparse.ArgumentParser(description="Input image directory path.")
parser.add_argument("image_path", help="Input image directory path")
args = parser.parse_args()


def resize(file_path, type):
    print(type + ":-- " + file_path)
    origin_size = os.path.getsize(file_path)
    if origin_size >= 210000:
        print(origin_size)
        new_size = math.sqrt(210000/origin_size)
        image = cv2.imread(file_path)
        resized = cv2.resize(image, None, fx=new_size, fy=new_size, interpolation=cv2.INTER_AREA)
        cv2.imwrite(file_path, resized)

#this method is used to ignore some hidden files in the MacOS system, if your system is Windows, you can ignore it.
def listdirInMac(path):
    os_list = os.listdir(path)
    for item in os_list:
        if item.startswith('.') and os.path.isfile(os.path.join(path, item)):
            os_list.remove(item)
    return os_list

#Go through every images in the folder, and resize it to under 300kb
for dir_name in listdirInMac(args.image_path):
       for filename in listdirInMac(args.image_path + "/" + dir_name):
        if filename.endswith(".jpg") or filename.endswith(".JPG"):
            resize(args.image_path + "/" + dir_name + "/" + filename, ".jpg")
        elif filename.endswith(".jpeg") or filename.endswith(".JPEG"):
            resize(args.image_path + "/" + dir_name + "/" + filename, ".jpeg")

