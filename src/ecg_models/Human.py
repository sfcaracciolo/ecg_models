# type: ignore
from typing import TypedDict
import numpy as np
from .waves import *

class Waves(TypedDict):
    P: FunFeatures
    Q: FunFeatures
    R: FunFeatures
    S: FunFeatures
    T: FunFeatures

    @classmethod
    def template(cls):
        return cls(
            P=FunFeatures(a=0, μ=0, σ=0),
            Q=FunFeatures(a=0, μ=0, σ=0),
            R=FunFeatures(a=0, μ=0, σ=0),
            S=FunFeatures(a=0, μ=0, σ=0),
            T=FunFeatures(a=0, μ=0, σ=0)
        )
    
def f(θ, fe: BeatFeatures):
    return  g(v(θ, fe['Waves']['P']), fe['Waves']['P']) + \
            g(v(θ, fe['Waves']['Q']), fe['Waves']['Q']) + \
            g(v(θ, fe['Waves']['R']), fe['Waves']['R']) + \
            g(v(θ, fe['Waves']['S']), fe['Waves']['S']) + \
            g(v(θ, fe['Waves']['T']), fe['Waves']['T'])

def dfdt(p, ω, fe):
    return dgdt(p, ω, fe['Waves']['P']) + \
        dgdt(p, ω, fe['Waves']['Q']) + \
        dgdt(p, ω, fe['Waves']['R']) + \
        dgdt(p, ω, fe['Waves']['S']) + \
        dgdt(p, ω, fe['Waves']['T'])
    
example_beat = BeatFeatures(
        Waves=Waves(
            P=FunFeatures(a=.2, μ=np.pi*2/3., σ=.25),
            Q=FunFeatures(a=-.2, μ=np.pi*11/12., σ=.1),
            R=FunFeatures(a=1.2, μ=np.pi*1., σ=.1),
            S=FunFeatures(a=-.3, μ=np.pi*13/12., σ=.1),
            T=FunFeatures(a=.4, μ=np.pi*3/2., σ=.4),
        ),
        RR=1.
)