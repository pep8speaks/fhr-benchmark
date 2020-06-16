""" Constants and functions for FHR benchmark depletion

This script contains the values for constants and functions used to 
set up the FHR benchmark depletion. 

"""

import numpy as np
import openmc

###############################################################################
#                               Constants 
###############################################################################
bu = np.array([0, 0.1,0.5, 1, 2, 4, 6, 8, 10, 12, 14, 
               16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 
               36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 
               56, 58, 60, 62, 64, 66, 68, 70]) #Gwd/tU cumu
bu_7b = np.array([0, 0.1,0.5, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 
               20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 
               42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 
               64, 66, 68, 70, 72, 74, 76, 78, 80, 82,
               84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 
               106, 108, 110, 112, 114, 116, 118, 120, 122, 124,
               126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 
               146, 148, 150, 152, 154, 156, 158, 160]) #Gwd/tU cumu
BUs_sheet = [0, 0.1,0.5,1,2,4,6,8,10,14,18,22,26,30,
             40,50,60,70,80,90,100,120,140,160] # burnups required by fhr benchmark
actinides = ['U235','U238','Pu239','Pu240','Pu241','Pu242','Pu243',
             'Pu244','Am241','Am242_m1','Am243','Cm242','Cm243',
             'Cm244','Cm245']
fp = ['Kr85','Sr90','Ag110_m1','Cs137','Xe135','Sm149','Sm151']
extended_list = ['U232','U233','U234','U235','U236','U238','Np236','Np237',
               'Pu236','Pu238','Pu239','Pu240','Pu241','Pu242','Pu243',
               'Pu244','Am241','Am242_m1','Am243','Cm242','Cm243','Cm244',
               'Cm245','Cm246','Cm247','Cm248','Ra226','Ra228','Ac227',
               'Th229','Th230','Th232','Cf252']
europium = ['Eu151','Eu153']