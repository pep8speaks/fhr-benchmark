""" Constants and functions for FHR benchmark geometry generation

This script contains the values for constants and functions used to
set up the FHR benchmark geometry.

"""

import numpy as np
from numpy import sin, cos, tan, pi
import openmc

###############################################################################
#                               Constants
###############################################################################

H_side = 22.5 / sin(pi / 3)
P_len = 23.1  # plank length
P_D_jut = 2 - 1.4948
P_D_jut_hyp = P_D_jut / sin(pi / 3)
P_D_jut_adj = P_D_jut / sin(pi / 3)
P_small_gap = 0.35
P_A1_height = 2.55
P_A1_adj = P_A1_height / tan(pi / 3)
P_big_gap = 0.7
P_A2_hyp = P_A1_height / sin(pi / 3)
P_big_gap_A2_hyp = P_big_gap / sin(pi / 3)
P_A3_hyp = P_A1_height / sin(pi / 3)
P_big_gap_A3_hyp = P_big_gap / sin(pi / 3)
D_to_center = 2
D_to_center_width = D_to_center * tan(pi / 6)
D_A1_width = P_len - 2 * (P_D_jut)
D_A1_height = 19.5
D_A1_adj = D_A1_height / tan(pi / 3)
T_pitch = 0.09266
T_r1 = 2135e-5
T_r2 = 3135e-5
T_r3 = 3485e-5
T_r4 = 3835e-5
T_r5 = 4235e-5
F_protect_gap = 0.1
F_width = T_pitch * (4)
F_len = T_pitch * (210)
F_A1_D_gap = (D_A1_width - F_len) / 2
F_F_gap = P_A1_height - 2 * F_width - 2 * F_protect_gap
F_F_gap_adj = F_F_gap / tan(pi / 3)
F_A1_width_adj = F_width / tan(pi / 3)
F_F_gap_A2_hyp = F_F_gap / sin(pi / 3)
F_A2_width_hyp = F_width / sin(pi / 3)
F_F_gap_A3_hyp = F_F_gap / sin(pi / 3)
F_F_gap_A3_adj = F_F_gap_A3_hyp * cos(pi / 3)
F_F_gap_A3_opp = F_F_gap_A3_hyp * sin(pi / 3)
F_A3_width_adj = F_width * cos(pi / 3)
F_A3_width_opp = F_width * sin(pi / 3)
S_S_gap = 14
S_A1_D_gap = (D_A1_width - S_S_gap) / 2
S_large_r = 0.7
S_small_r = 0.35
CS_l = 10.38
CS_w = 1.76
CA_l = 10
CA_w = 1
z_thickness = 101  # no. of triso particle thickness, must be odd

DE_r = 0.035
DE_pitch = 0.09266
DE_gap = 4
DE_mid = D_A1_width / 2

