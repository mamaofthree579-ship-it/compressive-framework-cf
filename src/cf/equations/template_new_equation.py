# Template for adding new equation models.
# Copy this file and modify the class name and evaluate() body.

import numpy as np
from .base import EquationModel

class TemplateEquation(EquationModel):
    def __init__(self, name='template'):
        super().__init__(name)

    def evaluate(self, *args, **kwargs):
        """Implement the numerical evaluation here.

        Example signature:
            evaluate(x, param=1.0)
        Return either a scalar or numpy array.
        """
        # Example placeholder behavior:
        x = kwargs.get('x', 0.0)
        return np.asarray(x) * kwargs.get('param', 1.0)
