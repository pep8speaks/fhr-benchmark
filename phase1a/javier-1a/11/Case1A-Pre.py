"""
*******************************************************************************
*                                                                             
*        Model: FHR Fuel Element                                                    
*   Created by: Javier Gonzalez   
*         Case: 1A
*  Assumptions: No burnable poison (BP) & control rods (CR) out                                              
*                                                                             
*******************************************************************************  
"""

#==============================================================================
#                         LIBRARIES 
#==============================================================================

import openmc
import numpy as np
#from PIL import Image
from math import sqrt
#import matplotlib.pyplot as plt
import pandas as pd

#==============================================================================
#                         MATERIALS 
#==============================================================================

#----- Uranium Oxycarbide (Enrichment 9%)
uoxy = openmc.Material(material_id=1, name='Uranium Oxycarbide')
uoxy.add_nuclide('U235', 2.27325E-3, percent_type='ao')
uoxy.add_nuclide('U238', 2.269476E-2, percent_type='ao')
uoxy.add_nuclide('O16', 3.561871E-2, percent_type='ao')
uoxy.add_nuclide('C0', 9.79714E-3, percent_type='ao')
uoxy.set_density('atom/b-cm', 7.038386E-2)
#uoxy.set_density('g/cm3', 11.0)
uoxy.temperature = 1110

#----- Porous Carbon
pcarbon = openmc.Material(material_id=2, name='Porous Carbon')
pcarbon.add_nuclide('C0', 5.013980E-2)
pcarbon.set_density('atom/b-cm', 5.013980E-2)
#pcarbon.set_density('g/cm3', 1.0)
pcarbon.add_s_alpha_beta('c_Graphite')
pcarbon.temperature = 948

#----- Silicon Carbide
SiC = openmc.Material(material_id=3, name='Silicon Carbide')
SiC.add_nuclide('Si28', 4.431240E-2, percent_type='ao')
SiC.add_nuclide('Si29', 2.25887E-3, percent_type='ao')
SiC.add_nuclide('Si30', 1.48990E-3, percent_type='ao')
SiC.add_nuclide('C0', 4.806117E-2, percent_type='ao')
SiC.set_density('atom/b-cm', 9.612234E-2)
#SiC.set_density('g/cm3', 3.2)
SiC.temperature = 948

#----- Graphite
graphite = openmc.Material(material_id=4, name='Graphite')
graphite.add_nuclide('C0', 9.025164E-2, percent_type='ao')
#graphite.set_density('atom/b-cm', 9.025164E-2)
graphite.set_density('g/cm3', 1.8)
graphite.add_s_alpha_beta('c_Graphite')
graphite.temperature = 948

#----- FLiBe Coolant
flibe = openmc.Material(material_id=5, name='FLiBe')
flibe.add_nuclide('Li6', 1.383014E-6, percent_type='ao')
flibe.add_nuclide('Li7', 2.37132E-2, percent_type='ao')
flibe.add_nuclide('Be9', 1.18573E-2, percent_type='ao')
flibe.add_nuclide('F19', 4.74291E-2, percent_type='ao')
flibe.set_density('atom/b-cm', 8.30097E-2)
#flibe.set_density('g/cm3', 1.95)
flibe.temperature = 948

#----- Materials collection & Nuclear Data
materials = openmc.Materials([uoxy, pcarbon, SiC, graphite, flibe])
#materials.cross_sections = '/home/javier/Documents/OpenMC/DataENDF-7.1/cross_sections.xml'
#materials.cross_sections = '/home/gonzaj10/simulations/DataENDF-7.1/cross_sections.xml'

#----- Export to "materials.xml"
materials.export_to_xml()

#==============================================================================
#                         GEOMETRY 
#==============================================================================

#********************** Regions **********************

#----- Plantes in X axis
px01 = openmc.XPlane(surface_id=101, x0=-10.38)

px02 = openmc.XPlane(surface_id=102, x0=-21.7382)
px03 = openmc.XPlane(surface_id=103, x0=-2.27959)
px04 = openmc.XPlane(surface_id=104, x0=-20.2659)
px05 = openmc.XPlane(surface_id=105, x0=-0.807345)

px06 = openmc.XPlane(surface_id=106, x0=-19.8618)
px07 = openmc.XPlane(surface_id=107, x0=-0.4032)
px08 = openmc.XPlane(surface_id=108, x0=-18.3896)
px09 = openmc.XPlane(surface_id=109, x0=1.06904)

px10 = openmc.XPlane(surface_id=110, x0=-17.9854)
px11 = openmc.XPlane(surface_id=111, x0=1.47319)
px12 = openmc.XPlane(surface_id=112, x0=-16.5132)
px13 = openmc.XPlane(surface_id=113, x0=2.94543)

px14 = openmc.XPlane(surface_id=114, x0=-16.109)
px15 = openmc.XPlane(surface_id=115, x0=3.34958)
px16 = openmc.XPlane(surface_id=116, x0=-14.6368)
px17 = openmc.XPlane(surface_id=117, x0=4.82182)

px18 = openmc.XPlane(surface_id=118, x0=-14.2326)
px19 = openmc.XPlane(surface_id=119, x0=5.22597)
px20 = openmc.XPlane(surface_id=120, x0=-12.7604)
px21 = openmc.XPlane(surface_id=121, x0=6.69821)

