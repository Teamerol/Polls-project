from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


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
        "Adds points to the parameter mark."
        if isinstance(value, int):
            self._mark += value
    
    def get(self):
        return self._mark

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
    Only for mans. Represents propensity, tendency to make antosocial, dangerous decisions.
    """
    def __init__(self):
        super().__init__()

class MasculinityOrFeminity(AdditionalParameter):
    """
    Shows the predominance of having masculine or femine character traits.
    """
    is_masculine: bool = False
    is_femine: bool = False

    def __init__(self):
        super().__init__()
    
    def compute(self, masculinity: Masculinity, feminity: Feminity):
        """Count score for masculinity and feminity marks."""
        self._mark = masculinity.get() - feminity.get()
    
    def result(self) -> NotImplemented:
        """Returns result about predominance of masculine of femine traits."""
        if self._mark > 0:
            self.is_masculine = True
        if self._mark < 0:
            self.is_femine = True
    
class Masculinity(MasculinityOrFeminity):
    """
    Shows the predominance of having masculine character traits.
    """
    def __init__(self):
        super().__init__()

class Feminity(MasculinityOrFeminity):
    """
    Shows the predominance of having femine character traits.
    """
    def __init__(self):
        super().__init__()

class Alcoholization():
    """
    Isn't inherited from class AdditionalParameter, 
    because instance of Alcoholization wouldn't be shown on result graph.

    Determines inclination to drinking alcohol.
    """

    def __init__(self) -> None:
        self._score: int = 0

    def increase(self, value: int) -> None:
        "Enchance score of alcoholization."
        if isinstance(value, int):
            self._score += value
        else:
            raise TypeError(f"Score estimate {value} is not integer.")

    def decrease(self, value: int) -> None:
        """Reduce score of alcoholization"""
        if isinstance(value, int):
            self._score -= value
        else:
            raise TypeError(f"Score estimate {value} is not integer.")