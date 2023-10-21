## ECG Models

ECG models based on wave functions to use in [ECG Simulator](https://github.com/sfcaracciolo/ecg_simulator/).

For instance, a human model published on [link](https://ieeexplore.ieee.org/document/1186732): based on a sum of Gaussian functions:

$$f_H = \sum_{i=0}^{M-1} g_i $$
where $g_i = a_i  \exp (-{v_i}^2/2)$ , $v_i = (\bullet -\mu_i)/\sigma_i$ and $M=5$ (P, Q, R, S and T).

or Wistar rat model published on [link](https://dx.doi.org/10.1142/S0218339023500407) based on Gaussian and Gumbel functions:

$$f_R = \sum_{i=0}^{M-1} g_i + h_i $$
where $h_i = a_i  \exp (1 - v_i - \exp(-v_i))$ and $M=3$ (P, R, S and T).
