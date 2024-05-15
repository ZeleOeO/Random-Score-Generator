from randing import *

# random =


class Team:
    def __init__(self, name):
        self.score = 0
        self.name = name


class Game:
    def __init__(self):
        pass

    def generate_Teams(self, name1, name2):
        self.team1 = Team(name1)
        self.team2 = Team(name2)

    def __generate_scores(self):
        self.team1.score = 0
        self.team2.score = 0

    def __calculate_winner(self):
        return max(self.team1.score, self.team2.score)
