# FHR Benchmark 
To run the simulations in this repository required for the benchmark, you must have 
OpenMC installed on your local machine and on BlueWaters. 
OpenMC Installation Guide: https://docs.openmc.org/en/stable/quickinstall.html

## OpenMC Version used for this benchmark 
I installed OpenMC from source (0.12-dev) on both my local machine and on BlueWaters. 

A slight alteration was made to the source code on BlueWaters to enable running OpenMC on BlueWaters (the full issue is described here: https://groups.google.com/forum/#!topic/openmc-users/xHKYV-EBgrY). The alteration was in openmc's `pool.py` script (https://github.com/openmc-dev/openmc/blob/develop/openmc/deplete/pool.py), in which the pool.starmap function is replaced by itertools.starmap to remove openmc's reliance on multiprocessing pool.  

For ARFC members, this altered version of OpenMC is compiled in our group's BBCC directory in the /projects/openmc/openmc-parallel-python/ directory. 
