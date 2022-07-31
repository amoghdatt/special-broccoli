from enum import Enum

class LifeRuleDefinitions(Enum):

    SURVIVAL_RULE_DEFINITION = lambda _ , neighbors_count: neighbors_count < 2 or neighbors_count > 3
    BIRTH_RULE_DEFINITION = lambda _ , neighbors_count: neighbors_count == 3