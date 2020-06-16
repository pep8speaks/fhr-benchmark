""" Functions for analyzing openmc depletion results

This scripts contains functions for analyzing the depletion results from 
the openmc depletion results file and tallies
from the openmc statepoint files and manipulate the data
into what is required for the depletion section (phase1b) of the FHR benchmark.

"""

import numpy as np
import pylab as pl
import matplotlib.colorbar as cbar
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
sys.path.insert(1, '../../scripts/')
from phase1b_constants import *
from openmc_analysis import *

###############################################################################
#                           Depletion Functions
###############################################################################

def drop_burnups(df):
    for i in df.index:
        if i not in BUs_sheet: 
            df = df.drop([i])
    return df


def depletion_keff(results,type,case):
    time, k = results.get_eigenvalue()
    if type == 'short':
        df_k = pd.DataFrame(index=bu)
    elif type == 'long':
        df_k = pd.DataFrame(index=bu_7b)
    else: 
        raise Exception("Only short and long are excepted.")
    df_k.index.name = 'BU'
    df_k['k'] = k[:,0]
    df_k['kerr'] = k[:,1]
    df_k = drop_burnups(df_k)
    name = 'analysis_output/' + case + '_a.csv'
    df_k.to_csv(name)
    return


def depletion_fission_density_c(burnups,case,particles,type='short'):
    if type == 'short':
        bus = bu.copy()
    elif type == 'long':
        bus = bu_7b.copy()
    else: 
        raise Exception('Only short and long types allowed.')
    for b in burnups: 
        sp = openmc.StatePoint('h5files/'+str(particles)+'p/openmc_simulation_n'+str(np.where(bus == b)[0][0])+'.h5')
        case_loop = case+'_bu_'+str(b)
        fission_density_c(sp,case_loop)
        name = 'analysis_output/' + case_loop + '_c.csv'
        df = pd.read_csv(name,index_col=[0,1])
        df = df.drop(columns=['mean','std. dev.'])
        df = df.drop([np.NaN,'Stripe'])
        if b == 0: 
            df_all = df.copy()
        else: 
            df_all = df_all.join(df,rsuffix='_bu_'+str(b))
        os.remove(name)
    df_all.to_csv('analysis_output/'+ case+'_c.csv')
    return 

def depletion_neutron_flux_d(case,type,particles):
    if type == 'short':
        burnups = BUs_sheet[:18].copy()
        bus = bu.copy()
    elif type == 'long':
        burnups = BUs_sheet.copy()
        bus = bu_7b.copy()
    else: 
        raise Exception('Only short and long types allowed.')
    df_keff = pd.read_csv('analysis_output/' + case + '_a.csv',index_col=0)
    for b in burnups:
        keff = df_keff.loc[b,:][0]
        keff_unc = df_keff.loc[b,:][1]
        sp = openmc.StatePoint('h5files/'+str(particles)+'p/openmc_simulation_n'+str(np.where(bus == b)[0][0])+'.h5')
        case_loop = case+'_bu_'+str(b)
        neutron_flux_d(sp,keff,keff_unc,case_loop)
        name = 'analysis_output/' + case_loop + '_d.csv'
        df = pd.read_csv(name,index_col=[0])
        if b == 0: 
            df_all = df.copy()
        else: 
            df_all = df_all.join(df,rsuffix='_bu_'+str(b))
        os.remove(name)
    df_all.to_csv('analysis_output/'+ case+'_d.csv')
    return


def depletion_neutron_flux_e(burnups,case,particles,type='short'):
    if type == 'short':
        bus = bu.copy()
    elif type == 'long':
        bus = bu_7b.copy()
    else: 
        raise Exception('Only short and long types allowed.')
    df_keff = pd.read_csv('analysis_output/' + case + '_a.csv',index_col=0)
    for b in burnups:
        keff = df_keff.loc[b,:][0]
        sp = openmc.StatePoint('h5files/'+str(particles)+'p/openmc_simulation_n'+str(np.where(bus == b)[0][0])+'.h5')
        case_loop = case+'_bu_'+str(b)
        neutron_flux_e(sp,keff,case_loop)
    for b in burnups: 
        name = 'analysis_output/' + case + '_bu_' + str(b) + '_e'
        for e in range(1,4):
            name_e = name + '_eg'+str(e)+'.csv'
            df = pd.read_csv(name_e,header=None)
            if e == 1: 
                df_all = df.copy()
            else: 
                df_all = df_all.append(df)
            os.remove(name_e)
        df_all.to_csv('analysis_output/' + case + '_e' + '_bu_' + str(b) +'.csv')
    return

def depletion_neutron_spectrum_f(burnups,case,particles,type='short'):
    if type == 'short':
        bus = bu.copy()
    elif type == 'long':
        bus = bu_7b.copy()
    else: 
        raise Exception('Only short and long types allowed.')
    df_keff = pd.read_csv('analysis_output/' + case + '_a.csv',index_col=0)
    for b in burnups: 
        sp = openmc.StatePoint('h5files/'+str(particles)+'p/openmc_simulation_n'+str(np.where(bus == b)[0][0])+'.h5')
        case_loop = case+'_f_bu_'+str(b)
        keff = df_keff.loc[b,:][0]
        keff_unc = df_keff.loc[b,:][1]
        neutron_spectrum_f(sp,case_loop,keff,keff_unc)
    return

def depletion_actinides(results,case,type='short'):
    if type == 'short':
        bus = bu.copy()
    elif type == 'long':
        bus = bu_7b.copy()
    else: 
        raise Exception('Only short and long types allowed.')
    df = pd.DataFrame(index=bus[:np.shape(results.get_atoms("1", 'U235'))[1]])
    df.index.name = 'BU'
    for a in actinides: 
        _time, df[a] = results.get_atoms("1", a, "atom/b-cm")
    df = drop_burnups(df)
    df = df.transpose()
    df.to_csv('analysis_output/'+case+'_g_actinides.csv')
    return

def depletion_fp(results,case,type='short'):
    if type == 'short':
        bus = bu.copy()
    elif type == 'long':
        bus = bu_7b.copy()
    else: 
        raise Exception('Only short and long types allowed.')
    df = pd.DataFrame(index=bus[:np.shape(results.get_atoms("1", 'U235'))[1]])
    df.index.name = 'BU'
    for f in fp: 
        _time, df[f] = results.get_atoms("1", f, "atom/b-cm")
    df = drop_burnups(df)
    df = df.transpose()
    df.to_csv('analysis_output/'+case+'_g_fission_products.csv')
    return

def depletion_extended(results,case,type='short'):
    if type == 'short':
        bus = bu.copy()
    elif type == 'long':
        bus = bu_7b.copy()
    else: 
        raise Exception('Only short and long types allowed.')
    df = pd.DataFrame(index=bus[:np.shape(results.get_atoms("1", 'U235'))[1]])
    df.index.name = 'BU'
    for e in extended_list: 
        _time, df[e] = results.get_atoms("1", e, "atom/b-cm")
    df = drop_burnups(df)
    df = df.transpose()
    df.to_csv('analysis_output/'+case+'_g_extended_list.csv')
    return


def depletion_eu(results,case):
    df = pd.DataFrame(index=bu[:np.shape(results.get_atoms("10", 'Eu151'))[1]])
    df.index.name = 'BU'
    for e in europium: 
        _time, df[e] = results.get_atoms("10", e, "atom/b-cm")
    df = drop_burnups(df)
    df = df.transpose()
    df.to_csv('analysis_output/'+case+'_g_europium.csv')
    return
