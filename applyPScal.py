import numpy as np
import pickle
from starlink import kappa

def applyPScal(imagelist,wave,target_uncertainties):

    region = imagelist[0].split('/')[-1].split('_')[0]
    target_uncertainty_key = str(int(100*target_uncertainties[0]))

    #Get calibration factors
    calinfo = pickle.load(open('pointsource_results/'+region+'/'+region+'_PointSource_cal_info_dict_targunc'+target_uncertainty_key+'_'+wave+'.pickle','rb'))

    for eachimage in imagelist:
        date_scan = eachimage.split('/')[-1].split('_')[1]+'_'+eachimage.split('/')[-1].split('_')[2]
        calfactor = np.array(calinfo['RelFCFs'])[np.where(calinfo['datescans']==date_scan)]
        kappa.cdiv(eachimage,calfactor[0],eachimage.split('.sdf')[0]+'_PScal.sdf')
        
    
