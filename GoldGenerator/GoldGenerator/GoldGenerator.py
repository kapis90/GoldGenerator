import os
import re
from shutil import copyfile
#Looking for test dirs. Can be filtered by regexp
test_names = [test for test in os.listdir(os.getcwd()) if re.search("BGA_color_map.*",test)]

#Pattern file used as source for gold files
pattern = r'C:/Users/kkoltons/Documents/xPD_trunk/_Sprint_common_core/automation/refs/bgacolormap.BGA_color_map_WARPX_1200.gold'

#Path to refs directory
dst_dir = r'C:/Users/kkoltons/Documents/running_xPD_test/automation/refs/'

GF_ABREV = "bgacolormap"

def copy_golds(dst_dir, GF_ABREV):
    for test_name in test_names:
        copyfile(pattern, dst_dir + GF_ABREV + "." + test_name +".gold")