# type: ignore
from typing import TypedDict
import numpy as np
from .waves import *

class Waves(TypedDict):
    P: FunFeatures
    R: FunFeatures
    S: FunFeatures
    T: FunFeatures

    @classmethod
    def template(cls):
        return cls(
            P=FunFeatures(a=0, μ=0, σ=0),
            R=FunFeatures(a=0, μ=0, σ=0),
            S=FunFeatures(a=0, μ=0, σ=0),
            T=FunFeatures(a=0, μ=0, σ=0)
        )

def f(θ, fe: BeatFeatures) -> np.ndarray:
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
            P=FunFeatures(a=.05, μ=np.pi*2/3., σ=.1),
            R=FunFeatures(a=.6, μ=np.pi*1., σ=.08),
            S=FunFeatures(a=-.3, μ=np.pi*13/12., σ=.06),
            T=FunFeatures(a=.25, μ=np.pi*15/12., σ=.3),
        ),
        RR=.22
)