px22 = openmc.XPlane(surface_id=122, x0=-12.3562)
px23 = openmc.XPlane(surface_id=123, x0=7.10235)
px24 = openmc.XPlane(surface_id=124, x0=-10.884)
px25 = openmc.XPlane(surface_id=125, x0=8.5746)

pxmin = openmc.XPlane(surface_id=126, x0 = -9.7293)
pxmax = openmc.XPlane(surface_id=127, x0 =  9.7293)

#----- Plantes in Y axis
py01 = openmc.YPlane(surface_id=201, y0=0.0)
py02 = openmc.YPlane(surface_id=202, y0=-0.88)
py03 = openmc.YPlane(surface_id=203, y0=-2.0)

py04 = openmc.YPlane(surface_id=204, y0=-2.35)
py05 = openmc.YPlane(surface_id=205, y0=-2.45)
py06 = openmc.YPlane(surface_id=206, y0=-2.82064)
py07 = openmc.YPlane(surface_id=207, y0=-4.42936)
py08 = openmc.YPlane(surface_id=208, y0=-4.8)
py09 = openmc.YPlane(surface_id=209, y0=-4.9)

py10 = openmc.YPlane(surface_id=210, y0=-5.6)
py11 = openmc.YPlane(surface_id=211, y0=-5.7)
py12 = openmc.YPlane(surface_id=212, y0=-6.07064)
py13 = openmc.YPlane(surface_id=213, y0=-7.67936)
py14 = openmc.YPlane(surface_id=214, y0=-8.05)
py15 = openmc.YPlane(surface_id=215, y0=-8.15)

py16 = openmc.YPlane(surface_id=216, y0=-8.85)
py17 = openmc.YPlane(surface_id=217, y0=-8.95)
py18 = openmc.YPlane(surface_id=218, y0=-9.32064)
py19 = openmc.YPlane(surface_id=219, y0=-10.92936)
py20 = openmc.YPlane(surface_id=220, y0=-11.3)
py21 = openmc.YPlane(surface_id=221, y0=-11.4)

py22 = openmc.YPlane(surface_id=222, y0=-12.1)
py23 = openmc.YPlane(surface_id=223, y0=-12.2)
py24 = openmc.YPlane(surface_id=224, y0=-12.57064)
py25 = openmc.YPlane(surface_id=225, y0=-14.17936)
py26 = openmc.YPlane(surface_id=226, y0=-14.55)
py27 = openmc.YPlane(surface_id=227, y0=-14.65)

py28 = openmc.YPlane(surface_id=228, y0=-15.35)
py29 = openmc.YPlane(surface_id=229, y0=-15.45)
py30 = openmc.YPlane(surface_id=230, y0=-15.82064)
py31 = openmc.YPlane(surface_id=231, y0=-17.42936)
py32 = openmc.YPlane(surface_id=232, y0=-17.8)
py33 = openmc.YPlane(surface_id=233, y0=-17.9)

py34 = openmc.YPlane(surface_id=234, y0=-18.6)
py35 = openmc.YPlane(surface_id=235, y0=-18.7)
py36 = openmc.YPlane(surface_id=236, y0=-19.07064)
py37 = openmc.YPlane(surface_id=237, y0=-20.67936)
py38 = openmc.YPlane(surface_id=238, y0=-21.05)
py39 = openmc.YPlane(surface_id=239, y0=-21.15)

py40 = openmc.YPlane(surface_id=240, y0=-21.50)
py41 = openmc.YPlane(surface_id=241, y0=-22.50)
py42 = openmc.YPlane(surface_id=242, y0=-23.40)
py43 = openmc.YPlane(surface_id=249, y0=23.40)

pymin = openmc.YPlane(surface_id=244, y0 = -0.18532)
pymax = openmc.YPlane(surface_id=245, y0 =  0.18532)

#----- Plantes in Z axis
pz01 = openmc.ZPlane(surface_id=301, z0=-0.04633)
pz02 = openmc.ZPlane(surface_id=302, z0= 0.04633)
pz03 = openmc.ZPlane(surface_id=303, z0=-2.3165)
pz04 = openmc.ZPlane(surface_id=304, z0= 2.3165)

#----- Arbitrary planes
p01 = openmc.Plane(surface_id=401, a=sqrt(3)/2, b= 0.5, c=0.0, d=0.0)
p02 = openmc.Plane(surface_id=402, a=sqrt(3)/2, b= 0.5, c=0.0, d=-0.88)
p03 = openmc.Plane(surface_id=403, a=sqrt(3)/2, b= 0.5, c=0.0, d=-1.65)
p04 = openmc.Plane(surface_id=404, a=sqrt(3)/2, b= 0.5, c=0.0, d=-2.0)
p05 = openmc.Plane(surface_id=405, a=sqrt(3)/2, b= 0.5, c=0.0, d=-21.15)
p06 = openmc.Plane(surface_id=406, a=sqrt(3)/2, b= 0.5, c=0.0, d=-21.5)
p07 = openmc.Plane(surface_id=407, a=sqrt(3)/2, b= 0.5, c=0.0, d=-22.5)
p08 = openmc.Plane(surface_id=408, a=sqrt(3)/2, b= 0.5, c=0.0, d=-23.4)
p09 = openmc.Plane(surface_id=409, a=-0.5, b=sqrt(3)/2, c=0.0, d=-10.38)
p10 = openmc.Plane(surface_id=410, a=sqrt(3)/2, b=-0.5, c=0.0, d=0.0)
p11 = openmc.Plane(surface_id=451, a=sqrt(3)/2, b=-0.5, c=0.0, d=-23.4)
p12 = openmc.Plane(surface_id=477, a=sqrt(3)/2, b= 0.5, c=0.0, d=23.4)
p13 = openmc.Plane(surface_id=478, a=sqrt(3)/2, b=-0.5, c=0.0, d=23.4)

