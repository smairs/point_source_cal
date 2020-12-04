from starlink import kappa
import glob

def smooth_input_data(datadir,wave):
    inputfiles = sorted(glob.glob(datadir+'/*'+wave+'*ACcal.sdf'))
    for eachfile in inputfiles;
        kappa.gausmooth(eachfile,eachfile.split('.sdf')[0]+'_sm.sdf',2)
