import numpy as np
from TCTrigger import *
import os
import glob

def make_coadds_metadata(region,wave):
    '''
    :param region: String representation of the Transient Field name of interest
    '''
    sdffiles = sorted(glob.glob('*.sdf'))

    TCTrigger(sdffiles,'config/protocat.txt','config/diskcat.txt',region,aperture_diam = 0.0005555555,trigger_thresh = 4, brightness_thresh = 0.0, sd_thresh = 2,wave=wave)

