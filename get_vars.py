import numpy as np
import pickle


def get_vars(region):
    if region == 'IC348':
        known_vars = [1]
        var_names  = ['IC 348 1']
    if region == 'NGC1333':
        known_vars = [0,10]
        var_names  = ['IRAS 4A','BOLO 40']
    if region == 'NGC2024':
        known_vars = []
        var_names  = []
    if region == 'NGC2071':
        known_vars = [1,2]
        var_names  = ['HOPS 358','HOPS 373']
    if region == 'OMC23':
        known_vars = [1,12,29,100]
        var_names  = ['HOPS 88','HOPS 370','HOPS 383','V1017 ORI']
    if region == 'OPHCORE':
        known_vars = [9]
        var_names  = ['OPH 162624']
    if region == 'SERPM':
        known_vars = [0,10,11]
        var_names  = ['SMM 1','EC 53','SMM 10']
    if region == 'SERPS':
        known_vars = [12]
        var_names  = ['IRAS 18270']
    if region == 'DR21C':
        known_vars = []
        var_names = []
    return(known_vars,var_names)
