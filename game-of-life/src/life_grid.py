from src.enums.rule import LifeRules

class LifeGrid:

    def __init__(self, seed_data):
        self.survivors = seed_data
        self.generation = 0


    def tick(self):
        
        survivors_for_next_generation = dict()

        for rule in LifeRules:
            rule.value.apply(survivors_for_next_generation, current_survivors = self.survivors)
        
        self.survivors = survivors_for_next_generation
        self.generation += 1


    def get_survivors(self):
        return self.survivors.keys()


    def print_survivors(self):
        print(*self.survivors.keys(), sep="\n")

