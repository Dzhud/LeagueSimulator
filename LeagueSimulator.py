#Premier League Simulator with skill ratings algorithm
#Author - B Lippitt
#Sep 2020

#imports
import math, random
#from prettytable import PrettyTable
import team
import results_generator, fixture_generator

#create team object; skill rating based on 19/20 position
liverpool = team.Team('Liverpool',20)
city = team.Team('City',19)
united = team.Team('United',18)
chelsea = team.Team('Chelsea',17)
leicester = team.Team('Leicester',16)
spurs = team.Team('Spurs',15)
wolves = team.Team('Wolves',14)
arsenal = team.Team('Arsenal', 13)
sheff_utd = team.Team('Sheff Utd',12)
burnley = team.Team('Burnley',11)
southampton = team.Team('Southampton',10)
everton = team.Team('Everton',9)
newcastle = team.Team('Newcastle',8)
palace = team.Team('Crystal Palace',7)
brighton = team.Team('Brighton',6)
west_ham = team.Team('West Ham',5)
villa = team.Team('Aston Villa',4)
leeds = team.Team('Leeds',3)
albion = team.Team('WBA',2)
fulham= team.Team('Fulham',1)

#list of teams in order to generate fixtures
teams = [liverpool, city, united, chelsea, leicester, spurs, wolves, arsenal,
         sheff_utd, burnley, southampton, everton, newcastle, palace, brighton,
         west_ham, villa, leeds, albion, fulham]

random.shuffle(teams)

schedule = fixture_generator.generate_fixtures(teams)

for fixture_list in schedule:
    print('\nGAMEWEEK',str(schedule.index(fixture_list)+1),'\n')
    for team in fixture_list:
        results_generator.generate_result(team[0],team[1])
        

league_standings = sorted(teams, key=lambda x: x.points, reverse=True)

print(league_standings)



    