# 252 energy groups
engs = [1.00E-11, 1.00E-10, 5.00E-10, 7.50E-10, 1.00E-09, 1.20E-09,
        1.50E-09, 2.00E-09, 2.50E-09, 3.00E-09, 4.00E-09, 5.00E-09,
        7.50E-09, 1.00E-08, 2.53E-08, 3.00E-08, 4.00E-08, 5.00E-08,
        6.00E-08, 7.00E-08, 8.00E-08, 9.00E-08, 1.00E-07, 1.25E-07,
        1.50E-07, 1.75E-07, 2.00E-07, 2.25E-07, 2.50E-07, 2.75E-07,
        3.00E-07, 3.25E-07, 3.50E-07, 3.75E-07, 4.00E-07, 4.50E-07,
        5.00E-07, 5.50E-07, 6.00E-07, 6.25E-07, 6.50E-07, 7.00E-07,
        7.50E-07, 8.00E-07, 8.50E-07, 9.00E-07, 9.25E-07, 9.50E-07,
        9.75E-07, 1.00E-06, 1.01E-06, 1.02E-06, 1.03E-06, 1.04E-06,
        1.05E-06, 1.06E-06, 1.07E-06, 1.08E-06, 1.09E-06, 1.10E-06,
        1.11E-06, 1.12E-06, 1.13E-06, 1.14E-06, 1.15E-06, 1.18E-06,
        1.20E-06, 1.23E-06, 1.25E-06, 1.30E-06, 1.35E-06, 1.40E-06,
        1.45E-06, 1.50E-06, 1.59E-06, 1.68E-06, 1.77E-06, 1.86E-06,
        1.94E-06, 2.00E-06, 2.12E-06, 2.21E-06, 2.30E-06, 2.38E-06,
        2.47E-06, 2.57E-06, 2.67E-06, 2.77E-06, 2.87E-06, 2.97E-06,
        3.00E-06, 3.10E-06, 3.20E-06, 3.50E-06, 3.73E-06, 4.10E-06,
        4.70E-06, 5.00E-06, 5.40E-06, 6.00E-06, 6.25E-06, 6.50E-06,
        6.75E-06, 6.88E-06, 7.00E-06, 7.15E-06, 8.10E-06, 9.10E-06,
        1.00E-05, 1.15E-05, 1.19E-05, 1.29E-05, 1.44E-05, 1.60E-05,
        1.70E-05, 1.85E-05, 1.94E-05, 2.00E-05, 2.05E-05, 2.12E-05,
        2.18E-05, 2.25E-05, 2.50E-05, 2.75E-05, 3.00E-05, 3.13E-05,
        3.18E-05, 3.33E-05, 3.38E-05, 3.50E-05, 3.55E-05, 3.60E-05,
        3.70E-05, 3.71E-05, 3.73E-05, 3.76E-05, 3.80E-05, 3.91E-05,
        3.96E-05, 4.10E-05, 4.24E-05, 4.40E-05, 4.52E-05, 4.83E-05,
        5.06E-05, 5.34E-05, 5.80E-05, 6.10E-05, 6.30E-05, 6.50E-05,
        6.75E-05, 7.20E-05, 7.60E-05, 8.00E-05, 8.17E-05, 9.00E-05,
        9.70E-05, 1.01E-04, 1.05E-04, 1.08E-04, 1.13E-04, 1.16E-04,
        1.18E-04, 1.19E-04, 1.22E-04, 1.43E-04, 1.70E-04, 1.80E-04,
        1.88E-04, 1.89E-04, 1.92E-04, 1.93E-04, 2.02E-04, 2.07E-04,
        2.10E-04, 2.20E-04, 2.40E-04, 2.85E-04, 3.05E-04, 5.50E-04,
        6.70E-04, 6.83E-04, 9.50E-04, 1.15E-03, 1.50E-03, 1.55E-03,
        1.80E-03, 2.20E-03, 2.25E-03, 2.50E-03, 3.00E-03, 3.74E-03,
        3.90E-03, 5.70E-03, 8.03E-03, 9.50E-03, 1.30E-02, 1.70E-02,
        2.00E-02, 3.00E-02, 4.50E-02, 5.00E-02, 5.20E-02, 6.00E-02,
        7.30E-02, 7.50E-02, 8.20E-02, 8.50E-02, 1.00E-01, 1.28E-01,
        1.49E-01, 2.00E-01, 2.70E-01, 3.30E-01, 4.00E-01, 4.20E-01,
        4.40E-01, 4.70E-01, 4.92E-01, 5.50E-01, 5.73E-01, 6.00E-01,
        6.70E-01, 6.79E-01, 7.50E-01, 8.20E-01, 8.61E-01, 8.75E-01,
        9.00E-01, 9.20E-01, 1.01E+00, 1.10E+00, 1.20E+00, 1.25E+00,
        1.32E+00, 1.36E+00, 1.40E+00, 1.50E+00, 1.85E+00, 2.35E+00,
        2.48E+00, 3.00E+00, 4.30E+00, 4.80E+00, 6.43E+00, 8.19E+00,
        1.00E+01, 1.28E+01, 1.38E+01, 1.46E+01, 1.57E+01, 1.73E+01,
        2.00E+01]
