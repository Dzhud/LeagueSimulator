import math, random
import team

#constants used in result generation algorithm for better/worse team in fixture
higher = 1.148698355
lower = 0.8705505633

#function to generate result between 2 teams
def generate_result(home_team, away_team):
    home_score = generate_home_score(home_team,away_team)
    away_score = generate_away_score(home_team, away_team)

    update_teams(home_team, away_team, home_score, away_score)

    print(home_team.name,home_score,'-',away_score,away_team.name)

    return home_team.name, home_score, away_score, away_team.name
#function to calculate the home team score - uses an equation which takes into consideration team and opponent's skill level
#and whether they are playing home or away
def generate_home_score(home,away):
    home_skill = home.skill_level / 3
    away_skill = away.skill_level / 3

    home_goals = 0
    lambHome = higher ** (home_skill - away_skill)
    x = random.random()
    while x>0:
        x = x - (((lambHome ** home_goals) * math.exp(-1 * lambHome)) /
                 math.factorial(home_goals))
        home_goals += 1
        
    return (home_goals - 1)
#function to calculate the away team score - uses an equation which takes into consideration team and opponent's skill level
#and whether they are playing home or away
def generate_away_score(home,away):
    home_skill = home.skill_level/3
    away_skill = away.skill_level/3

    away_goals = 0
    lambAway = lower ** (home_skill - away_skill)
    x = random.random()
    while x > 0:
        x = x - (((lambAway ** away_goals) * math.exp(-1 * lambAway)) /
                 math.factorial(away_goals))
        away_goals += 1

    return (away_goals - 1)


#update team stats for league table
def update_teams(home_team, away_team, home_score, away_score):
    #home team win
    if home_score > away_score:
        home_team.points += 3
        home_team.wins += 1
        home_team.gf += home_score
        home_team.ga += away_score
        home_team.gp += 1

        away_team.losses += 1
        away_team.gf += away_score
        away_team.ga += home_score
        away_team.gp += 1
    #away win
    elif away_score > home_score:
        away_team.points += 3
        away_team.wins += 1
        away_team.gf += away_score
        away_team.ga += home_score
        away_team.gp += 1

        home_team.losses += 1
        home_team.gf += home_score
        home_team.ga += away_score
        home_team.gp += 1
    #draw
    else:
        home_team.points += 1
        home_team.draws += 1
        home_team.gf += home_score
        home_team.ga += away_score
        home_team.gp += 1

        away_team.points+= 1
        away_team.draws += 1
        away_team.gf += away_score
        away_team.ga += home_score
        away_team.gp += 1
        




        
