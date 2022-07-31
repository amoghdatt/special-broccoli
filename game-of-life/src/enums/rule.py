from enum import Enum
from src.rules.birth_rule import BirthRule
from src.rules.survival_rule import SurvivalRule

class LifeRules(Enum):

    SURVIVAL_RULE = SurvivalRule()
    BIRTH_RULE = BirthRule()