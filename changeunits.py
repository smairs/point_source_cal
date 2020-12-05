import subprocess
import glob
import os

def changeunits(datadir,wave):
    inputfiles = sorted(glob.glob(datadir+'/*'+wave+'*.sdf'))
    for eachfile in inputfiles:
        subprocess.call('/stardev/bin/oracdr/src/etc/picard_start.sh -nodisplay -log sf CALIBRATE_SCUBA2_DATA '+eachfile,shell=True)
        os.system('mv '+eachfile.split('/')[-1].split('.sdf')[0]+'_uncal_cal.sdf '+eachfile.split('.sdf')[0]+'_mJybm.sdf')
