import os
from os import walk
from pathlib import Path
import json

class FileHelper():
    def __init__(self):
        self.saved_games_location_path = Path(os.path.dirname(os.path.realpath(__file__)) + '\\saved_games')
        self.saved_games_location_path.resolve()
        self.saved_games_location_path_string = self.saved_games_location_path._str

    def save_game(self, game_state):
        print ('Enter the name of your game to save:')
        game_name = input()
        try:
            saved_game_path = self.saved_games_location_path_string + '\\' + game_name
            if not os.path.exists(saved_game_path):
                saved_game_file = open(saved_game_path, 'w+')
                game_state.current_state['current_class'] = game_state.__class__.__name__
                saved_game_file.write(json.dumps(game_state.current_state))
                saved_game_file.close()
                print ('Your game was saved succesfully')
            else:
                print ('That name already exists - please choose another name')
        except Exception as err:
            print ('There was a problem saving your game, tell Paul about it! Error is: %s' % str(err))

    def load_game(self):
        print ('Saved games:')
        print ('------------')
        count = 1
        file_name_map = {}
        for (dirpath, dirnames, filenames) in walk(self.saved_games_location_path_string):
            for file_name in filenames:
                print ('%d: %s' % (count, file_name))
                count += 1
                file_name_map[count] = file_name
        print ('Which game do you want to load?')
        try:
            load_game_nr = int(input())
            load_file = open(self.saved_games_location_path_string + '\\' + file_name_map[load_game_nr], 'r')
            game_data = json.loads(load_file.read())

            # TODO: pull the class name out of the game status and map it to an import path
            # prevent saving more than X nr games
            # allow deleting of games
            load_file.close()
        except Exception as err:
            print ('Error trying to save your game, sorry! Error is: %s' % str(err))
            print ('Did you enter a valid number?')