import numpy as np
def read450noise(filename,region):
    catalogue = np.genfromtxt(filename,dtype=None,names=True)
    date_scan = []
    noise     = []
    for eachfile,eachnoise in zip(catalogue['Image'],catalogue['Noise']):
        eachfile = eachfile.decode('utf-8')
        if eachfile.split('_')[0] == region:
            date_scan.append(eachfile.split('_')[-7]+'_'+eachfile.split('_')[-6])
            noise.append(eachnoise)
    return(np.array(date_scan),np.array(noise))
