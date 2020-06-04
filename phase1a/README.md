# FHR Benchmark Phase IA
This description in this README applies to each of the case directories. 

## To build the OpenMC XML files
Run `python case##_build_xml.py`. 

## To run the simulation on BlueWaters:
Clone this repository on BlueWaters after building the OpenMC XML files on your local machine, 
and run the job script: `qsub bw_fhr_p1a_c##_run`. (When tallies_on is toggled `True`, the 
tallies results will also be generated, and the simulation will take longer to run.)

The outputs of the job script for Case ## with 3pcm error is in the results directory: 
- `results_fhr_p1a_c##_3pcm` (tallies_on = True)
- `results_fhr_p1a_c##_3pcm_doppler`: + 50K to temperature of fuel material (tallies_on = False)
- `results_fhr_p1a_c##_3pcm_flibe`: + 50K to temperature of FliBe material (tallies_on = False)
- `results_fhr_p1a_c##_3pcm_graphite`: + 50K to temperature of graphite materials (tallies_on = False)

In this directory, `python case##_build_xml.py` builds the XML files required to create  `results_fhr_p1a_c##_3pcm`'s 
output. To generate the other results, `python case##_build_xml.py` must be edited slightly based on the 
descriptions above. 

## To analyze the output of the results:
On your local machine's version of the case directory, create the 
following directories: `h5files/3pcm/` and `analysis_output/`. Download the `statepoint.500.h5` and 
`summary.h5` output files into the directory. Run `python case##_analysis.py` and the analysis
required for the benchmark will be generated. 
