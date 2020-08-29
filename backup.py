import os
from datetime import date, timedelta
import re
import shutil

import constants

SRC_DIR = constants.SRC_DIR
DEST_DIR = constants.DEST_DIR

DAYS = constants.DAYS
dates = [str(date.today() - timedelta(days=day)) for day in range(DAYS)]

for cur_date in dates:
    dest = os.path.join(DEST_DIR, cur_date)
    if os.path.isdir(dest) == False:
        os.mkdir(dest)
    for dir in os.listdir(SRC_DIR):
        src = os.path.join(SRC_DIR, dir)
        for sub_dir in os.listdir(src):
            if re.search(f'^{cur_date}$', str(sub_dir)):
                src = os.path.join(SRC_DIR, dir, cur_date)
                dest = os.path.join(DEST_DIR, cur_date, dir)
                print(src, dest)
                shutil.copytree(src, dest)
    dest = src = os.path.join(DEST_DIR, cur_date)
    shutil.make_archive(dest, 'zip', src)
    shutil.rmtree(src)

