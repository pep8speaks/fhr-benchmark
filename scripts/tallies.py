import openmc
import openmc.mgxs as mgxs
from phase1a_constants import *


def tallies_generation(root):
    """ Creates tallies.xml file

    Parameters
    ----------
    root: openmc.Universe with all the relevant cells for the geometry.

    Returns
    -------
    This function generates the tallies.xml file.
    """
    tallies_file = openmc.Tallies()
    # phase1a-b
    energy_filter_b = openmc.EnergyFilter([1e-6, 20.0e6])
    mesh_b = openmc.RegularMesh(mesh_id=16)
    mesh_b.dimension = [1, 1]
    L = 27.02
    mesh_b.lower_left = [-L, -L]
    mesh_b.upper_right = [L, L]
    mesh_filter_b = openmc.MeshFilter(mesh_b)
    tally_b = openmc.Tally(name='mesh tally b')
    tally_b.filters = [mesh_filter_b, energy_filter_b]
    tally_b.scores = ['delayed-nu-fission', 'nu-fission']
    tallies_file.append(tally_b)
    # phase1a-c
    mesh_no = 0
    for t in range(6):
        mesh_no += 1
        for x in range(2):
            x_trans = t * T['A1']['P']['x']
            y_trans = t * T['A1']['P']['y']
            if x == 1:
                mesh_no += 1
                x_trans += T['A1']['F']['x']
                y_trans += T['A1']['F']['y']
            mesh_c = openmc.RegularMesh(mesh_id=mesh_no)
            mesh_c.dimension = [1, 5]
            mesh_c.lower_left = [V['A1']['F']['L']['x'] + x_trans,
                                 V['A1']['F']['B']['y'] + y_trans]
            mesh_c.upper_right = [V['A1']['F']['R']['x'] + x_trans,
                                  V['A1']['F']['T']['y'] + y_trans]
            mesh_filter_c = openmc.MeshFilter(mesh_c)
            tally_c = openmc.Tally(name='mesh tally c' + str(mesh_no))
            tally_c.filters = [mesh_filter_c]
            tally_c.scores = ['fission']
            tallies_file.append(tally_c)
    # phase 1a-d
    energy_filter_d = openmc.EnergyFilter([1e-5, 3, 1.0e5, 20.0e6])
    mesh_d = openmc.RegularMesh(mesh_id=13)
    mesh_d.dimension = [1, 1]
    L = 27.02
    mesh_d.lower_left = [-L, -L]
    mesh_d.upper_right = [L, L]
    mesh_filter_d = openmc.MeshFilter(mesh_d)
    tally_d = openmc.Tally(name='mesh tally d')
    tally_d.filters = [mesh_filter_d, energy_filter_d]
    tally_d.scores = ['flux', 'nu-fission', 'fission']
    tallies_file.append(tally_d)
    # phase 1a-e
    energy_filter_e = openmc.EnergyFilter([1e-5, 3, 0.1e6, 20.0e6])
    mesh_e = openmc.RegularMesh(mesh_id=14)
    mesh_e.dimension = [100, 100]
    L = 27.02
    mesh_e.lower_left = [-L, -L]
    mesh_e.upper_right = [L, L]
    mesh_filter_e = openmc.MeshFilter(mesh_e)
    tally_e = openmc.Tally(name='mesh tally e')
    tally_e.filters = [mesh_filter_e, energy_filter_e]
    tally_e.scores = ['flux', 'nu-fission', 'fission']
    tallies_file.append(tally_e)
    # phase 1a-f
    energy_filter_f = openmc.EnergyFilter(engs)
    mesh_f = openmc.RegularMesh(mesh_id=15)
    mesh_f.dimension = [1, 1]
    L = 27.02
    mesh_f.lower_left = [-L, -L]
    mesh_f.upper_right = [L, L]
    mesh_filter_f = openmc.MeshFilter(mesh_f)
    tally_f = openmc.Tally(name='mesh tally f')
    tally_f.filters = [mesh_filter_f, energy_filter_f]
    tally_f.scores = ['flux', 'nu-fission', 'fission']
    tallies_file.append(tally_f)

    tallies_file.export_to_xml()
    return
