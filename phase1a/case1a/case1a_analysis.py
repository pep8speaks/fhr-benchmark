"""
PHASE 1A CASE 1A
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
case = 'p1a_c1a'
keff = 1.39389
keff_unc = 0.00010

sp = openmc.StatePoint('h5files/10pcm/statepoint.500.h5')
beta_b(sp, case)
# doppler
print(
    reactivity_coefficient_b(
        keff_og=keff,
        keff_og_unc=keff_unc,
        keff_new=1.39607,
        keff_new_unc=0.00010,
        temp_change=-50))
# flibe
print(
    reactivity_coefficient_b(
        keff_og=keff,
        keff_og_unc=keff_unc,
        keff_new=1.39374,
        keff_new_unc=0.00011,
        temp_change=+50))
# graphite
print(
    reactivity_coefficient_b(
        keff_og=keff,
        keff_og_unc=keff_unc,
        keff_new=1.39323,
        keff_new_unc=0.00010,
        temp_change=+50))

#fission_density_c(sp, case)
#neutron_flux_d(sp, keff, keff_unc, case)
#neutron_flux_e(sp, keff, case)
#neutron_spectrum_f(sp, case, keff, keff_unc)
