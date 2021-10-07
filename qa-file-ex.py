
#file = open('teams.txt', 'w')

#teamnames = ['Road Runners','Green Stripes','Black Bears','The Hooligans','Nice Guys n Gals']
#for n in teamnames:
#    newteams =  f'Team name: {n}' + '\n'
#    file.write(newteams)
#file.close()

with open('teams.txt', 'w') as file:
    teamnames = ['Team 1: Road Runners','\nTeam 2: Green Stripes','\nTeam 3: Black Bears','\nTeam 4: The Hooligans','\nTeam 5: Nice Guys n Gals']
    file.writelines(teamnames)
file.close()

file = open('teams.txt', 'r')
lines = file.readlines()
print(lines[0],lines[3])
file.close()

file = open('teams.txt', 'w')
newline = 'This is a new line!\n'
file.writelines(newline)
file.writelines(teamnames)
file.close()
