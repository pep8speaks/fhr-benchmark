# FHR Benchmark 
This respository comprises of UIUC AFRC's contribution to the OECD Fluoride-salt High-temperature Reactor (FHR) Benchmark using the OpenMC code. Brief description of the benchmark is provided here: https://www.oecd-nea.org/science/wprs/fhr/index.html. Full description of the benchmark specification must be requested through the OECD. 

Relevant Papers of similar reactor geometries include: 
1) B. Petrovic, T. Flaspoehler, K. Ramey, “Benchmarking FHR Core Physics Simulations: 2D Fuel Assembly Model,” Proc. 12th Intl. Conf. on Nuclear Option in Countries with Small and Medium Electricity Grids, Zadar, Croatia, June 3-6, 2018.
2) K. Ramey, B. Petrovic, “Monte Carlo Modeling and Simulations of AHTR Fuel Assembly to Support V&V of FHR Core Physics Methods,” Annals of Nuclear Energy, 118, 272-282 (2018).
3) V.K. Varma, D.E. Holcomb, F.J. Peretz, E.C. Bradley, D. Ilas, A.L. Qualls, N.M. Zaharia, “AHTR Mechanical, Structural, and Neutronic Preconceptual Design,” ORNL/TM-2012/320, Oak Ridge National Laboratory (2011).

## OpenMC Dependency
To run the simulations in this repository required for the benchmark, you must have 
OpenMC installed on your local machine and on BlueWaters. 
OpenMC Installation Guide: https://docs.openmc.org/en/stable/quickinstall.html

### OpenMC Version used for this benchmark 
I installed OpenMC from source (0.12-dev) on both my local machine and on BlueWaters. 

A slight alteration was made to the source code on BlueWaters to enable running OpenMC on BlueWaters (the full issue is described here: https://groups.google.com/forum/#!topic/openmc-users/xHKYV-EBgrY). The alteration was in openmc's `pool.py` script (https://github.com/openmc-dev/openmc/blob/develop/openmc/deplete/pool.py), in which the pool.starmap function is replaced by itertools.starmap to remove openmc's reliance on multiprocessing pool.  

For ARFC members, this altered version of OpenMC is compiled in our group's BBCC directory in the /projects/openmc/openmc-parallel-python/ directory. 
