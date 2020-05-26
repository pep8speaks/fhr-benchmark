from pyne import data
import pandas as pd
import numpy as np


def reactor_power(sp_power, particles):
    """Returns the FHR's power 

    Parameters
    ----------
    sp_power: float 
        specific power of reactor [W/gU]
    particles: int 
        number of triso particles in each fuel stripes's y-direction

    Returns
    -------
    t_u: float 
        mass of Uranium [metric tonnes]
    power: float 
        power of reactor [W]
    """

    wtp_u = ((0.00227325*data.atomic_mass('U235'))+ \
            (0.02269476*data.atomic_mass('U238')))/ \
            (0.00227325*data.atomic_mass('U235')+ \
             0.02269476*data.atomic_mass('U238')+ \
             0.03561871*data.atomic_mass('O16') + 
             0.00979714*data.atomic_mass('C0'))*100 #%
    V = (101 * 210 * particles * 36 * 4/3 * np.pi * (2135e-5)**3) #cm3
    density = 11 #g/cc
    grams_u = V * density * (wtp_u) / 100 #gU
    t_u = grams_u * 1e-6 #t
    power = grams_u * sp_power # W

    return t_u, power 


def atoms_to_prel(nuclides_type,hmop): 
    if nuclides_type not in  ['actinides','fission_products','extended_list']:
        raise Exception('Types allowed: actinides, fission_products or extended_list.')
    df =  pd.read_csv('depletion_analysis/'+nuclides_type+'_preconv.csv',index_col=0)
    avo = 6.0221409e+23
    #hmop = 1227.4327087024026e-6 #tHM
    nuclides = list(df.columns.values)
    for a in range(len(nuclides)): 
        nuclide = nuclides[a]
        if nuclide == 'Am242_m1':
            amu = data.atomic_mass('Am242m')
        elif nuclide == 'Ag110_m1': 
            amu = data.atomic_mass('Ag110m')
        else: 
            amu = data.atomic_mass(nuclide)
        prel = df[nuclide] * amu / avo / hmop 
        df[nuclide] = prel
    df = df.transpose()
    df.to_csv('depletion_analysis/'+nuclides_type+'.csv')
    return 