#----- Cylinders
cz01 = openmc.ZCylinder(surface_id=601, x0=-5.00890, y0=-2.35, r=0.35)
cz02 = openmc.ZCylinder(surface_id=602, x0=-19.0089, y0=-2.35, r=0.35)
cz03 = openmc.ZCylinder(surface_id=603, x0=-3.1325,  y0=-5.6,  r=0.7)
cz04 = openmc.ZCylinder(surface_id=604, x0=-17.1325, y0=-5.6,  r=0.7)
cz05 = openmc.ZCylinder(surface_id=605, x0=-1.25612, y0=-8.85, r=0.7)
cz06 = openmc.ZCylinder(surface_id=606, x0=-15.25612, y0=-8.85, r=0.7)
cz07 = openmc.ZCylinder(surface_id=607, x0= 0.62027, y0=-12.1, r=0.7)
cz08 = openmc.ZCylinder(surface_id=608, x0=-13.37973, y0=-12.1, r=0.7)
cz09 = openmc.ZCylinder(surface_id=609, x0= 2.49666, y0=-15.35,r=0.7)
cz10 = openmc.ZCylinder(surface_id=610, x0=-11.50334, y0=-15.35,r=0.7)
cz11 = openmc.ZCylinder(surface_id=611, x0= 4.37304, y0=-18.6, r=0.7)
cz12 = openmc.ZCylinder(surface_id=612, x0=-9.62696, y0=-18.6, r=0.7)
cz13 = openmc.ZCylinder(surface_id=613, x0= 5.84529, y0=-21.15,r=0.35)
cz14 = openmc.ZCylinder(surface_id=614, x0=-8.15471, y0=-21.15,r=0.35)

#----- Spheres
sph01 = openmc.Sphere(surface_id=701, r=0.02135)
sph02 = openmc.Sphere(surface_id=702, r=0.03135)
sph03 = openmc.Sphere(surface_id=703, r=0.03485)
sph04 = openmc.Sphere(surface_id=704, r=0.03835)
sph05 = openmc.Sphere(surface_id=705, r=0.04235)

#----- Boundary conditions
pz03.boundary_type='reflective'
pz04.boundary_type='reflective'

p08.boundary_type='periodic'
p11.boundary_type='periodic'
p12.boundary_type='periodic'
p13.boundary_type='periodic'
py42.boundary_type='periodic'
py43.boundary_type='periodic'

p08.periodic_surface = p12
p11.periodic_surface = p13

#********************** Cells & Universes **********************

#----- Create the wrapper for Cell 1
wrapper1_cell = openmc.Cell(cell_id=1, name='Wrapper', fill=graphite)
wrapper1_cell.region = (-py01 & +py03 & -px01 & +p07 | -py02 & +py03 & -p02 & +px01
                       | -py03 & -p02 & +p03 & +p09 | +py40  & +p03 & -p09 & -p01
                       | -py03 & +py40 & +p07 & -p06 | -py40 & +py41 & +p07 & -p01 
                       | -py03 & +py04 & -p03 & +p04 | -py09 & +py10 & -p03 & +p04
                       | -py15 & +py16 & -p03 & +p04 | -py21 & +py22 & -p03 & +p04
                       | -py27 & +py28 & -p03 & +p04 | -py33 & +py34 & -p03 & +p04 
                       | -py39 & +py40 & -p03 & +p04 | -py03 & +py04 & -p05 & +p06
                       | -py09 & +py10 & -p05 & +p06 | -py15 & +py16 & -p05 & +p06
                       | -py21 & +py22 & -p05 & +p06 | -py27 & +py28 & -p05 & +p06
                       | -py33 & +py34 & -p05 & +p06 | -py39 & +py40 & -p05 & +p06)

#----- Create the planks for Cell 1
plank01_cell = openmc.Cell(cell_id=2, name='Plank 1', fill=graphite)
plank01_cell.region = (-py04 & +py05 & -p03 & +p06 | -py05 & +py06 & +p06 & -px02
                      | -py05 & +py06 & -p03 & +px03 | -py06 & +py07 & -p03 & +p06
                      | -py07 & +py08 & +p06 & -px04 | -py07 & +py08 & -p03 & +px05
                      | -py08 & +py09 & -p03 & +p06) 

plank02_cell = openmc.Cell(cell_id=3, name='Plank 2', fill=graphite)
plank02_cell.region = (-py10 & +py11 & -p03 & +p06 | -py11 & +py12 & +p06 & -px06
                      | -py11 & +py12 & -p03 & +px07 | -py12 & +py13 & -p03 & +p06
                      | -py13 & +py14 & +p06 & -px08 | -py13 & +py14 & -p03 & +px09
                      | -py14 & +py15 & -p03 & +p06)

