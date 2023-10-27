import numpy as np 
from src.ecg_models import Rat 
from geometric_plotter import Plotter 

fs = 1024
RR = Rat.example_beat['RR']
θ = np.linspace(0, 2*np.pi, num=int(fs*RR))
ω = 2*np.pi/RR
t = θ / ω
beat = Rat.f(θ, Rat.example_beat)

p = Plotter(_2d=True, figsize=(8.,5))
p.axs.plot(t, beat, '-k')

d2s = lambda x: int( fs * x / ω )

# P wave
fe = Rat.example_beat['Waves']['P']
w = Rat.g(Rat.v(θ, fe), fe)
start, end = d2s((fe['μ'] - 3. * fe['σ'])), d2s(fe['μ'] + 3. * fe['σ'])
p.axs.plot(t[start:end], w[start:end] - .01, linestyle='--', color='gray')
p.axs.annotate('$P_{on}$',
               xy=(t[start],  - .01),
               xytext=(0, -4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)
p.axs.annotate('$P_{off}$',
               xy=(t[end], - .01),
               xytext=(0, -4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)
p.axs.annotate('$P_{peak}$',
               xy=(t[d2s((fe['μ']))], w[d2s((fe['μ']))] + .01),
               xytext=(0, 4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)

# R wave
fe = Rat.example_beat['Waves']['R']
w = Rat.g(Rat.v(θ, fe), fe)
start, end = d2s((fe['μ'] - 3. * fe['σ'])), d2s(fe['μ'] + 3. * fe['σ'])
p.axs.plot(t[start:end], w[start:end] - .01, linestyle='--', color='gray')
p.axs.annotate('$RS_{on}$',
               xy=(t[start], - .01),
               xytext=(0, -4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)
p.axs.annotate('$R_{peak}$',
               xy=(t[d2s((fe['μ']))], w[d2s((fe['μ']))] + .01),
               xytext=(0, 4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)

# S wave
fe = Rat.example_beat['Waves']['S']
w = Rat.g(Rat.v(θ, fe), fe)
start, end = d2s((fe['μ'] - 3. * fe['σ'])), d2s(fe['μ'] + 3. * fe['σ'])
p.axs.plot(t[start:end], w[start:end] - .01, linestyle='--', color='gray')
p.axs.annotate('$S_{peak}$',
               xy=(t[d2s((fe['μ']))], w[d2s((fe['μ']))] - 2*.01),
               xytext=(0, -4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)
p.axs.annotate('$J$',
               xy=(t[end], - .01),
               xytext=(0, -4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)

# T wave
fe = Rat.example_beat['Waves']['T']
w = Rat.h(Rat.v(θ, fe), fe)
start, end = d2s((fe['μ'] - 1.5 * fe['σ'])), d2s(fe['μ'] + 4. * fe['σ'])
p.axs.plot(t[start:end], w[start:end] - .01, linestyle='--', color='gray')
p.axs.annotate('$T_{off}$',
               xy=(t[end], - .01),
               xytext=(0, -4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)
p.axs.annotate('$T_{peak}$',
               xy=(t[d2s((fe['μ']))], w[d2s((fe['μ']))] + .01),
               xytext=(0, 4),
               textcoords='offset fontsize',
               ha='center',
               bbox=dict(edgecolor='w',facecolor='w', alpha=0.),
               arrowprops=dict(
                   width=.1,
                   headwidth =4,
                   facecolor='black',
                )
)
p.axs.axis('off')
p.show()