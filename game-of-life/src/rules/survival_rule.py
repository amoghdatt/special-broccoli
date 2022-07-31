from src.rules.rule import Rule
from src.enums import LifeRuleDefinitions

class SurvivalRule(Rule):

    survival_rule_definition = LifeRuleDefinitions.SURVIVAL_RULE_DEFINITION

    def apply(self, potential_survivors, current_survivors):

        current_survivors_values = current_survivors.values()


        for survivor in current_survivors_values:
            neighbors_count = 0

            for neighbor in survivor.get_neighbors():
                row = neighbor.row
                column = neighbor.column

                if f'{row}, {column}' in current_survivors:
                    neighbors_count+=1

            if not self.survival_rule_definition(neighbors_count-1):
                potential_survivors[f'{survivor.row}, {survivor.column}'] = survivor



        