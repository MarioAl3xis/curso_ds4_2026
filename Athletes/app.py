
from Game import Game
from Team import Team
from Sport import Sport
from Athlete import Athlete
import json

def load_json(file_path):
    """Loads JSON data from a file and returns the data as a Python object."""
    data = None 
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def convert_json_to_teams (json_data):
    """ Converts JSON data into a list of Team objects."""
    teams = []
    for team_data in json_data:
        team_name = team_data['name']
        team_name = team_data['name']
        sport_name = team_data['sport']
        sport_league = team_data ['sport']
        ['league']
        sport_num_players = team_data
        ['sport']['num_players']

        print(team_name)


def main():
    """ Main function to create teams, athletes, and simulate a game""" 
    # Load data from JSON files
    tournament_data = load_json(r"C:\\Users\\mario\\Documentos\\desarrollo4\\curso_ds4_2026\Athletes\\tournament.json")
    print ("tournament:", tournament_data)
    convert_json_to_teams(tournament_data)

if __name__ == "__main__":
    main()