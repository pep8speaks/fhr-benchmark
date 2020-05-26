"""
This python script builds the XML files for case3a of the FHR benchmark
materials.xml, geometry.xml, settings.xml, and tallies.xml

"""

###############################################################################
#                      Python Package Import
###############################################################################

import openmc
import numpy as np
from numpy import sin, cos, tan, pi
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, '../../scripts/')
from phase1a_constants import *
from tallies import *

###############################################################################
#                      Simulation Input File Parameters
###############################################################################

# OpenMC simulation parameters
batches = 500
inactive = 100
particles = 2000000
tallies_on = True

###############################################################################
#                 Exporting to OpenMC materials.xml file
###############################################################################

uoc_9 = openmc.Material()
uoc_9.set_density('g/cc', 11)
uoc_9.add_nuclide('U235', 2.27325e-3)
uoc_9.add_nuclide('U238', 2.269476e-2)
uoc_9.add_nuclide('O16', 3.561871e-2)
uoc_9.add_nuclide('C0', 9.79714e-3)
uoc_9.temperature = 1110
uoc_9.volume = 4 / 3 * pi * (T_r1 ** 3) * 101 * 210 * 4 * 36

por_c = openmc.Material()
por_c.set_density('g/cc', 1)
por_c.add_nuclide('C0', 5.013980e-2)
por_c.temperature = 948

si_c = openmc.Material()
si_c.set_density('g/cc', 3.2)
si_c.add_nuclide('Si28', 4.431240e-2)
si_c.add_nuclide('Si29', 2.25887e-3)
si_c.add_nuclide('Si30', 1.48990e-3)
si_c.add_nuclide('C0', 4.806117e-2)
si_c.temperature = 948

graphite = openmc.Material()
graphite.set_density('g/cc', 1.8)
graphite.add_nuclide('C0', 9.025164e-2)
graphite.temperature = 948

p_graphite = openmc.Material()
p_graphite.set_density('g/cc', 1.8)
p_graphite.add_nuclide('C0', 9.025164e-2)
p_graphite.temperature = 948

s_graphite = openmc.Material()
s_graphite.set_density('g/cc', 1.8)
s_graphite.add_nuclide('C0', 9.025164e-2)
s_graphite.temperature = 948

lm_graphite = openmc.Material()
lm_graphite.set_density('g/cc', 1.8)
lm_graphite.add_nuclide('C0', 9.025164e-2)
lm_graphite.temperature = 948

flibe = openmc.Material()
flibe.set_density('g/cc', 1.95)
flibe.add_nuclide('Li6', 1.383014e-6)
flibe.add_nuclide('Li7', 2.37132e-2)
flibe.add_nuclide('Be9', 1.18573e-2)
flibe.add_nuclide('F19', 4.74291e-2)
flibe.temperature = 948

mhc = openmc.Material()
mhc.set_density('g/cc', 10.28)
mhc.add_nuclide('Mo92', 9.328884e-3)
mhc.add_nuclide('Mo94', 5.850533e-3)
mhc.add_nuclide('Mo95', 1.010836e-2)
mhc.add_nuclide('Mo96', 1.061782e-2)
mhc.add_nuclide('Mo97', 6.102080e-3)
mhc.add_nuclide('Mo98', 1.546981e-2)
mhc.add_nuclide('Mo100', 6.205246e-3)
mhc.add_nuclide('Hf174', 6.659530e-7)
mhc.add_nuclide('Hf176', 2.189321e-5)
mhc.add_nuclide('Hf177', 7.741704e-5)
mhc.add_nuclide('Hf178', 1.135450e-4)
mhc.add_nuclide('Hf179', 5.668925e-5)
mhc.add_nuclide('Hf180', 1.460102e-4)
mhc.add_nuclide('C0', 5.154371e-4)
mhc.temperature = 948

euo_s = openmc.Material()
euo_s.set_density('g/cc', 5)
euo_s.add_nuclide('Eu151', 8.179510e-3)
euo_s.add_nuclide('Eu153', 8.932435e-3)
euo_s.add_nuclide('O16', 2.56792e-2)
euo_s.temperature = 948

mats = openmc.Materials(
    (uoc_9,
     por_c,
     si_c,
     graphite,
     p_graphite,
     lm_graphite,
     flibe,
     mhc,
     s_graphite,
     euo_s))
mats.export_to_xml()

###############################################################################
#                 Exporting to OpenMC geometry.xml file
###############################################################################

