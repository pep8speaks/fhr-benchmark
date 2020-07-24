"""
This python script runs the depletion analysis for case4b of the FHR
benchmark.

"""
###############################################################################
#                      Python Package Import
###############################################################################

import openmc.deplete
import os
import pandas as pd
import sys
sys.path.insert(1, '../../scripts/')
from depletion_analysis import *
from openmc_analysis import *
from phase1b_constants import *

###############################################################################
#                                  Run
###############################################################################

case = 'p1b_c4b'
results = openmc.deplete.ResultsList.from_hdf5(
    "results/depletion_results_100000p.h5")
depletion_keff(results, 'short', case)
burnups = [0, 1, 30, 70]
depletion_fission_density_c(burnups, case, 100000)
depletion_neutron_flux_d(case, 'short', 100000)
depletion_neutron_flux_e(burnups, case, 100000)
depletion_neutron_spectrum_f(burnups, case, 100000)
