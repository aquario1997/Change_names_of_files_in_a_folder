import os
import datetime
import re
import time

"""Rename all the files in a folder (which does not have any subfolders) with current time with a milli second gap"""
"""First change the working directory to the required directory using os.chdir()"""
for file in os.listdir():
    if not os.path.isdir(file):
        regex = r'(.*)(\.\w+)$'
        time.sleep(0.001)
        timenow = str(datetime.datetime.today())
        timenow = re.sub(':', '-', timenow)
        new_name = re.sub(regex, timenow+'\\2', file)
        os.rename(file, new_name)
