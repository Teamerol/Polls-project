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
        self.threshold_score: int = 5

    def __str__(self) -> str:
        return f"{self.__class__.__name__} score = {self._score}"
    
    def increase(self, value: int) -> None:
        "Enchance score of accentuation."
        if isinstance(value, int):
            self._score += value
        else:
            raise TypeError(f"Score estimate {value} is not integer.")
    
    def decrease(self, value: int) -> None:
        "Reduce score of accentuation"
        if isinstance(value, int):
            self._score -= value
        else:
            raise TypeError(f"Score estimate {value} is not integer.")

class Hyperthymic(Accentuation):
    """
    Active, energetic, extraversive people have this type of accentuation.
    """
    def __init__(self):
        super().__init__()

class Cycloid(Accentuation):
    """
    Mood volatile, fickle people.
    """
    def __init__(self):
        super().__init__()

class Labile(Accentuation):
    """
    Prone to mood swings, not stable emotionally people.
    """
    def __init__(self):
        super().__init__()

class AsthenoNeuroticity(Accentuation):
    """
    Hypochondriacs, extremely concerned about health people.
    """
    def __init__(self):
        super().__init__()

class Sensitive(Accentuation):
    """
    Very sensitive, subtle, but not souciable people.
    """
    def __init__(self):
        super().__init__()

class Psychasthenic(Accentuation):
    """
    Indecisive, pensive, suspicious people.
    """
    def __init__(self):
        super().__init__()

class Schizoid(Accentuation):
    """
    Not prone to empaphy, eccentric, rather clever and inventive people.
    """
    def __init__(self):
        super().__init__()

class Epileptoid(Accentuation):
    """
    Usually affective, pedantic and adaptive people.
    """
    def __init__(self):
        super().__init__()

class Hysteroid(Accentuation):
    """
    Dramatic, creative, willing to be in spotlight people.
    """
    def __init__(self):
        super().__init__()

class Unstable(Accentuation):
    """
    People in this category don't have stable intersts, 
    they can't concentrate on hard work, preferring entartainments.
    """
    def __init__(self):
        super().__init__()

class Conformal(Accentuation):
    """
    These people try to be  indistinguishable from the environment.
    They are 'products' of their surroundings.
    """
    def __init__(self):
        super().__init__()