engs = [x * 1e6 for x in engs]

###############################################################################
#                                  Functions
###############################################################################


def plane(m, x, y, bc='transmission'):
    """ Creates openmc plane

    Parameters
    ----------
    m: float
        gradient of plane
    x: float
        x-intercept
    y: float
        y-intercept
    bc: str
        boundary condition

    Returns
    -------
    openmc.Plane
    """

    return openmc.Plane(a=-m, b=1, d=-m * x + y, boundary_type=bc)


def region_maker(area,area_type):
    """ Creates 2D openmc.region.Intersection on x-y plane 

    Parameters
    ----------
    area: str 
        This refers to the 3 diamond sections in the FHR geometry. Options are:
        'A1', 'A2', 'A3'
    area_type: str
        This refers to the various areas within each quadrant. 
        Diamond Plank Area: 'D', Plank Area: 'P', Fuel Area: 'F' 
        Spacers: 'S', Control Rod Slot: 'CS', Control Rod Arm: 'CA' 

    Returns
    -------
    openmc.region.Intersection
    """

    if area in ['A1','A3']:
        if V[area][area_type]['L']['m'] == 0.0 and V[area][area_type]['R']['m'] == 0.0: 
            region = -plane(V[area][area_type]['T']['m'],V[area][area_type]['T']['x'],V[area][area_type]['T']['y']) &\
                     +plane(V[area][area_type]['B']['m'],V[area][area_type]['B']['x'],V[area][area_type]['B']['y']) &\
                     +openmc.XPlane(x0=V[area][area_type]['L']['x']) &\
                     -openmc.XPlane(x0=V[area][area_type]['R']['x'])     
        else: 
            region = -plane(V[area][area_type]['T']['m'],V[area][area_type]['T']['x'],V[area][area_type]['T']['y']) &\
                     +plane(V[area][area_type]['B']['m'],V[area][area_type]['B']['x'],V[area][area_type]['B']['y']) &\
                     +plane(V[area][area_type]['L']['m'],V[area][area_type]['L']['x'],V[area][area_type]['L']['y']) &\
                     -plane(V[area][area_type]['R']['m'],V[area][area_type]['R']['x'],V[area][area_type]['R']['y']) 
        
    elif area in ['A2']:
        region = -plane(V[area][area_type]['T']['m'],V[area][area_type]['T']['x'],V[area][area_type]['T']['y']) &\
                 +plane(V[area][area_type]['B']['m'],V[area][area_type]['B']['x'],V[area][area_type]['B']['y']) &\
                 -plane(V[area][area_type]['L']['m'],V[area][area_type]['L']['x'],V[area][area_type]['L']['y']) &\
                 +plane(V[area][area_type]['R']['m'],V[area][area_type]['R']['x'],V[area][area_type]['R']['y']) 
    else: 
        raise Exception('Your region type has yet to be defined.')

    return region 


def rx(x_i, y_i, t):
    """ Rotates x on x-y plane counterclockwise
    through a specified angle with respect to the x axis about the
    origin of a 2D cartesian coordinate system.

    Parameters
    ----------
    x_i float
        x value to rotate
    y_i: float
        y value to rotate
    t: float
        angle to rotate about origin

    Returns
    -------
    rotated x value
    """

    return x_i * cos(t) - y_i * sin(t)


def ry(x_i, y_i, t):
    """ Rotates y on x-y plane counterclockwise
    through a specified angle with respect to the x axis about the
    origin of a 2D cartesian coordinate system.

    Parameters
    ----------
    x_i float
        x value to rotate
    y_i: float
        y value to rotate
    t: float
        angle to rotate about origin

    Returns
    -------
    rotated y value
    """
    return x_i * sin(t) + y_i * cos(t)

