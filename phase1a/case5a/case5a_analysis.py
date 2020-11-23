"""
PHASE 1A CASE 5A
This python script builds analyzes the tallies from openmc statepoint file
and uses functions in scripts/openmc_analysis.py to analyze and manipulate
the data into what is required for the FHR benchmark.
"""

###############################################################################
#                      Python Package Import
###############################################################################

import openmc
import sys
sys.path.insert(1, '../../scripts/')
from phase1a_constants import *
from openmc_analysis import *

###############################################################################
#                                  Run
###############################################################################
case = 'p1a_5a'
keff = 0.79837
keff_unc = 0.00009

sp = openmc.StatePoint('h5files/9pcm/statepoint.500.h5')
beta_b(sp, case)
# doppler
print(
    reactivity_coefficient_b(
        keff_og=0.79611,
        keff_og_unc=0.00009,
        keff_new=0.79309,
        keff_new_unc=0.00009,
        temp_change=100))
# flibe
print(
    reactivity_coefficient_b(
        keff_og=0.79600,
        keff_og_unc=0.00009,
        keff_new=0.79373,
        keff_new_unc=0.00009,
        temp_change=+100))
# graphite
print(
    reactivity_coefficient_b(
        keff_og=keff,
        keff_og_unc=0.00009,
        keff_new=0.78729,
        keff_new_unc=0.00009,
        temp_change=+50))
fission_density_c(sp, case)
neutron_flux_d(sp, keff, keff_unc, case)
neutron_flux_e(sp, keff, case)
neutron_spectrum_f(sp, case, keff, keff_unc)
