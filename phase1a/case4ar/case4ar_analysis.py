"""
PHASE 1A CASE 4AR
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
case = 'p1a_4ar'
keff = 0.83437  # 0.83771
keff_unc = 0.00009  # 0.00003

sp = openmc.StatePoint('h5files/9pcm/statepoint.500.h5')

beta_b(sp, case)
# doppler
print(
    reactivity_coefficient_b(
        keff_og=0.83584,
        keff_og_unc=0.00010,
        keff_new=0.83250,
        keff_new_unc=0.00010,
        temp_change=+100))
# flibe
print(
    reactivity_coefficient_b(
        keff_og=0.83474,
        keff_og_unc=0.00010,
        keff_new=0.83376,
        keff_new_unc=0.00010,
        temp_change=+100))
# graphite
print(
    reactivity_coefficient_b(
        keff_og=0.83798,
        keff_og_unc=0.00010,
        keff_new=0.83080,
        keff_new_unc=0.00009,
        temp_change=+100))
# fission_density_c(sp,case)
# neutron_flux_d(sp,keff,keff_unc,case)
# neutron_flux_e(sp,keff,case)
# neutron_spectrum_f(sp,case,keff,keff_unc)
