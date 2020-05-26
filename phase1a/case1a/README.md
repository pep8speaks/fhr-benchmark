# FHR Benchmark Phase IA Case 1A 

## To build the OpenMC XML files
Run `python case1a_build_xml.py`. 

## To run the simulation on BlueWaters:
Clone this repository on BlueWaters with the XML files, 
and run the job script: `qsub bw_fhr_p1a_c1a_run`. (When tallies_on is toggled `True`, the 
tallies results will also be generated, and the simulation will take longer to run.)

The outputs of the job script for Case 1A with 3pcm error is in the results directory: 
- `results_fhr_p1a_c1a_3pcm` (tallies yes)
- `results_fhr_p1a_c1a_3pcm_doppler`: + 50K to temperature of fuel (tallies no)
- `results_fhr_p1a_c1a_3pcm_flibe`: + 50K to temperature of FliBe (tallies no)
- `results_fhr_p1a_c1a_3pcm_graphite`: + 50K to temperature of graphite (tallies no) 

In this directory, `python case1a_build_xml.py` builds the XML files required to create  `results_fhr_p1a_c1a_3pcm`'s 
output. To generate the other results, `python case1a_build_xml.py` must be edited slightly based on the 
descriptions above. 

## To analyze the output of the results:
On your local machine's version of this directory, create the 
following directories: `h5files/3pcm/` and `analysis_output/`. Download the `statepoint.500.h5` and 
`summary.h5` output files into the directory. Run `python case1a_analysis.py` and the analysis
required for the benchmark will be generated. 
