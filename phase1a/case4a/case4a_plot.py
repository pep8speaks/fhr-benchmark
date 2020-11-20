from case4a_build_xml import *
import openmc 

# create plot.xml 
colors = {
    uoc_9: 'yellow', 
    por_c: 'black',
    si_c: 'orange',
    graphite: 'grey', 
    p_graphite:'red',
    flibe: 'blue',
    lm_graphite: 'green',
    s_graphite: 'pink', 
    mhc: 'black',
    euo_s: 'darkolivegreen'
}

twod_plot = openmc.Plot() 
twod_plot.filename = 'full_2d_plot'
twod_plot.basis = 'xy'
twod_plot.width = (55., 55.)
twod_plot.pixels = (2000, 2000)
twod_plot.color_by = 'material'
twod_plot.colors = colors 
twod_plot.origin = (0, 0, 0)

plots = openmc.Plots([twod_plot])
plots.export_to_xml()