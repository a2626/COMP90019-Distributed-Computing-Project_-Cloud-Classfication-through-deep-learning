# AUTHOR: JIA-NENG CHEN
# REFERENCE:https://github.com/ClarkYang91/Computing_Project_90055_Cloud-Classification-Through-Deep-Learning
# Following his way to collect data, and add a new BaiduCrawler to further collect images from chinese resources

from icrawler.builtin import BaiduImageCrawler, GoogleImageCrawler
import os

## Specify where you want to save your images
image_path = "SPECIFY PATH HERE "

## First one is CHINESE version of clouds list, it use to collect images from Baidu. Another one use to collect images from google
CloudTypesList_CHINESE = open('ColudListBaidu.txt', 'r')
CloudTypesList_ENG = open('ColudListBaidu.txt', 'r')

## this one is Baidu crawller
for cloudTypesName in CloudTypesList_CHINESE:
    cloud_type = cloudTypesName.strip('\n')

    imageDir = image_path + "\\" + cloud_type
    if not os.path.isdir(imageDir):
        os.mkdir(imageDir)
    print("imageDir--------------" + imageDir)

    baidu_crawler = BaiduImageCrawler(parser_threads=2,
                                      downloader_threads=4,
                                      storage={'root_dir': imageDir})
    baidu_crawler.crawl(keyword=cloud_type,
                        max_num=1000,file_idx_offset='auto')

## this one is GOOGLE crawller
for cloudTypesName in CloudTypesList_ENG:
    cloud_type = cloudTypesName.strip('\n')

    imageDir = image_path + "\\" + cloud_type
    if not os.path.isdir(imageDir):
        os.mkdir(imageDir)
    print("imageDir--------------" + imageDir)

    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': imageDir})
    google_crawler.crawl(
        keyword=cloud_type,
        filters={'date': ((2010, 1, 1), (2019, 1, 1))},
        max_num=1000,
        file_idx_offset=0)
    
    google_crawler.crawl(
        keyword=cloud_type,
        filters={'date': ((2003, 1, 1), (2009, 12, 31))},
        max_num=1000,
        file_idx_offset='auto')

print("Image Collection is done")