# top and bottom surfaces (dz)
top_surface = openmc.ZPlane(
    z0=T_pitch / 2 + (z_thickness - 1) / 2 * T_pitch, boundary_type='reflective')
bot_surface = openmc.ZPlane(
    z0=-(T_pitch / 2 + (z_thickness - 1) / 2 * T_pitch), boundary_type='reflective')

# Outermost Hexagon

H_m = 1 / tan(pi / 6)
H_1 = openmc.YPlane(0.5 * H_side / tan(pi / 6), 'periodic')
H_2 = plane(-H_m, 0.5 * H_side, 0.5 * H_side / tan(pi / 6), 'periodic')
H_3 = plane(H_m, 0.5 * H_side, -0.5 * H_side / tan(pi / 6), 'periodic')
H_4 = openmc.YPlane(-0.5 * H_side / tan(pi / 6), 'periodic')
H_5 = plane(-H_m, -0.5 * H_side, -0.5 * H_side / tan(pi / 6), 'periodic')
H_6 = plane(H_m, -0.5 * H_side, 0.5 * H_side / tan(pi / 6), 'periodic')
H_1.periodic_surface = H_4
H_2.periodic_surface = H_5
H_3.periodic_surface = H_6
H_region = -H_1 & +H_4 & -H_2 & +H_3 & +H_5 & -H_6
H_cell = openmc.Cell(fill=graphite)
H_cell.region = H_region & -top_surface & + bot_surface

# Diamond Plank Area
A1_D_cell = openmc.Cell(fill=flibe)
A1_D_cell.region = region_maker('A1', 'D') & -top_surface & + bot_surface

A2_D_cell = openmc.Cell(fill=flibe)
A2_D_cell.region = region_maker('A2', 'D') & -top_surface & + bot_surface

A3_D_cell = openmc.Cell(fill=flibe)
A3_D_cell.region = region_maker('A3', 'D') & -top_surface & + bot_surface

D_regions = A1_D_cell.region | A2_D_cell.region | A3_D_cell.region
D_universe = openmc.Universe(cells=(A1_D_cell, A2_D_cell, A3_D_cell,))
D_areas = openmc.Cell(fill=D_universe, region=D_regions)
H_cell.region &= ~D_regions

# Discrete Europia
DE_sphere = openmc.Sphere(r=DE_r)
DE_cells = [openmc.Cell(fill=euo_s, region=-DE_sphere),
            openmc.Cell(fill=p_graphite, region=+DE_sphere)]
DE_univ = openmc.Universe(cells=DE_cells)
p_graphite_cell = openmc.Cell(fill=p_graphite)
p_graphite_univ = openmc.Universe(cells=(p_graphite_cell,))

v = DE_univ
lattice1 = openmc.RectLattice()
lattice1.lower_left = (V['A1']['DE']['L']['x'], V['A1']['DE'][
                       'L']['y'], -(DE_pitch / 2 + (z_thickness - 1) / 2 * DE_pitch))
lattice1.pitch = (DE_gap, DE_pitch, DE_pitch)
lattice1.outer = p_graphite_univ
lattice1_list = []
for z in range(z_thickness):
    lattice1_z_list = []
    for row in range(1):
        lattice1_y_list = []
        for col in range(5):
            lattice1_y_list.append(v)
        lattice1_z_list.append(lattice1_y_list)
    lattice1_list.append(lattice1_z_list)

lattice1.universes = lattice1_list

# Graphite Planks
all_P_univ = openmc.Universe()
all_P_regions = region_maker('A1', 'P')  # initialize

for area in range(3):
    area_str = 'A{}'.format(area + 1)
    P_region = region_maker(area_str, 'P')
    P_cell = openmc.Cell(fill=p_graphite,)
    P_cell.fill = lattice1
    P_univ = openmc.Universe(cells=(P_cell,))
    for trans in range(6):
        P_region_new = P_region.translate(
            (trans * T[area_str]['P']['x'], trans * T[area_str]['P']['y'], 0))
        P_cell_new = openmc.Cell(fill=P_univ, region=P_region_new)
        if area == 1:
            P_cell_new.rotation = (0, 0, -120)
        if area == 2:
            P_cell_new.rotation = (0, 0, 120)
        P_cell_new.translation = (
            trans *
            T[area_str]['P']['x'],
            trans *
            T[area_str]['P']['y'],
            0)
        all_P_univ.add_cell(P_cell_new)
        all_P_regions |= P_region_new
        D_areas.region &= ~P_region_new
        H_cell.region &= ~P_region_new
