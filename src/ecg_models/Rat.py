from typing import TypedDict
import numpy as np
from .waves import *

class Waves(TypedDict):
    P: FunFeatures
    R: FunFeatures
    S: FunFeatures
    T: FunFeatures

def f(θ, fe: BeatFeatures):
    return  g(v(θ, fe['Waves']['P']), fe['Waves']['P']) + \
            g(v(θ, fe['Waves']['R']), fe['Waves']['R']) + \
            g(v(θ, fe['Waves']['S']), fe['Waves']['S']) + \
            h(v(θ, fe['Waves']['T']), fe['Waves']['T'])

def dfdt(p, ω, fe):
    return dgdt(p, ω, fe['Waves']['P']) + \
        dgdt(p, ω, fe['Waves']['R']) + \
        dgdt(p, ω, fe['Waves']['S']) + \
        dhdt(p, ω, fe['Waves']['T'])
    
example_beat = BeatFeatures(
        Waves=Waves(
            P=FunFeatures(a=.2, μ=np.pi*2/3., σ=.15),
            R=FunFeatures(a=1.2, μ=np.pi*1., σ=.1),
            S=FunFeatures(a=-1.2, μ=np.pi*13/12., σ=.1),
            T=FunFeatures(a=.4, μ=np.pi*16/12., σ=.4),
        ),
        RR=1.
)