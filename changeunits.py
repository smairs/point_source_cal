import subprocess
import glob
import os

def changeunits(datadir,wave):
    inputfiles = sorted(glob.glob(datadir+'/*'+wave+'*.sdf'))
    print(inputfiles)
    for eachfile in inputfiles:
        subprocess.call('/stardev/bin/oracdr/src/etc/picard_start.sh -nodisplay -log sf UNCALIBRATE_SCUBA2_DATA '+eachfile,shell=True)
        subprocess.call('/stardev/bin/oracdr/src/etc/picard_start.sh -nodisplay -log sf CALIBRATE_SCUBA2_DATA '+eachfile.split('/')[-1].split('.sdf')[0]+'_uncal.sdf',shell=True)
        os.system('mv '+eachfile.split('/')[-1].split('.sdf')[0]+'_uncal_cal.sdf '+eachfile.split('.sdf')[0]+'_mJybm.sdf')
        os.system('rm -f '+eachfile.split('/')[-1].split('.sdf')[0]+'_uncal.sdf')
