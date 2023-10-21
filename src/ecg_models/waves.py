import numpy as np
from typing import TypedDict 

class FunFeatures(TypedDict):
    a: float # V   
    μ: float # rad
    σ: float # rad

class BeatFeatures(TypedDict):
    Waves: TypedDict
    RR: float
    
def v(θ, fe: FunFeatures):
    return ( θ % (2*np.pi) - fe['μ'] ) / fe['σ']

def g(v, fe: FunFeatures):
    return fe['a'] * np.exp( -.5 * v**2 )

def h(v, fe: FunFeatures):
    # note: mu is the mode in gumbel (not mean)
    return fe['a'] * np.exp( 1. - v - np.exp( - v ) )

def dgdt(p, ω, fe: FunFeatures):
    θ, _, _ = p
    vi = v(θ, fe)
    return - g(vi, fe) * vi * ω / fe['σ']

def dhdt(p, ω, fe: FunFeatures):
    θ, _, _ = p
    vi = v(θ, fe)
    return h(vi, fe) * ( np.exp( -vi ) - 1. ) * ω / fe['σ']
