# FHR Benchmark Phase IB
This description in this README applies to each of the case directories.  

## To run the simulation on BlueWaters:
Clone this repository on BlueWaters and run the job script: `qsub bw_fhr_p1b_c##_run`. 
The job script makes BlueWaters run `case##_deplete.py` which relies on its corresponding 
`phase1a/case##/case##_build_xml.py` for simulation parameters for each depletion step. 
(When tallies_on is toggled `True`, the tallies results will also be generated, 
and the simulation will take longer to run.)

The outputs of the job script for Case ## is in the results directory: 
- `results_fhr_p1b_c##_run_100000p` (tallies_on = True)
- `depletion_results_100000p.h5`
- `results_fhr_p1b_c##_run_10000p_nobug` (tallies_on = False)
- `depletion_results_100000p.h5`

In this directory, `python case##_build_xml.py` builds the XML files required to create  `results_fhr_p1a_c##_3pcm`'s 
output. To generate the other results, `python case##_build_xml.py` must be edited slightly based on the 
descriptions above. 

## To analyze the output of the results:
On your local machine's version of the case directory, create the 
following directories: `h5files/3pcm/` and `analysis_output/`. Download the `statepoint.500.h5` and 
`summary.h5` output files into the directory. Run `python case##_analysis.py` and the analysis
required for the benchmark will be generated. 
