# REFERENCE: https://stackoverflow.com/questions/11310220/why-am-i-getting-the-error-not-a-jpeg-file-starts-with-0x89-0x50/37277735#37277735
# USAGE: CHECK images encoding

import glob
import os
import re
import logging
import traceback

#Specify folder that you would like to examine.
filelist = glob.glob("/Users/lucsas/graduate_project/project/img/9/*.jpg")
for file_obj in filelist:
    try:
        print(file_obj)
        jpg_str = os.popen("file \"" + str(file_obj) + "\"").read()
        if (re.search('PNG image data', jpg_str, re.IGNORECASE)) or (re.search('Png patch', jpg_str, re.IGNORECASE)):
            print("Deleting jpg as it contains png encoding - " + str(file_obj))
            os.system("rm \"" + str(file_obj) + "\"")
    except Exception as e:
        logging.error(traceback.format_exc())
print("Cleaning jps done")
