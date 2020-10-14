class Team:
    def __init__(self,name,skill_level):
        self.name = name
        self.skill_level = skill_level
        self.points = self.gf = self.ga = self.wins = self.draws = self.losses = self.gp = 0

    def add_goals(self, goals):
        self.gf += goals
