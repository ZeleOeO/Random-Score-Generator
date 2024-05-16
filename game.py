from LinearCongruential import LinearCongruential

# random =


class Team:
    def __init__(self, name):
        self.score = 0
        self.name = name
        self.points = 0


class Game:
    def __init__(self):
        pass

    def generate_Teams(self, name1, name2, name3, name4, name5, name6, name7, name8):
        self.team1 = Team(name1)
        self.team2 = Team(name2)
        self.team3 = Team(name3)
        self.team4 = Team(name4)
        self.team5 = Team(name5)
        self.team6 = Team(name6)
        self.team7 = Team(name7)
        self.team8 = Team(name8)

    def __generate_scores(self):
        self.team1.score = 0
        self.team2.score = 0
        self.team3.score = 0
        self.team4.score = 0
        self.team5.score = 0
        self.team6.score = 0
        self.team7.score = 0
        self.team8.score = 0

    def calculate_winner(self, team1: Team, team2: Team):
        if team1.score > team2.score():
            team1.points += 3
        elif team2.score > team1.score:
            team2.points += 3
        else:
            team1.points += 1
            team2.points += 2