###############################################################################
#                             Geometry for Planes
# The V (values) dictionary organizes the x-intercept, y-intercept, and
# gradient values required to create the planes that set up the regions for
# various areas of the FHR geometry.
# Example V format: V[level1][level2][level3][level4]
# level1: 3 diamond sections in the FHR geometry. Options are: 'A1', 'A2', 'A3'
# level2: various areas within each quadrant. Options are:
#         Diamond Plank Area: 'D', Plank Area: 'P', Fuel Area: 'F'
#         Spacers: 'S', Control Rod Slot: 'CS', Control Rod Arm: 'CA'
# level3: plane position relative to area. Options are:
#         Top: 'T', Bottom: 'B', Left: 'L', Right: 'R'
# level4: gradient, x-intercept, or y-intercept value. Options are:
#         gradient: 'm', x-intercept: 'x', y-intercept: 'y'
###############################################################################


m1 = -D_A1_height / D_A1_adj
m2 = D_A1_width * sin(pi / 3) / (D_A1_width * cos(pi / 3))

V = {'A1': {}, 'A2': {}, 'A3': {}}

V['A1'] = {'D': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'P': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'F': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'S': {'C': {}, 'Cb': {}},
           'CS': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'CA': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'DE': {'T': {}, 'B': {}, 'L': {}, 'R': {}}}
V['A2'] = {'D': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'P': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'F': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'S': {'C': {}, 'Cb': {}},
           'CS': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'CA': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'DE': {'T': {}, 'B': {}, 'L': {}, 'R': {}}}
V['A3'] = {'D': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'P': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'F': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'S': {'C': {}, 'Cb': {}},
           'CS': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'CA': {'T': {}, 'B': {}, 'L': {}, 'R': {}},
           'DE': {'T': {}, 'B': {}, 'L': {}, 'R': {}}}

V['A1']['D']['T'] = {'m': 0, 'x': 0, 'y': -D_to_center}
V['A1']['D']['B'] = {'m': 0, 'x': 0, 'y': -D_to_center - D_A1_height}
V['A1']['D']['R'] = {'m': m1, 'x': -D_to_center_width, 'y': -D_to_center}
V['A1']['D']['L'] = {'m': m1, 'x': V['A1']['D']
                     ['R']['x'] - D_A1_width, 'y': -D_to_center}

V['A1']['P']['T'] = {'m': 0, 'x': 0, 'y': V['A1']['D']['T']['y'] - P_small_gap}
V['A1']['P']['B'] = {'m': 0, 'x': 0, 'y': V['A1']['P']['T']['y'] - P_A1_height}
V['A1']['P']['R'] = {'m': m1, 'x': V['A1']['D']['R']['x'] + P_small_gap *
                     tan(pi / 6) + P_D_jut_hyp, 'y': V['A1']['D']['R']['y'] - P_small_gap}
V['A1']['P']['L'] = {'m': m1, 'x': V['A1']['D']['L']['x'] + P_small_gap *
                     tan(pi / 6) - P_D_jut_hyp, 'y': V['A1']['D']['L']['y'] - P_small_gap}

V['A1']['F']['T'] = {'m': 0, 'x': V['A1']['D']['R']['x'] -
                     F_A1_D_gap, 'y': V['A1']['P']['T']['y'] - F_protect_gap}
V['A1']['F']['B'] = {'m': 0, 'x': V['A1']['F']['T']
                     ['x'], 'y': V['A1']['F']['T']['y'] - F_width}
V['A1']['F']['R'] = {'m': 0, 'x': V['A1']['D']['R']
                     ['x'] - F_A1_D_gap, 'y': V['A1']['F']['T']['y']}
V['A1']['F']['L'] = {'m': 0, 'x': V['A1']['D']['L']
                     ['x'] + F_A1_D_gap, 'y': V['A1']['F']['T']['y']}

V['A1']['S']['C'] = {
    'x0': -D_to_center_width - S_A1_D_gap,
    'y0': -D_to_center - P_small_gap}
V['A1']['S']['Cb'] = {
    'x0': -D_to_center_width - S_A1_D_gap + P_A1_adj,
    'y0': -D_to_center - P_small_gap - P_A1_height}

