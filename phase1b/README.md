# FHR Benchmark Phase IB
This description in this README applies to each of the case directories.  

## To run the simulation on BlueWaters:
Clone this repository on BlueWaters and run the job script: `qsub bw_fhr_p1b_c##_run`. 
The job script makes BlueWaters run `case##_deplete.py` which relies on its corresponding 
`phase1a/case##/case##_build_xml.py` for simulation parameters for each depletion step. 
To produce the results in this directory, `phase1a/case##/case##_build_xml.py` must be edited slightly for each case. 
- 100000 particles 
  - batches = 100
  - inactive = 10
  - particles = 100000
  - tallies_on = True 
- 10000 particles 
  - batches = 100
  - inactive = 10
  - particles = 10000
  - tallies_on = False 

The outputs of the job script for Case ## is in the results directory: 
- 100000 particles 
  - `results_fhr_p1b_c##_run_100000p`
  - `depletion_results_100000p.h5`
- 10000 particles 
  - `results_fhr_p1b_c##_run_10000p_nobug` 
  - `depletion_results_100000p.h5`
  
** There exists both a 100000 particle case and 10000_nobug particle case because when I ran the 100000 particle case on BlueWaters, the version of OpenMC I used had a minor bug that resulted in an error in the depleted isotopic amounts (fixed here: https://github.com/openmc-dev/openmc/pull/1581). More information on the OpenMC version used is described in the README.md in the root directory. 

## To analyze the output of the results:
On your local machine's version of the case directory, create the 
following directories: `h5files/100000p/` and `analysis_output/`. Download all the `openmc_simulation_n??.h5` output files from the 100000 particle run into the h5files/100000p/ directory. Run `python case##_depletion_analysis.py` and the depletion analysis required for the benchmark will be generated. Since there was a bug in the 100000 particle case for depleted isotopic amounts, the 10000_nobug particle results is used for this component of depletion analysis. Run `python case##_depletion_analysi_isotopics.py` and isotopic depletion analysis required for the benchmark will be generated. 
