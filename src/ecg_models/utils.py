from .waves import BeatFeatures, FunFeatures
from typing import Callable, Literal, Tuple
import json
import copy

class FeatureEditor:
    def __init__(self, f: BeatFeatures) -> None:
        self.model = copy.deepcopy(f)

    def __str__(self) -> str:
        return json.dumps(self.model, indent=4, ensure_ascii=False)
    
    def scale(self, value: float, feature: Literal['a', 'μ', 'σ'] = None):
        self.set(lambda x: x*value, feature=feature)

    def expand(self, value: float, feature: Literal['a', 'μ', 'σ'] = None):
        self.set(lambda x: x*(1+value) if x > 0 else x*(1-value), feature=feature)

    def collapse(self, value: float, feature: Literal['a', 'μ', 'σ'] = None):
        self.set(lambda x: x*(1-value) if x > 0 else x*(1+value), feature=feature)

    def abs(self, feature: Literal['a', 'μ', 'σ'] = None):
        self.set(abs, feature=feature)

    def constant(self, value: float, feature: Literal['a', 'μ', 'σ'] = None):
        self.set(lambda x: value, feature=feature)

    def set(self, fun: Callable, feature: Literal['a', 'μ', 'σ'] = None):
        for k, v in self.model['Waves'].items():
            if feature is None:
                v['a'] = fun(v['a'])
                v['μ'] = fun(v['μ'])
                v['σ'] = fun(v['σ'])
            else:
                v[feature] = fun(v[feature])

    def get_feature(self):
        return copy.deepcopy(self.model)

def vectorize(fes: BeatFeatures) -> Tuple:
    vec = [ fes['RR'] ]
    for v in fes['Waves'].values():
        vec += v.values()
    return vec

def modelize(l: Tuple, WavesClass) -> BeatFeatures:
    WavesTemplate = WavesClass.template()
    i = 0
    for k in WavesTemplate.keys():
        WavesTemplate[k] = FunFeatures(a=l[i+1], μ=l[i+2], σ=l[i+3])
        i += 3

    return BeatFeatures(
        Waves=WavesTemplate,
        RR=l[0],
    )

def fvec(f, WavesClass, θ, *args):
    fe = modelize(args, WavesClass)
    return f(θ, fe)