V['A1']['CS']['T'] = {'m': 0, 'x': 0, 'y': CS_w / 2}
V['A1']['CS']['B'] = {'m': 0, 'x': 0, 'y': -CS_w / 2}
V['A1']['CS']['R'] = {'m': 0, 'x': 0, 'y': 0}
V['A1']['CS']['L'] = {'m': 0, 'x': -CS_l, 'y': 0}

V['A1']['CA']['T'] = {'m': 0, 'x': 0, 'y': CA_w / 2}
V['A1']['CA']['B'] = {'m': 0, 'x': 0, 'y': -CA_w / 2}
V['A1']['CA']['R'] = {'m': 0, 'x': 0, 'y': 0}
V['A1']['CA']['L'] = {'m': 0, 'x': -CA_l, 'y': 0}

V['A1']['DE']['L'] = {'m': 0, 'x': V['A1']['P']['R']['x'] + P_A1_height /
                      2 / tan(pi / 3) - DE_mid - 10, 'y': V['A1']['P']['T']['y'] - P_A1_height / 2}

A2_t = -pi / 3 * 2
V['A2']['D']['T'] = {
    'm': 0,
    'x': rx(
        V['A1']['D']['L']['x'],
        V['A1']['D']['L']['y'],
        A2_t),
    'y': ry(
        V['A1']['D']['L']['x'],
        V['A1']['D']['L']['y'],
        A2_t)}
V['A2']['D']['B'] = {
    'm': 0,
    'x': rx(
        V['A1']['D']['R']['x'],
        V['A1']['D']['R']['y'],
        A2_t),
    'y': ry(
        V['A1']['D']['R']['x'],
        V['A1']['D']['R']['y'],
        A2_t)}
V['A2']['D']['R'] = {
    'm': m2,
    'x': rx(
        V['A1']['D']['T']['x'],
        V['A1']['D']['T']['y'],
        A2_t),
    'y': ry(
        V['A1']['D']['T']['x'],
        V['A1']['D']['T']['y'],
        A2_t)}
V['A2']['D']['L'] = {
    'm': m2,
    'x': rx(
        V['A1']['D']['B']['x'],
        V['A1']['D']['B']['y'],
        A2_t),
    'y': ry(
        V['A1']['D']['B']['x'],
        V['A1']['D']['B']['y'],
        A2_t)}

V['A2']['P']['T'] = {
    'm': 0,
    'x': rx(
        V['A1']['P']['L']['x'],
        V['A1']['P']['L']['y'],
        A2_t),
    'y': ry(
        V['A1']['P']['L']['x'],
        V['A1']['P']['L']['y'],
        A2_t)}
V['A2']['P']['B'] = {
    'm': 0,
    'x': rx(
        V['A1']['P']['R']['x'],
        V['A1']['P']['R']['y'],
        A2_t),
    'y': ry(
        V['A1']['P']['R']['x'],
        V['A1']['P']['R']['y'],
        A2_t)}
V['A2']['P']['R'] = {
    'm': m2,
    'x': rx(
        V['A1']['P']['T']['x'],
        V['A1']['P']['T']['y'],
        A2_t),
    'y': ry(
        V['A1']['P']['T']['x'],
        V['A1']['P']['T']['y'],
        A2_t)}
V['A2']['P']['L'] = {
    'm': m2,
    'x': rx(
        V['A1']['P']['B']['x'],
        V['A1']['P']['B']['y'],
        A2_t),
    'y': ry(
        V['A1']['P']['B']['x'],
        V['A1']['P']['B']['y'],
        A2_t)}

V['A2']['F']['T'] = {
    'm': -1 / m2,
    'x': rx(
        V['A1']['F']['L']['x'],
        V['A1']['F']['L']['y'],
        A2_t),
    'y': ry(
        V['A1']['F']['L']['x'],
        V['A1']['F']['L']['y'],
        A2_t)}
V['A2']['F']['B'] = {
    'm': -1 / m2,
    'x': rx(
        V['A1']['F']['R']['x'],
        V['A1']['F']['R']['y'],
        A2_t),
    'y': ry(
        V['A1']['F']['R']['x'],
        V['A1']['F']['R']['y'],
        A2_t)}
