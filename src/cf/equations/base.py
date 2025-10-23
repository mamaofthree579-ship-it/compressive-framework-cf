class EquationModel:
    """Abstract base class for equation models used in CF.

    Subclasses should implement:
      - evaluate(self, **kwargs) -> numeric result (numpy arrays allowed)
    """
    def __init__(self, name):
        self.name = name

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement evaluate()")
