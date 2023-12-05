#Count of Matches in Tournament
n = 14
Match=0
team_adv=0
while team_adv != 1:
    if n % 2 == 0:
        Match += n // 2 
        team_adv = n // 2

    else:
        Match += n // 2
        team_adv = n // 2+1 
    n = team_adv
print(Match)

#Recursive method
def count(n,Match=0,team_adv=0):
    if team_adv == 1:
        return 0
    if n % 2 == 0:
        Match = team_adv = n // 2

    else:
        Match = n // 2
        team_adv = n // 2+1 
    return Match+count(team_adv,Match,team_adv)
print(count(14))