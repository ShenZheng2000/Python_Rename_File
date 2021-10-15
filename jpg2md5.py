# Purpose: Rename jpg file name to its md5.

import os
import hashlib

path_name='/share_data_node65/users/zhengshen/12585/gr_b_20210913_germany_demo_p_1c2/'

for item in os.listdir(path_name):
    if not item.endswith(".jpg"):
        continue
    old_name = os.path.join(path_name, item)
    image_md5 = hashlib.md5(open(old_name, 'rb').read()).hexdigest()
    new_name = os.path.join(path_name, (image_md5 +'.jpg'))
    os.rename(old_name, new_name)
