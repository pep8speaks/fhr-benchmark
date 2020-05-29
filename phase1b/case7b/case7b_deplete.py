"""
This python script runs the depletion calculation for case4b of the FHR
benchmark.

"""

###############################################################################
#                      Python Package Import
###############################################################################
import openmc.deplete
import numpy as np
import sys
sys.path.insert(1, '../../phase1a/case7a/')
from case7a_build_xml import *
sys.path.insert(1, '../../scripts/')
from phase1b_constants import *

###############################################################################
#                                  Run
###############################################################################
chain_file = "../../data/chain_endfb71_pwr.xml"
chain = openmc.deplete.Chain.from_xml(chain_file)

operator = openmc.deplete.Operator(geom, settings, chain_file)

hmop = operator.heavy_metal
print('hm = ' + str(hmop))

integrator = openmc.deplete.PredictorIntegrator(operator=operator, timesteps=np.diff(bu), timestep_units='Mwd/kg', power=245486.6796001383)
integrator.integrate()

