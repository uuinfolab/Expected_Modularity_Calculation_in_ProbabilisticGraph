# Expected_Modularity_Calculation_in_ProbabilisticGraph

This is the official implementation for 'Fast and accurate algorithms to calculate expected modularity in probabilistic networks'.

## Main idea

We created two methods for expected modularity calculation in probabilistic networks, the first one is non-approximation method called PWP^EMOD, the second one is approximation method called APWP^EMOD.

There are three genral steps to implement:

(1) partition all possible worlds based on their modularity 

(2) calculate all partitions' probabilities, PWP^EMOD uses the definition of Poisson-Binomial distribution and APWP^EMOD uses Discrete Fourier Transform (DFT).

(3) calculate expected modularity of all partitions

## Installation

To prepare the Python environment for the code in this rpo, the users can create the any of enviroment below

```
Python 3.9.13
Python 3.8.10
```
## Run Code
```
cd /.../.../Expected_Modularity_Calculation_in_ProbabilisticGraph-main

python3 Accuracy_and_execution_time_4.1.py

python3 Comparison_with_weighting_4.2.1.py
python3 Comparison_with_thresholding_4.2.2.py
python3 Comparison_with_sampling_CCS_4.2.3.py
python3 Comparison_with_sampling_LCCS_4.2.3.py
python3 Factors_influencing_execution_time_ex1_4.3.py
python3 Factors_influencing_execution_time_ex2_4.3.py
```
## Citation

If you find the repository helpful, please consider citing our papers:
```
Fast and accurate algorithms to calculate expected modularity in probabilistic networks
Xin Shen, Matteo Magnani, Christian Rohner, Fiona Skerman
```

