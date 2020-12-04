import numpy as np
from TCTriggerPS.TCTriggerPS import TCTrigger
import os
import glob

def make_coadds_metadata(region,datadir,wave):
    '''
    :param region: String representation of the Transient Field name of interest
    '''
    sdffiles = sorted(glob.glob(datadir+'/*'+wave+'*sm.sdf'))

    if wave == '450':
        TCTrigger(sdffiles,'config/protocat.txt','config/diskcat.txt',region,aperture_diam = 0.0005555555,trigger_thresh = 4, brightness_thresh = 0.0, sd_thresh = 2,wave=wave)
    else:
        TCTrigger(sdffiles,'config/protocat.txt','config/diskcat.txt',region,aperture_diam = 0.0008333333,trigger_thresh = 5, brightness_thresh = 0.0, sd_thresh = 2,wave=wave)