plank03_cell = openmc.Cell(cell_id=4, name='Plank 3', fill=graphite)
plank03_cell.region = (-py16 & +py17 & -p03 & +p06 | -py17 & +py18 & +p06 & -px10
                      | -py17 & +py18 & -p03 & +px11 | -py18 & +py19 & -p03 & +p06
                      | -py19 & +py20 & +p06 & -px12 | -py19 & +py20 & -p03 & +px13
                      | -py20 & +py21 & -p03 & +p06)

plank04_cell = openmc.Cell(cell_id=5, name='Plank 4', fill=graphite)
plank04_cell.region = (-py22 & +py23 & -p03 & +p06 | -py23 & +py24 & +p06 & -px14
                      | -py23 & +py24 & -p03 & +px15 | -py24 & +py25 & -p03 & +p06
                      | -py25 & +py26 & +p06 & -px16 | -py25 & +py26 & -p03 & +px17
                      | -py26 & +py27 & -p03 & +p06)

plank05_cell = openmc.Cell(cell_id=6, name='Plank 5', fill=graphite)
plank05_cell.region = (-py28 & +py29 & -p03 & +p06 | -py29 & +py30 & +p06 & -px18
                      | -py29 & +py30 & -p03 & +px19 | -py30 & +py31 & -p03 & +p06 
                      | -py31 & +py32 & +p06 & -px20 | -py31 & +py32 & -p03 & +px21
                      | -py32 & +py33 & -p03 & +p06)

plank06_cell = openmc.Cell(cell_id=7, name='Plank 6', fill=graphite)
plank06_cell.region = (-py34 & +py35 & -p03 & +p06 | -py35 & +py36 & +p06 & -px22
                      | -py35 & +py36 & -p03 & +px23 | -py36 & +py37 & -p03 & +p06
                      | -py37 & +py38 & +p06 & -px24 | -py37 & +py38 & -p03 & +px25
                      | -py38 & +py39 & -p03 & +p06)

#----- Create the coolant for Cell 1
coolant1_cell = openmc.Cell(cell_id=8, name='Coolant Cell 1', fill=flibe)
coolant1_cell.region = (  -py01 & -p07 | -py41 & -p01 
                       | -py01 & +py02 & +px01 & -p01 | -py01 & +p02 & -p01 & +p09 
                       | -py03 & +py04 & -p04 & +p05 & +cz01 & +cz02
                       | -py09 & +py10 & -p04 & +p05 & +cz03 & +cz04 
                       | -py15 & +py16 & -p04 & +p05 & +cz05 & +cz06
                       | -py21 & +py22 & -p04 & +p05 & +cz07 & +cz08
                       | -py27 & +py28 & -p04 & +p05 & +cz09 & +cz10
                       | -py33 & +py34 & -p04 & +p05 & +cz11 & +cz12
                       | -py39 & +py40 & -p04 & +p05 & +cz13 & +cz14)

#----- Create the universe of one TRISO particle
kernel = openmc.Cell(cell_id=9, fill=uoxy, region=-sph01)
pcarbon = openmc.Cell(cell_id=10, fill=pcarbon, region=+sph01 & -sph02)
IPyC = openmc.Cell(cell_id=11, fill=graphite, region=+sph02 & -sph03)
SiC = openmc.Cell(cell_id=12, fill=SiC, region=+sph03 & -sph04)
OPyC = openmc.Cell(cell_id=13, fill=graphite, region=+sph04 & -sph05)
outer = openmc.Cell(cell_id=14, fill=graphite, region=+sph05)

particle = openmc.Universe(cells=[kernel, pcarbon, IPyC, SiC, OPyC, outer])
#particle.plot(origin=(0, 0, 0), width=(0.1, 0.1), color_by='material')

outer_cell = openmc.Cell(cell_id=15, fill=graphite)
outer_univ = openmc.Universe(cells=[outer_cell])

#----- Create the lattice of TRISO particles
triso_lattice = openmc.RectLattice(name='TRISO Lattice')
triso_lattice.pitch = (0.09266, 0.09266, 0.09266)
triso_lattice.lower_left = (-9.7293, -0.18532, -2.3165)
triso_lattice.outer = outer_univ
triso_lattice.universes = np.tile(particle, (50, 4, 210))

trisos_cell = openmc.Cell(cell_id=16, name='TRISOS', fill=triso_lattice)
trisos_universe = openmc.Universe(cells=[trisos_cell])
#trisos_universe.plot(width=(0.4, 0.2), colors={external_cell: 'blue'})

#----- Create the fuel stripes for Cell 1
stripe01_cell = openmc.Cell(cell_id=17, name='Stripe 1', fill=trisos_universe)
stripe01_cell.region = (-py05 & +py06 & +px02 & -px03) 
stripe01_cell.translation = (-12.00890, -2.63532, 0)

stripe02_cell = openmc.Cell(cell_id=18, name='Stripe 2', fill=trisos_universe)
stripe02_cell.region = (-py07 & +py08 & +px04 & -px05) 
stripe02_cell.translation = (-10.53662, -4.61468, 0)

stripe03_cell = openmc.Cell(cell_id=19, name='Stripe 3', fill=trisos_universe)
stripe03_cell.region = (-py11 & +py12 & +px06 & -px07) 
stripe03_cell.translation = (-10.13250, -5.88532, 0)