P_areas = openmc.Cell(
    fill=all_P_univ,
    region=all_P_regions & -
    top_surface & +
    bot_surface)

# Triso Particles
spheres = [openmc.Sphere(r=r)
           for r in [T_r1, T_r2, T_r3, T_r4, T_r5]]
triso_cells = [openmc.Cell(fill=uoc_9, region=-spheres[0]),
               openmc.Cell(fill=por_c, region=+spheres[0] & -spheres[1]),
               openmc.Cell(fill=graphite, region=+spheres[1] & -spheres[2]),
               openmc.Cell(fill=si_c, region=+spheres[2] & -spheres[3]),
               openmc.Cell(fill=graphite, region=+spheres[3] & -spheres[4]),
               openmc.Cell(fill=lm_graphite, region=+spheres[4])]
triso_univ = openmc.Universe(cells=triso_cells)
lm_graphite_cell = openmc.Cell(fill=lm_graphite)
lm_graphite_univ = openmc.Universe(cells=(lm_graphite_cell,))

u = triso_univ
lattice = openmc.RectLattice()
lattice.lower_left = (V['A1']['F']['L']['x'], V['A1']['F']['B']
                      ['y'], -(T_pitch / 2 + (z_thickness - 1) / 2 * T_pitch))
lattice.pitch = (T_pitch, T_pitch, T_pitch)
lattice.outer = lm_graphite_univ
lattice_list = []
for z in range(z_thickness):
    lattice_z_list = []
    for row in range(4):
        lattice_y_list = []
        for col in range(210):
            lattice_y_list.append(u)
        lattice_z_list.append(lattice_y_list)
    lattice_list.append(lattice_z_list)

lattice.universes = lattice_list

# Fuel Plank
all_F_univ = openmc.Universe()
all_F_regions = region_maker('A1', 'F')  # initialize

for area in range(3):
    area_str = 'A{}'.format(area + 1)
    F_region = region_maker(area_str, 'F')
    F_cell = openmc.Cell(fill=lm_graphite,)
    F_cell.fill = lattice
    F_univ = openmc.Universe(cells=(F_cell,))
    for t in range(6):
        for x in range(2):
            x_trans = t * T[area_str]['P']['x']
            y_trans = t * T[area_str]['P']['y']
            if x == 1:
                x_trans += T[area_str]['F']['x']
                y_trans += T[area_str]['F']['y']
            F_region_new = F_region.translate((x_trans, y_trans, 0))
            F_cell_new = openmc.Cell(fill=F_univ, region=F_region_new)
            if area == 1:
                F_cell_new.rotation = (0, 0, -120)
            if area == 2:
                F_cell_new.rotation = (0, 0, 120)
            F_cell_new.translation = (x_trans, y_trans, 0)
            all_F_univ.add_cell(F_cell_new)
            all_F_regions |= F_region_new
            P_areas.region &= ~F_region_new
            D_areas.region &= ~F_region_new
            H_cell.region &= ~F_region_new
F_areas = openmc.Cell(
    fill=all_F_univ,
    region=all_F_regions & -
    top_surface & +
    bot_surface)

# Spacer
all_S_univ = openmc.Universe()
S_small_spacer_surf = openmc.ZCylinder(
    r=S_small_r,
    x0=-D_to_center_width - S_A1_D_gap,
    y0=-D_to_center - P_small_gap)  # initialize
all_S_regions = -S_small_spacer_surf & + \
    plane(V['A1']['P']['T']['m'], V['A1']['P']['T']['x'], V['A1']['P']['T']['y'])

