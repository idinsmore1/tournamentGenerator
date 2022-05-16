def get_num_teams():
    num_teams = int(input("Enter the number of teams in the tournament: "))
    if num_teams < 2:
        print("The minimum number of teams is 2, try again.")
        get_num_teams()
    return num_teams

def get_team_names(num_teams):
    team_names = []
    for i in range(num_teams):
        while True:
            team_name = input(f"Enter the name of team #{i + 1}: ")
            if len(team_name.strip().split(' ')) > 2:
                print("Team names must be at most 2 words, try again.")
                continue
            elif len(team_name) < 2:
                print("Team names must be at least 2 characters long, try again.")
                continue
            else:
                team_name = team_name.strip().capitalize()
                team_names.append(team_name)
                break
    return team_names

def get_number_of_games(num_teams):
    n_games = int(input('Enter the number of games played by each team: '))
    while n_games < num_teams - 1:
        print('Invalid number of games. Each team plays each other at least once in the regular season, try again.')
        n_games = int(input('Enter the number of games played by each team: '))
    return n_games

def get_number_of_wins(team_names, n_games):
    wins = []
    for team in team_names:
        while True:
            num_wins = int(input(f'Enter the number of wins for Team {team} had: '))
            if num_wins < 0:
                print('The minimum number of wins is 0, try again.')
                continue
            elif num_wins > n_games:
                print(f'The maximum number of wins is {n_games}, try again.')
                continue
            else:
                wins.append(num_wins)
                break
    return wins

def generate_schedule(team_dict):
    sorted_teams = sorted(team_dict, key=team_dict.get)
    if len(sorted_teams) % 2 == 1:
        bye_team = sorted_teams[-1]
        print(f'Team {bye_team} gets a first round bye as it had the most wins.')
        sorted_teams = sorted_teams[:-1]
    for i in range(len(sorted_teams) // 2):
        print(f'Home: {sorted_teams[-(i + 1)]} VS Away: {sorted_teams[i]}')

if __name__ == '__main__':
    num_teams = get_num_teams()
    team_names = get_team_names(num_teams)
    num_games = get_number_of_games(num_teams)
    num_wins = get_number_of_wins(team_names, num_games)
    team_dict = {team_name: wins for team_name, wins in zip(team_names, num_wins)}
    print("Generating the games to be played in the first round of the tournament...")
    generate_schedule(team_dict)
    
