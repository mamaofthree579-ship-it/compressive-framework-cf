# Registry of available equation models for CF
from .resonance import ResonanceEquation
from .compression import CompressionEquation
from .feedback import FeedbackEquation

EQUATION_REGISTRY = {
    'resonance': ResonanceEquation(),
    'compression': CompressionEquation(),
    'feedback': FeedbackEquation(),
}

def list_equations():
    return sorted(EQUATION_REGISTRY.keys())