stripe04_cell = openmc.Cell(cell_id=20, name='Stripe 4', fill=trisos_universe)
stripe04_cell.region = (-py13 & +py14 & +px08 & -px09) 
stripe04_cell.translation = (-8.66028, -7.86468, 0)

stripe05_cell = openmc.Cell(cell_id=21, name='Stripe 5', fill=trisos_universe)
stripe05_cell.region = (-py17 & +py18 & +px10 & -px11) 
stripe05_cell.translation = (-8.256105, -9.13532, 0)

stripe06_cell = openmc.Cell(cell_id=22, name='Stripe 6', fill=trisos_universe)
stripe06_cell.region = (-py19 & +py20 & +px12 & -px13) 
stripe06_cell.translation = (-6.78389, -11.11470, 0)

stripe07_cell = openmc.Cell(cell_id=23, name='Stripe 7', fill=trisos_universe)
stripe07_cell.region = (-py23 & +py24 & +px14 & -px15) 
stripe07_cell.translation = (-6.37971, -12.38530, 0)

stripe08_cell = openmc.Cell(cell_id=24, name='Stripe 8', fill=trisos_universe)
stripe08_cell.region = (-py25 & +py26 & +px16 & -px17) 
stripe08_cell.translation = (-4.90749, -14.36470, 0)

stripe09_cell = openmc.Cell(cell_id=25, name='Stripe 9', fill=trisos_universe)
stripe09_cell.region = (-py29 & +py30 & +px18 & -px19) 
stripe09_cell.translation = (-4.50332, -15.63530, 0)

stripe10_cell = openmc.Cell(cell_id=26, name='Stripe 10', fill=trisos_universe)
stripe10_cell.region = (-py31 & +py32 & +px20 & -px21) 
stripe10_cell.translation = (-3.03110, -17.61470, 0)

stripe11_cell = openmc.Cell(cell_id=27, name='Stripe 11', fill=trisos_universe)
stripe11_cell.region = (-py35 & +py36 & +px22 & -px23) 
stripe11_cell.translation = (-2.62693, -18.88530, 0)

stripe12_cell = openmc.Cell(cell_id=28, name='Stripe 12', fill=trisos_universe)
stripe12_cell.region = (-py37 & +py38 & +px24 & -px25) 
stripe12_cell.translation = (-1.15470, -20.86470, 0)

#----- Create the spacers for Cell 1
spacers1_cell = openmc.Cell(cell_id=29, name='Spacers', fill=graphite)
spacers1_cell.region = (-cz01 & +py04   | -cz02 & +py04 | -cz03 & +py10 
                       | -cz04 & +py10 | -cz05 & +py16 | -cz06 & +py16 
                       | -cz07 & +py22 | -cz08 & +py22 | -cz09 & +py28 
                       | -cz10 & +py28 | -cz11 & +py34 | -cz12 & +py34
                       | -cz13 & -py39 | -cz14 & -py39)

#----- Create the universe containing all cells
universe1 = openmc.Universe(cells=[plank01_cell, plank02_cell, plank03_cell, 
                                  plank04_cell, plank05_cell, plank06_cell,
                                  stripe01_cell, stripe02_cell, stripe03_cell,
                                  stripe04_cell, stripe05_cell, stripe06_cell, 
                                  stripe07_cell, stripe08_cell, stripe09_cell, 
                                  stripe10_cell, stripe11_cell, stripe12_cell, 
                                  coolant1_cell, spacers1_cell, wrapper1_cell])

#----- Create the root universe
cell1 = openmc.Cell(cell_id=30, name='Cell 1', fill=universe1)
cell1.region = (-py01 & +py42 & +p08 & -p01 & +pz03 & -pz04)

cell2 = openmc.Cell(cell_id=31, name='Cell 2', fill=universe1)
cell2.region = (+py01 & -py43 & -p10 & +p11 & +pz03 & -pz04)
cell2.rotation = (0, 0, -120)

cell3 = openmc.Cell(cell_id=32, name='Cell 3', fill=universe1)
cell3.region = (+p01 & -p13 & +p10 & -p12 & +pz03 & -pz04)
cell3.rotation = (0, 0, 120)

root_universe = openmc.Universe(name='root universe', cells=[cell1, cell2, cell3])
"""
#root_universe.plot(origin=(-17, 11, 0), width=(15, 15), pixels=(200, 200), basis='xy',
root_universe.plot(origin=(0, 0, 0), width=(60, 60), pixels=(200, 200), basis='xy',
                   colors={plank01_cell:'yellow', plank02_cell:'yellow',
                           plank03_cell:'yellow', plank04_cell:'yellow',
                           plank05_cell:'yellow', plank06_cell:'yellow',
                           stripe01_cell:'red', stripe02_cell:'red',
                           stripe03_cell:'red', stripe04_cell:'red',
                           stripe05_cell:'red', stripe06_cell:'red',
                           stripe07_cell:'red', stripe08_cell:'red',
                           stripe09_cell:'red', stripe10_cell:'red',
                           stripe11_cell:'red', stripe12_cell:'red',
                           spacers1_cell:'fuchsia', coolant1_cell:'blue',
                           wrapper1_cell:'gray'})"""
