from src.rules.rule import Rule
from src.enums import LifeRuleDefinitions

class BirthRule(Rule):

    birth_rule_definition = LifeRuleDefinitions.BIRTH_RULE_DEFINITION

    def apply(self, potential_survivors, current_survivors):
        
        current_survivors_values = current_survivors.values()

        for survivor in current_survivors_values:

            for neighbor in survivor.get_neighbors():
                row = neighbor.row
                column = neighbor.column

                neighbors_count = 0

                if not f'{row}, {column}' in current_survivors:
                    
                    for dead_cell_neighbor in neighbor.get_neighbors():
                        dead_cell_row = dead_cell_neighbor.row
                        dead_cell_column = dead_cell_neighbor.column

                        if f'{dead_cell_row}, {dead_cell_column}' in current_survivors:
                            neighbors_count += 1

                    if self.birth_rule_definition(neighbors_count):
                        if not f'{row}, {column}' in potential_survivors:
                            potential_survivors[f'{row}, {column}'] = neighbor