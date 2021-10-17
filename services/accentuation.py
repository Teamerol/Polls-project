from abc import ABC, abstractmethod


class Accentuation(ABC):
    """
    Basic class for accentuation concept. It doesn't implements directly, instead is used as a parent.


    Accentuation, following the defition in Pathoharacterological diagnostic questionnaire
    (rus. Патохарактерологический_диагностический_опросник),
    means inclination, tendency in person's character.
    
    For example, proactive and resilient individual has a hypertemic accentuation,
    and humans, prone to self-examonation, having excessive suspiciousness, 
    rich imagination are psychasthenics.
    
    There are 11 types of accentuations, and they are explained in psychological works of Andrey Yevgenyevich Lichko
    (https://en.wikipedia.org/wiki/Andrey_Yevgenyevich_Lichko)."""

    @abstractmethod
    def __init__(self):
        self._score: int = 0

    def __str__(self) -> str:
        return f"{self.__class__.__name__} score = {self._score}"
    
    def increase_score(self, value: int) -> None:
        "Enchance score of accentuation."
        if isinstance(value, int):
            self._score += value
    
    def decrease_score(self, value: int) -> None:
        "Reduce score of accentuation"
        if isinstance(value, int):
            self._score -= value