"""
root_universe.plot(origin=(-2.5, -2.5, 0), width=(1, 0.8), pixels=(200, 200), basis='xz',
                   colors={plank01_cell:'yellow', plank02_cell:'yellow',
                           plank03_cell:'yellow', plank04_cell:'yellow',
                           plank05_cell:'yellow', plank06_cell:'yellow',
                           stripe01_cell:'red', stripe02_cell:'red',
                           stripe03_cell:'red', stripe04_cell:'red',
                           stripe05_cell:'red', stripe06_cell:'red',
                           stripe07_cell:'red', stripe08_cell:'red',
                           stripe09_cell:'red', stripe10_cell:'red',
                           stripe11_cell:'red', stripe12_cell:'red',
                           spacers1_cell:'fuchsia', coolant1_cell:'blue',
                           wrapper1_cell:'gray'})
"""
"""
root_universe.plot(origin=(-4, -5, 0), width=(8,2), pixels=(200, 200),
                   color_by='material')
"""

#----- Set root universe & export to "geometry.xml"
geometry = openmc.Geometry(root_universe)
geometry.export_to_xml()

#==============================================================================
#                         PLOT 
#==============================================================================
"""
# Instantiate a Plot
plot = openmc.Plot()
plot.filename = 'ElementXY'
plot.origin = (0, 0, 0)
plot.colors = ({plank01_cell:'yellow', plank02_cell:'yellow',
                           plank03_cell:'yellow', plank04_cell:'yellow',
                           plank05_cell:'yellow', plank06_cell:'yellow',
                           stripe01_cell:'red', stripe02_cell:'red',
                           stripe03_cell:'red', stripe04_cell:'red',
                           stripe05_cell:'red', stripe06_cell:'red',
                           stripe07_cell:'red', stripe08_cell:'red',
                           stripe09_cell:'red', stripe10_cell:'red',
                           stripe11_cell:'red', stripe12_cell:'red',
                           spacers1_cell:'fuchsia', coolant1_cell:'blue',
                           wrapper1_cell:'gray'})
plot.width = [60, 60]
plot.pixels = [600, 600]

# Plots collection & export to "plots.xml"
plot_file = openmc.Plots([plot])
plot_file.export_to_xml()


#==============================================================================
#                         TALLIES
#==============================================================================

#----- Instantiate Tallies
tallies = openmc.Tallies()

#----- Tally reaction rates at fuel stripe 1
tally201 = openmc.Tally(tally_id=201, name='stripe01 rxn rates')
tally201.scores = ['fission', 'nu-fission', 'total']
tally201.filters = [openmc.CellFilter(stripe01_cell)]
tallies.append(tally201)

#----- Tally reaction rates at fuel stripe 2
tally202 = openmc.Tally(tally_id=202, name='stripe02 rxn rates')
tally202.scores = ['fission', 'nu-fission', 'total']
tally202.filters = [openmc.CellFilter(stripe02_cell)]
tallies.append(tally202)

#----- Tally reaction rates at fuel stripe 3
tally203 = openmc.Tally(tally_id=203, name='stripe03 rxn rates')
tally203.scores = ['fission', 'nu-fission', 'total']
tally203.filters = [openmc.CellFilter(stripe03_cell)]
tallies.append(tally203)

#----- Tally reaction rates at fuel stripe 4
tally204 = openmc.Tally(tally_id=204, name='stripe04 rxn rates')
tally204.scores = ['fission', 'nu-fission', 'total']
tally204.filters = [openmc.CellFilter(stripe04_cell)]
tallies.append(tally204)

#----- Tally reaction rates at fuel stripe 5
tally205 = openmc.Tally(tally_id=205, name='stripe05 rxn rates')
tally205.scores = ['fission', 'nu-fission', 'total']
tally205.filters = [openmc.CellFilter(stripe05_cell)]
tallies.append(tally205)

#----- Tally reaction rates at fuel stripe 6
tally206 = openmc.Tally(tally_id=206, name='stripe06 rxn rates')
tally206.scores = ['fission', 'nu-fission', 'total']
tally206.filters = [openmc.CellFilter(stripe06_cell)]
tallies.append(tally206)

#----- Tally reaction rates at fuel stripe 7
tally207 = openmc.Tally(tally_id=207, name='stripe07 rxn rates')
tally207.scores = ['fission', 'nu-fission', 'total']
tally207.filters = [openmc.CellFilter(stripe07_cell)]
tallies.append(tally207)

#----- Tally reaction rates at fuel stripe 8
tally208 = openmc.Tally(tally_id=208, name='stripe08 rxn rates')
tally208.scores = ['fission', 'nu-fission', 'total']
tally208.filters = [openmc.CellFilter(stripe08_cell)]
tallies.append(tally208)

#----- Tally reaction rates at fuel stripe 9
tally209 = openmc.Tally(tally_id=209, name='stripe09 rxn rates')
tally209.scores = ['fission', 'nu-fission', 'total']
tally209.filters = [openmc.CellFilter(stripe09_cell)]
tallies.append(tally209)

#----- Tally reaction rates at fuel stripe 10
tally210 = openmc.Tally(tally_id=210, name='stripe10 rxn rates')
tally210.scores = ['fission', 'nu-fission', 'total']
tally210.filters = [openmc.CellFilter(stripe10_cell)]
tallies.append(tally210)

#----- Tally reaction rates at fuel stripe 11
tally211 = openmc.Tally(tally_id=211, name='stripe11 rxn rates')
tally211.scores = ['fission', 'nu-fission', 'total']
tally211.filters = [openmc.CellFilter(stripe11_cell)]
tallies.append(tally211)

#----- Tally reaction rates at fuel stripe 12
tally212 = openmc.Tally(tally_id=212, name='stripe12 rxn rates')
tally212.scores = ['fission', 'nu-fission', 'total']
tally212.filters = [openmc.CellFilter(stripe12_cell)]
tallies.append(tally212)

#----- Tally reaction rates at 1-5th of fuel stripe 01
mesh301 = openmc.RegularMesh(mesh_id=1)
mesh301.dimension = [5, 1, 1]
mesh301.lower_left = [-21.7382, -2.82064, -2.3165]
mesh301.width = [3.89172, 0.37064, 4.633]

tally301 = openmc.Tally(tally_id=301, name='1-5stripe01 rxn rates')
tally301.scores = ['fission', 'nu-fission', 'total']
tally301.filters = [openmc.MeshFilter(mesh301)]
tallies.append(tally301)

#----- Tally reaction rates at 1-5th of fuel stripe 02
mesh302 = openmc.RegularMesh(mesh_id=2)
mesh302.dimension = [5, 1, 1]
mesh302.lower_left = [-20.2659, -4.8, -2.3165]
mesh302.width = [3.89172, 0.37064, 4.633]

tally302 = openmc.Tally(tally_id=302, name='1-5stripe02 rxn rates')
tally302.scores = ['fission', 'nu-fission', 'total']
tally302.filters = [openmc.MeshFilter(mesh302)]
tallies.append(tally302)

#----- Tally reaction rates at 1-5th of fuel stripe 03
mesh303 = openmc.RegularMesh(mesh_id=3)
mesh303.dimension = [5, 1, 1]
mesh303.lower_left = [-19.8618, -6.07064, -2.3165]
mesh303.width = [3.89172, 0.37064, 4.633]

tally303 = openmc.Tally(tally_id=303, name='1-5stripe03 rxn rates')
tally303.scores = ['fission', 'nu-fission', 'total']
tally303.filters = [openmc.MeshFilter(mesh303)]
tallies.append(tally303)

#----- Tally reaction rates at 1-5th of fuel stripe 04
mesh304 = openmc.RegularMesh(mesh_id=4)
mesh304.dimension = [5, 1, 1]
mesh304.lower_left = [-18.3896, -8.05, -2.3165]
mesh304.width = [3.89172, 0.37064, 4.633]

tally304 = openmc.Tally(tally_id=304, name='1-5stripe04 rxn rates')
tally304.scores = ['fission', 'nu-fission', 'total']
tally304.filters = [openmc.MeshFilter(mesh304)]
tallies.append(tally304)

#----- Tally reaction rates at 1-5th of fuel stripe 05
mesh305 = openmc.RegularMesh(mesh_id=5)
mesh305.dimension = [5, 1, 1]
mesh305.lower_left = [-17.9854, -9.32064, -2.3165]
mesh305.width = [3.89172, 0.37064, 4.633]

tally305 = openmc.Tally(tally_id=305, name='1-5stripe05 rxn rates')
tally305.scores = ['fission', 'nu-fission', 'total']
tally305.filters = [openmc.MeshFilter(mesh305)]
tallies.append(tally305)

#----- Tally reaction rates at 1-5th of fuel stripe 06
mesh306 = openmc.RegularMesh(mesh_id=6)
mesh306.dimension = [5, 1, 1]
mesh306.lower_left = [-16.5132, -11.3, -2.3165]
mesh306.width = [3.89172, 0.37064, 4.633]

tally306 = openmc.Tally(tally_id=306, name='1-5stripe06 rxn rates')
tally306.scores = ['fission', 'nu-fission', 'total']
tally306.filters = [openmc.MeshFilter(mesh306)]
tallies.append(tally306)

#----- Tally reaction rates at 1-5th of fuel stripe 07
mesh307 = openmc.RegularMesh(mesh_id=7)
mesh307.dimension = [5, 1, 1]
mesh307.lower_left = [-16.109, -12.57064, -2.3165]
mesh307.width = [3.89172, 0.37064, 4.633]

tally307 = openmc.Tally(tally_id=307, name='1-5stripe07 rxn rates')
tally307.scores = ['fission', 'nu-fission', 'total']
tally307.filters = [openmc.MeshFilter(mesh307)]
tallies.append(tally307)

#----- Tally reaction rates at 1-5th of fuel stripe 08
mesh308 = openmc.RegularMesh(mesh_id=8)
mesh308.dimension = [5, 1, 1]
mesh308.lower_left = [-14.6368, -14.55, -2.3165]
mesh308.width = [3.89172, 0.37064, 4.633]

tally308 = openmc.Tally(tally_id=308, name='1-5stripe08 rxn rates')
tally308.scores = ['fission', 'nu-fission', 'total']
tally308.filters = [openmc.MeshFilter(mesh308)]
tallies.append(tally308)

#----- Tally reaction rates at 1-5th of fuel stripe 09
mesh309 = openmc.RegularMesh(mesh_id=9)
mesh309.dimension = [5, 1, 1]
mesh309.lower_left = [-14.2326, -15.82064, -2.3165]
mesh309.width = [3.89172, 0.37064, 4.633]

tally309 = openmc.Tally(tally_id=309, name='1-5stripe09 rxn rates')
tally309.scores = ['fission', 'nu-fission', 'total']
tally309.filters = [openmc.MeshFilter(mesh309)]
tallies.append(tally309)

#----- Tally reaction rates at 1-5th of fuel stripe 10
mesh310 = openmc.RegularMesh(mesh_id=10)
mesh310.dimension = [5, 1, 1]
mesh310.lower_left = [-12.7604, -17.8, -2.3165]
mesh310.width = [3.89172, 0.37064, 4.633]

tally310 = openmc.Tally(tally_id=310, name='1-5stripe10 rxn rates')
tally310.scores = ['fission', 'nu-fission', 'total']
tally310.filters = [openmc.MeshFilter(mesh310)]
tallies.append(tally310)

#----- Tally reaction rates at 1-5th of fuel stripe 11
mesh311 = openmc.RegularMesh(mesh_id=11)
mesh311.dimension = [5, 1, 1]
mesh311.lower_left = [-12.3562, -19.07064, -2.3165]
mesh311.width = [3.89172, 0.37064, 4.633]

tally311 = openmc.Tally(name='1-5stripe11 rxn rates')
tally311.scores = ['fission', 'nu-fission', 'total']
tally311.filters = [openmc.MeshFilter(mesh311)]
tallies.append(tally311)

#----- Tally reaction rates at 1-5th of fuel stripe 12
mesh312 = openmc.RegularMesh(mesh_id=12)
mesh312.dimension = [5, 1, 1]
mesh312.lower_left = [-10.884, -21.05, -2.3165]
mesh312.width = [3.89172, 0.37064, 4.633]

tally312 = openmc.Tally(tally_id=312, name='1-5stripe12 rxn rates')
tally312.scores = ['fission', 'nu-fission', 'total']
tally312.filters = [openmc.MeshFilter(mesh312)]
tallies.append(tally312)

#----- Tally neutron flux in whole model for 3 energy groups & 100x100 mesh
#energy_filter = openmc.EnergyFilter([0, 3, 0.1e6, 20e6])
mesh400 = openmc.RegularMesh(mesh_id=13)
mesh400.dimension = [100, 100, 1]
mesh400.lower_left = [-27.02, -27.02, -2.3165]
mesh400.width = [0.5404, 0.5404, 4.633]

tally400 = openmc.Tally(tally_id=400, name='Flux Mesh')
tally400.scores = ['flux']
tally400.filters = [openmc.MeshFilter(mesh400),
                    openmc.EnergyFilter([0.0, 3.0, 0.1e6, 20e6])]
tallies.append(tally400)

tally401 = openmc.Tally(tally_id=401, name='Flux')
tally401.scores = ['flux']
tally401.filters = [openmc.EnergyFilter([0.0, 3.0, 0.1e6, 20e6])]
tallies.append(tally401)

tally402 = openmc.Tally(tally_id=402, name='Fission')
tally402.scores = ['fission', 'nu-fission']
tally402.filters = [openmc.MeshFilter(mesh400)]
tallies.append(tally402)

#----- Tally reaction rates over whole model
tally500 = openmc.Tally(tally_id=500, name='Rates')
tally500.scores = ['fission', 'nu-fission']            
tallies.append(tally500)

#----- Tally flux spectrum
groups = pd.read_excel('../252_EnergyGroups.xlsx')
garray = groups['Emax'].to_numpy()
tally600 = openmc.Tally(tally_id=600, name='Flux Spectrum')
tally600.scores = ['flux']
tally600.filters = [openmc.EnergyFilter(garray)]
#tally600.filters = [openmc.EnergyFilter(np.logspace(np.log10(10e-5), np.log10(20.0e6), 501))]
tallies.append(tally600)

#----- Export to "tallies.xml"
tallies.export_to_xml()
"""
#==============================================================================
#                         SETTINGS & EXECUTION 
#==============================================================================

#----- Simulation parameters
point = openmc.stats.Point((-11.96257, -2.58899, 0.04633)) # Identifies the center
                                                           # of a TRISO particle (kernel)
                                                           # to start reaction 
                                                     
settings = openmc.Settings()
settings.source = openmc.Source(space=point)
settings.inactive  = 50
settings.batches   = 500
settings.particles = 250000
settings.temperature = {'method': 'interpolation'}
settings.output = {'tallies': False}

geom_mesh = openmc.Mesh()
geom_mesh.lower_left = (-27.02, -23.4, -2.3165)
geom_mesh.upper_right = (27.02, 23.4, 2.3165)
geom_mesh.dimension = (8, 8, 8)
settings.entropy_mesh = geom_mesh

#----- Export to "settings.xml"
settings.export_to_xml()

#----- Executing OpenMC
#openmc.plot_geometry()           # Plot mode
#im = Image.open('ElementXY.ppm') # Exporting to JPG
#im.save('ElementXY.jpg')
#im.pixels=[600, 600]
#openmc.run(geometry_debug=True)  # Geometry debug mode
#openmc.run()                     # Normal mode   

