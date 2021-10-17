from abc import ABC, abstractmethod


class AdditionalParameter(ABC):
    """
    Represents important indicators 
    that point to specific characteristics of person 
    being tested.
    """
    @abstractmethod
    def __init__(self):
        self._mark: int = 0
    
    def increase(self, value: int) -> None:
        "Adds balls to the parameter mark."
        if isinstance(value, int):
            self._mark += value

class NegativeAttitude(AdditionalParameter):
    """
    Measures how negative tested person relates to the test.
    """
    def __init__(self):
        super().__init__()

class Dissimulation(AdditionalParameter):
    """
    Estimates intention to hode the result.
    """
    def __init__(self):
        super().__init__()

class Francness(AdditionalParameter):
    """
    Points at high francness of person.
    """
    def __init__(self):
        super().__init__()

class OrganicPsychopaphy(AdditionalParameter):
    """
    Lets know how likely the organic origin 
    of the accentuation is.
    """
    def __init__(self):
        super().__init__()

class Emansipation(AdditionalParameter):
    """
    Reflects how expressed independence, emansipation is.
    """
    def __init__(self):
        super().__init__()

class Delinquent(AdditionalParameter):
    """
    
    """
    def __init__(self):
        super().__init__()