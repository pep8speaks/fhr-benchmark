from pyne import data
import pandas as pd
import numpy as np


def reactor_power(sp_power, particles):
    """Returns the FHR's power

    Parameters
    ----------
    sp_power: float
        specific power of reactor [W/gU]
    particles: int
        number of triso particles in each fuel stripes's y-direction

    Returns
    -------
    t_u: float
        mass of Uranium [metric tonnes]
    power: float
        power of reactor [W]
    """

    wtp_u = ((0.00227325 * data.atomic_mass('U235')) +
             (0.02269476 * data.atomic_mass('U238'))) / \
            (0.00227325 * data.atomic_mass('U235') +
             0.02269476 * data.atomic_mass('U238') +
             0.03561871 * data.atomic_mass('O16') +
             0.00979714 * data.atomic_mass('C0')) * 100  # %
    V = (101 * 210 * particles * 36 * 4 / 3 * np.pi * (2135e-5)**3)  # cm3
    density = 11  # g/cc
    grams_u = V * density * (wtp_u) / 100  # gU
    t_u = grams_u * 1e-6  # t
    power = grams_u * sp_power  # W

    return t_u, power
