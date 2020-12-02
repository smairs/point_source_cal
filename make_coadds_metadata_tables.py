import numpy as np
from TCTrigger import *
import os
import glob

region = 'IC348'

sdffiles = sorted(glob.glob('*.sdf'))

TCTrigger(sdffiles,'/export/data/smairs/smairs_github/450_calibration_test/config/protocat.txt','/export/data/smairs/smairs_github/450_calibration_test/config/diskcat.txt',region,aperture_diam = 0.0005555555,trigger_thresh = 4, brightness_thresh = 0.0, sd_thresh = 2,wave='450')