V['A2']['F']['R'] = {
    'm': m2,
    'x': rx(
        V['A1']['F']['T']['x'],
        V['A1']['F']['T']['y'],
        A2_t),
    'y': ry(
        V['A1']['F']['T']['x'],
        V['A1']['F']['T']['y'],
        A2_t)}
V['A2']['F']['L'] = {
    'm': m2,
    'x': rx(
        V['A1']['F']['B']['x'],
        V['A1']['F']['B']['y'],
        A2_t),
    'y': ry(
        V['A1']['F']['B']['x'],
        V['A1']['F']['B']['y'],
        A2_t)}

V['A2']['S']['C'] = {
    'x0': rx(
        V['A1']['S']['C']['x0'],
        V['A1']['S']['C']['y0'],
        A2_t),
    'y0': ry(
        V['A1']['S']['C']['x0'],
        V['A1']['S']['C']['y0'],
        A2_t)}
V['A2']['S']['Cb'] = {
    'x0': rx(
        V['A1']['S']['Cb']['x0'],
        V['A1']['S']['Cb']['y0'],
        A2_t),
    'y0': ry(
        V['A1']['S']['Cb']['x0'],
        V['A1']['S']['Cb']['y0'],
        A2_t)}

V['A2']['CS']['T'] = {
    'm': -1 / m2,
    'x': rx(
        V['A1']['CS']['L']['x'],
        V['A1']['CS']['L']['y'],
        A2_t),
    'y': ry(
        V['A1']['CS']['L']['x'],
        V['A1']['CS']['L']['y'],
        A2_t)}
V['A2']['CS']['B'] = {
    'm': -1 / m2,
    'x': rx(
        V['A1']['CS']['R']['x'],
        V['A1']['CS']['R']['y'],
        A2_t),
    'y': ry(
        V['A1']['CS']['R']['x'],
        V['A1']['CS']['R']['y'],
        A2_t)}
V['A2']['CS']['R'] = {
    'm': m2,
    'x': rx(
        V['A1']['CS']['T']['x'],
        V['A1']['CS']['T']['y'],
        A2_t),
    'y': ry(
        V['A1']['CS']['T']['x'],
        V['A1']['CS']['T']['y'],
        A2_t)}
V['A2']['CS']['L'] = {
    'm': m2,
    'x': rx(
        V['A1']['CS']['B']['x'],
        V['A1']['CS']['B']['y'],
        A2_t),
    'y': ry(
        V['A1']['CS']['B']['x'],
        V['A1']['CS']['B']['y'],
        A2_t)}

V['A2']['CA']['T'] = {
    'm': -1 / m2,
    'x': rx(
        V['A1']['CA']['L']['x'],
        V['A1']['CA']['L']['y'],
        A2_t),
    'y': ry(
        V['A1']['CA']['L']['x'],
        V['A1']['CA']['L']['y'],
        A2_t)}
V['A2']['CA']['B'] = {
    'm': -1 / m2,
    'x': rx(
        V['A1']['CA']['R']['x'],
        V['A1']['CA']['R']['y'],
        A2_t),
    'y': ry(
        V['A1']['CA']['R']['x'],
        V['A1']['CA']['R']['y'],
        A2_t)}
V['A2']['CA']['R'] = {
    'm': m2,
    'x': rx(
        V['A1']['CA']['T']['x'],
        V['A1']['CA']['T']['y'],
        A2_t),
    'y': ry(
        V['A1']['CA']['T']['x'],
        V['A1']['CA']['T']['y'],
        A2_t)}
V['A2']['CA']['L'] = {
    'm': m2,
    'x': rx(
        V['A1']['CA']['B']['x'],
        V['A1']['CA']['B']['y'],
        A2_t),
    'y': ry(
        V['A1']['CA']['B']['x'],
        V['A1']['CA']['B']['y'],
        A2_t)}

