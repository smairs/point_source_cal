from starlink import kappa
import glob

def smooth_input_data(datadir,wave):
    inputfiles = sorted(glob.glob(datadir+'/*'+wave+'*mJybm.sdf'))
    for eachfile in inputfiles:
        kappa.gausmooth(eachfile,eachfile.split('.sdf')[0]+'sm.sdf',2)
