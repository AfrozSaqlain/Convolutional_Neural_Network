# import warnings
# warnings.filterwarnings("ignore", category=UserWarning)

# from pyseobnr.generate_waveform import GenerateWaveform
# import matplotlib.pyplot as plt

# parameters = {
#     'mass1': 10,
#     'mass2': 10,
#     'spin1z': 0.1,
#     'spin2z': 0.1,
#     'distance': 400,
#     'deltaT': 1./4096,        # note: use 'deltaT' not 'delta_t'
#     'eccentricity': 0.6,
#     'phi_ref': 0,             # use 'phi_ref' instead of 'coa_phase'
#     'f22_start': 20,          # use 'f22_start' instead of 'f_lower'
#     'long_asc_nodes': 0,
#     'approximant': 'SEOBNRv5EHM'
# }

# generator = GenerateWaveform(parameters)
# hp, hc = generator.generate_td_polarizations()

# plt.plot(hp.data.data, label='hplus')
# plt.plot(hc.data.data, label='hcross')
# plt.legend()
# plt.show()


import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from pyseobnr.generate_waveform import GenerateWaveform
import pylab
import numpy as np

parameters = {
    'mass1': 10,
    'mass2': 10,
    'spin1z': 0.1,
    'spin2z': 0.1,
    'distance': 400,
    'deltaT': 1./4096,       
    'eccentricity': 0.6,
    'phi_ref': 0,            
    'f22_start': 20,        
    'long_asc_nodes': 0,
    'approximant': 'SEOBNRv5EHM'
}

generator = GenerateWaveform(parameters)
hp, hc = generator.generate_td_polarizations()

hp_data = hp.data.data
hc_data = hc.data.data

t_start = hp.epoch
dt = hp.deltaT
n_samples = len(hp_data)
time = np.arange(n_samples) * dt + float(t_start)

pylab.figure(figsize=(12, 6))
pylab.plot(time, hp_data, label='h_plus', linewidth=0.8)
pylab.plot(time, hc_data, label='h_cross', linewidth=0.8)
pylab.xlabel('Time (s)')
pylab.ylabel('Strain')
pylab.title('Gravitational Wave Polarizations')
pylab.legend()
pylab.grid(True, alpha=0.3)
pylab.show()
