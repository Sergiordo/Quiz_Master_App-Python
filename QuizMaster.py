class Team():
    Team_list = []

    def __init__(self, name):
        self.name = name
        self.score = 0

    @classmethod
    def add_team(cls, new_team):
        cls.Team_list.append(new_team)

    @classmethod
    def get_winning_team(cls):
        return max(cls.Team_list, key=lambda team: team.score)

class Score():
    
    def __init__(self, current_score):
        self.current_score = current_score
    
    @classmethod
    def add_score(cls, current_score, new_score):
        return current_score + new_score
    
    def __str__(self):
        return str(self.current_score)

class Rounds():
    Round = 1
    
    def __init__(self, total_r):
        self.total_r = total_r

    @classmethod
    def new_round(cls):
        cls.Round += 1
        
    @classmethod
    def current_round(cls):
        print(cls.Round)

# Collect teams
while True:
    new_team_name = input("Add a team (type 'stop' to stop): ")

    if new_team_name.lower() == 'stop':
        break

    Team.add_team(Team(new_team_name))

print("Team List:", [team.name for team in Team.Team_list])

# Round 1
Rounds.total_r = int(input("Enter the number of rounds: "))

while Rounds.Round <= Rounds.total_r:
    print(f"Round {Rounds.Round}:")
    for team in Team.Team_list:
        try:
            round_score = int(input(f"Enter the score for {team.name}: "))
            team.score = Score.add_score(team.score, round_score)
            break 
        except:
            print("Please enter a valid integer")

    print("Scores after Round", Rounds.Round)
    for team in Team.Team_list:
        print(f"{team.name}: {team.score}")

    Rounds.new_round()
    
    if Rounds.Round > Rounds.total_r:
        winning_teams = Team.get_winning_team()
        if len(winning_teams) == 1:
            print(f"The winning Team is {winning_teams[0].name} with a score of {winning_teams[0].score}")
        else:
            print("It's a tie! The winning teams are:")
            for team in winning_teams:
                print(f"{team.name} with a score of {team.score}")

print("Game Over!")