A3_t = pi / 3 * 2
V['A3']['D']['T'] = {
    'm': m2,
    'x': rx(
        V['A1']['D']['R']['x'],
        V['A1']['D']['R']['y'],
        A3_t),
    'y': ry(
        V['A1']['D']['R']['x'],
        V['A1']['D']['R']['y'],
        A3_t)}
V['A3']['D']['B'] = {
    'm': m2,
    'x': rx(
        V['A1']['D']['L']['x'],
        V['A1']['D']['L']['y'],
        A3_t),
    'y': ry(
        V['A1']['D']['L']['x'],
        V['A1']['D']['L']['y'],
        A3_t)}
V['A3']['D']['R'] = {
    'm': m1,
    'x': rx(
        V['A1']['D']['B']['x'],
        V['A1']['D']['B']['y'],
        A3_t),
    'y': ry(
        V['A1']['D']['B']['x'],
        V['A1']['D']['B']['y'],
        A3_t)}
V['A3']['D']['L'] = {
    'm': m1,
    'x': rx(
        V['A1']['D']['T']['x'],
        V['A1']['D']['T']['y'],
        A3_t),
    'y': ry(
        V['A1']['D']['T']['x'],
        V['A1']['D']['T']['y'],
        A3_t)}

V['A3']['P']['T'] = {
    'm': m2,
    'x': rx(
        V['A1']['P']['R']['x'],
        V['A1']['P']['R']['y'],
        A3_t),
    'y': ry(
        V['A1']['P']['R']['x'],
        V['A1']['P']['R']['y'],
        A3_t)}
V['A3']['P']['B'] = {
    'm': m2,
    'x': rx(
        V['A1']['P']['L']['x'],
        V['A1']['P']['L']['y'],
        A3_t),
    'y': ry(
        V['A1']['P']['L']['x'],
        V['A1']['P']['L']['y'],
        A3_t)}
V['A3']['P']['R'] = {
    'm': m1,
    'x': rx(
        V['A1']['P']['B']['x'],
        V['A1']['P']['B']['y'],
        A3_t),
    'y': ry(
        V['A1']['P']['B']['x'],
        V['A1']['P']['B']['y'],
        A3_t)}
V['A3']['P']['L'] = {
    'm': m1,
    'x': rx(
        V['A1']['P']['T']['x'],
        V['A1']['P']['T']['y'],
        A3_t),
    'y': ry(
        V['A1']['P']['T']['x'],
        V['A1']['P']['T']['y'],
        A3_t)}

V['A3']['F']['T'] = {
    'm': -1 / m1,
    'x': rx(
        V['A1']['F']['R']['x'],
        V['A1']['F']['R']['y'],
        A3_t),
    'y': ry(
        V['A1']['F']['R']['x'],
        V['A1']['F']['R']['y'],
        A3_t)}
V['A3']['F']['B'] = {
    'm': -1 / m1,
    'x': rx(
        V['A1']['F']['L']['x'],
        V['A1']['F']['L']['y'],
        A3_t),
    'y': ry(
        V['A1']['F']['L']['x'],
        V['A1']['F']['L']['y'],
        A3_t)}
V['A3']['F']['R'] = {
    'm': m1,
    'x': rx(
        V['A1']['F']['B']['x'],
        V['A1']['F']['B']['y'],
        A3_t),
    'y': ry(
        V['A1']['F']['B']['x'],
        V['A1']['F']['B']['y'],
        A3_t)}
V['A3']['F']['L'] = {
    'm': m1,
    'x': rx(
        V['A1']['F']['T']['x'],
        V['A1']['F']['T']['y'],
        A3_t),
    'y': ry(
        V['A1']['F']['T']['x'],
        V['A1']['F']['T']['y'],
        A3_t)}

V['A3']['S']['C'] = {
    'x0': rx(
        V['A1']['S']['C']['x0'],
        V['A1']['S']['C']['y0'],
        A3_t),
    'y0': ry(
        V['A1']['S']['C']['x0'],
        V['A1']['S']['C']['y0'],
        A3_t)}
