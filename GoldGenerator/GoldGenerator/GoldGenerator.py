import os
import re
from shutil import copyfile

test_names = [a for a in os.listdir(os.getcwd()) if re.search("BGA_color_map.*",a)]

pattern = r'C:/Users/kkoltons/Documents/xPD_trunk/_Sprint_common_core/automation/refs/bgacolormap.BGA_color_map_WARPX_1200.gold'

dst_dir = r'C:/Users/kkoltons/Documents/running_xPD_test/automation/refs/'

for test_name in test_names:
	copyfile(pattern, dst_dir + "bgacolormap." + test_name +".gold")