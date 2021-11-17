class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return f"{self.name:20}" + self.team + " " + f"{str(self.goals):2}" + " + " + f"{str(self.assists):2}" + " = " + f"{self.assists+self.goals:2}"