V['A3']['S']['Cb'] = {
    'x0': rx(
        V['A1']['S']['Cb']['x0'],
        V['A1']['S']['Cb']['y0'],
        A3_t),
    'y0': ry(
        V['A1']['S']['Cb']['x0'],
        V['A1']['S']['Cb']['y0'],
        A3_t)}

V['A3']['CS']['T'] = {
    'm': -1 / m1,
    'x': rx(
        V['A1']['CS']['R']['x'],
        V['A1']['CS']['R']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['R']['x'],
        V['A1']['CA']['R']['y'],
        A3_t)}
V['A3']['CS']['B'] = {
    'm': -1 / m1,
    'x': rx(
        V['A1']['CS']['L']['x'],
        V['A1']['CS']['L']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['L']['x'],
        V['A1']['CA']['L']['y'],
        A3_t)}
V['A3']['CS']['R'] = {
    'm': m1,
    'x': rx(
        V['A1']['CS']['B']['x'],
        V['A1']['CS']['B']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['B']['x'],
        V['A1']['CA']['B']['y'],
        A3_t)}
V['A3']['CS']['L'] = {
    'm': m1,
    'x': rx(
        V['A1']['CS']['T']['x'],
        V['A1']['CS']['T']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['T']['x'],
        V['A1']['CA']['T']['y'],
        A3_t)}

V['A3']['CA']['T'] = {
    'm': -1 / m1,
    'x': rx(
        V['A1']['CA']['R']['x'],
        V['A1']['CA']['R']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['R']['x'],
        V['A1']['CA']['R']['y'],
        A3_t)}
V['A3']['CA']['B'] = {
    'm': -1 / m1,
    'x': rx(
        V['A1']['CA']['L']['x'],
        V['A1']['CA']['L']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['L']['x'],
        V['A1']['CA']['L']['y'],
        A3_t)}
V['A3']['CA']['R'] = {
    'm': m1,
    'x': rx(
        V['A1']['CA']['B']['x'],
        V['A1']['CA']['B']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['B']['x'],
        V['A1']['CA']['B']['y'],
        A3_t)}
V['A3']['CA']['L'] = {
    'm': m1,
    'x': rx(
        V['A1']['CA']['T']['x'],
        V['A1']['CA']['T']['y'],
        A3_t),
    'y': ry(
        V['A1']['CA']['T']['x'],
        V['A1']['CA']['T']['y'],
        A3_t)}


###############################################################################
#                            Translation for Planes
###############################################################################
T = {
    'A1': {
        'P': {}, 'F': {}, 'S': {}}, 'A2': {
            'P': {}, 'F': {}, 'S': {}}, 'A3': {
                'P': {}, 'F': {}, 'S': {}}}

T['A1']['P'] = {'x': (P_big_gap + P_A1_height) /
                tan(pi / 3), 'y': -(P_big_gap + P_A1_height)}
T['A2']['P'] = {'x': -P_A2_hyp - P_big_gap_A2_hyp, 'y': 0}
T['A3']['P'] = {'x': (P_A3_hyp + P_big_gap_A3_hyp) * cos(pi / 3),
                'y': (P_A3_hyp + P_big_gap_A3_hyp) * sin(pi / 3)}

T['A1']['F'] = {'x': F_F_gap_adj + F_A1_width_adj, 'y': -F_F_gap - F_width}
T['A2']['F'] = {'x': -F_F_gap_A2_hyp - F_A2_width_hyp, 'y': 0}
T['A3']['F'] = {
    'x': F_F_gap_A3_adj + F_A3_width_adj,
    'y': F_F_gap_A3_opp + F_A3_width_opp}

T['A1']['S'] = {'x': -S_S_gap, 'y': 0}
T['A2']['S'] = {'x': S_S_gap * cos(pi / 3), 'y': S_S_gap * sin(pi / 3)}
T['A3']['S'] = {'x': S_S_gap * cos(pi / 3), 'y': -S_S_gap * sin(pi / 3)}
