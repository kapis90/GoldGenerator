import os
import re
from shutil import copyfile

#Looking for test dirs. Can be filtered by regexp
test_names = [test for test in os.listdir(os.getcwd()) if re.search("BGA_color_map_exception.*",test)]
#Pattern file used as source for gold files
source = r'C:\Users\kkoltons\Documents\running_xPD_test\automation\clean_with_padstack\PKG\LogFiles\AIFImport.txt'

#Path to refs directory
dst_dir = r'C:/Users/kkoltons/Documents/running_xPD_test/automation/refs/'

GF_ABREV = "messages"

def copy_golds(source, dst_dir, GF_ABREV, test_names):

    for test_name in test_names:
        copyfile(source, dst_dir + GF_ABREV + "." + test_name + ".gold")


copy_golds(source, dst_dir, GF_ABREV, test_names)