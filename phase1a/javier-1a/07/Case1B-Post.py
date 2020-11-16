"""
*******************************************************************************
*                                                                             
*  Results of FHR Benchmarck Case 1B                                          
*                                                                             
*******************************************************************************  
"""

# ====================== LIBRARIES ============================================

import openmc
import openmc.deplete
import matplotlib.pyplot as plt

# ====================== DATA PROCESSING ======================================

print()
print('Running post-processing...')

#--- Reading results & defining burnup steps
results = openmc.deplete.ResultsList.from_hdf5('depletion_results.h5')
burnsteps = [0, 0.1,  0.5, 1, 2, 4, 6, 8, 10, 14, 18, 22, 26, 30, 40, 50, 60, 70]

#----- Getting eigenvalues
time, k = results.get_eigenvalue()

#----- Getting number of atomes per nuclide
time, U235  = results.get_atoms("1", "U235")
time, U238  = results.get_atoms("1", "U238")
time, Pu239  = results.get_atoms("1", "Pu239")

#----- Plotting eigenvalues
plt.figure(1)
plt.scatter(burnsteps, k[:, 0])
plt.xlabel("Burnup [MWd/kg]")
plt.ylabel("$k_{eff}$")
plt.grid(linestyle='dashed', color='gray')
plt.tight_layout()

#----- Plotting time variation of atomic density
plt.figure(2)
plt.scatter(burnsteps, U235/(61.63668*(10**24)))
plt.xlabel("Burnup [MWd/kg]")
plt.ylabel("Isotopic composition of U235 [atoms/b-cm]")
plt.grid(linestyle='dashed', color='gray')
plt.tight_layout()
plt.legend(loc='best')

plt.figure(3)
plt.scatter(burnsteps, U238/(61.63668*(10**24)))
plt.xlabel("Burnup [MWd/kg]")
plt.ylabel("Isotopic composition of U238 [atoms/b-cm]")
plt.grid(linestyle='dashed', color='gray')
plt.tight_layout()
plt.legend(loc='best')

plt.figure(4)
plt.scatter(burnsteps, Pu239/(61.63668*(10**24)))
plt.xlabel("Burnup [MWd/kg]")
plt.ylabel("Isotopic composition of Pu239 [atoms/b-cm]")
plt.grid(linestyle='dashed', color='gray')
plt.tight_layout()
plt.legend(loc='best')

print('Post-processing finished...')