# outer loop is for 3 types of spacers, small top, big middle, small bottom
rad = [S_small_r, S_large_r, S_small_r]
start = [0, 1, 5]
end = [1, 6, 6]
C = ['C', 'C', 'Cb']
for y in range(3):
    for area in range(3):
        area_str = 'A{}'.format(area + 1)
        S_cylinder = openmc.ZCylinder(r=rad[y],
                                      x0=V[area_str]['S'][C[y]]['x0'],
                                      y0=V[area_str]['S'][C[y]]['y0'])
        if area == 0:
            S_region = -S_cylinder & + \
                plane(V[area_str]['P']['T']['m'], V[area_str]['P']['T']['x'], V[area_str]['P']['T']['y'])
            if y == 2:
                S_region = -S_cylinder & - \
                    plane(V[area_str]['P']['B']['m'], V[area_str]['P']['B']['x'], V[area_str]['P']['B']['y'])
        if area == 1:
            S_region = -S_cylinder & - \
                plane(V[area_str]['P']['R']['m'], V[area_str]['P']['R']['x'], V[area_str]['P']['R']['y'])
            if y == 2:
                S_region = -S_cylinder & + \
                    plane(V[area_str]['P']['L']['m'], V[area_str]['P']['L']['x'], V[area_str]['P']['L']['y'])
        if area == 2:
            S_region = -S_cylinder & - \
                plane(V[area_str]['P']['L']['m'], V[area_str]['P']['L']['x'], V[area_str]['P']['L']['y'])
            if y == 2:
                S_region = -S_cylinder & + \
                    plane(V[area_str]['P']['R']['m'], V[area_str]['P']['R']['x'], V[area_str]['P']['R']['y'])
        S_cell = openmc.Cell(fill=s_graphite, region=S_region)
        S_univ = openmc.Universe(cells=(S_cell,))
        for trans in range(start[y], end[y]):
            for x in range(2):
                x_trans = trans * T[area_str]['P']['x']
                y_trans = trans * T[area_str]['P']['y']
                if x == 1:
                    x_trans += T[area_str]['S']['x']
                    y_trans += T[area_str]['S']['y']
                S_region_new = S_region.translate((x_trans, y_trans, 0))
                S_cell_new = openmc.Cell(fill=S_univ, region=S_region_new)
                S_cell_new.translation = (x_trans, y_trans, 0)
                all_S_univ.add_cell(S_cell_new)
                all_S_regions |= S_region_new
                F_areas.region &= ~S_region_new
                P_areas.region &= ~S_region_new
                D_areas.region &= ~S_region_new
                H_cell.region &= ~S_region_new
S_areas = openmc.Cell(
    fill=all_S_univ,
    region=all_S_regions & -
    top_surface & +
    bot_surface)

# Control Rod Slot
A1_CS_cell = openmc.Cell(fill=flibe)
A1_CS_cell.region = region_maker('A1', 'CS') & -top_surface & + bot_surface

A2_CS_cell = openmc.Cell(fill=flibe)
A2_CS_cell.region = region_maker('A2', 'CS') & -top_surface & + bot_surface

A3_CS_cell = openmc.Cell(fill=flibe)
A3_CS_cell.region = region_maker('A3', 'CS') & -top_surface & + bot_surface

CS_regions = A1_CS_cell.region | A2_CS_cell.region | A3_CS_cell.region
CS_universe = openmc.Universe(cells=(A1_CS_cell, A2_CS_cell, A3_CS_cell,))
CS_areas = openmc.Cell(fill=CS_universe, region=CS_regions)
S_areas.region &= ~CS_regions
F_areas.region &= ~CS_regions
P_areas.region &= ~CS_regions
D_areas.region &= ~CS_regions
H_cell.region &= ~CS_regions

# Control Rod Arm
A1_CA_cell = openmc.Cell(fill=flibe)
A1_CA_cell.region = region_maker('A1', 'CA') & -top_surface & + bot_surface

A2_CA_cell = openmc.Cell(fill=flibe)
A2_CA_cell.region = region_maker('A2', 'CA') & -top_surface & + bot_surface

A3_CA_cell = openmc.Cell(fill=flibe)
A3_CA_cell.region = region_maker('A3', 'CA') & -top_surface & + bot_surface

CA_regions = A1_CA_cell.region | A2_CA_cell.region | A3_CA_cell.region
CA_universe = openmc.Universe(cells=(A1_CA_cell, A2_CA_cell, A3_CA_cell,))
CA_areas = openmc.Cell(fill=CA_universe, region=CA_regions)
CS_areas.region &= ~CA_regions
S_areas.region &= ~CA_regions
F_areas.region &= ~CA_regions
P_areas.region &= ~CA_regions
D_areas.region &= ~CA_regions
H_cell.region &= ~CA_regions

# export to xml
root = openmc.Universe(
    cells=[
        H_cell,
        D_areas,
        P_areas,
        F_areas,
        S_areas,
        CS_areas,
        CA_areas])
geom = openmc.Geometry(root)
geom.export_to_xml()

###############################################################################
#                   Exporting to OpenMC settings.xml file
##############################################################################
settings = openmc.Settings()
settings.batches = batches
settings.inactive = inactive
settings.particles = particles
settings.temperature = {'multipole': True, 'method': 'interpolation'}
settings.export_to_xml()

###############################################################################
#                   Exporting to OpenMC tallies.xml file
###############################################################################

if tallies_on:
    tallies_generation(root)
else:
    print('tallies off')
