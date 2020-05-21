import os
from os import walk
from pathlib import Path
import json

class FileHelper():
    def __init__(self):
        self.saved_games_location_path = Path(os.path.dirname(os.path.realpath(__file__)) + '\\saved_games')
        self.saved_games_location_path.resolve()
        self.saved_games_location_path_string = self.saved_games_location_path._str

    def get_class_from_full_path(self, full_path_name):
        components = full_path_name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    def get_class_from_class_name(self, class_name):
        if class_name in ['InitialScene', 'BaseScene', 'InTree']:
            return self.get_class_from_full_path('scenes.BaseScene.' + class_name)
        elif class_name in ['Thirty', 'TwentyNine', 'TwentyEightTreasure', 'TwentyEightTreasureGone', 'TwentySeven', 'TwentySix', 'TwentyFive', 'TwentyFour', 'TwentyThree', 'TwentyTwo', 'TwentyOne', 'Twenty',
                            'Nineteen', 'Eighteen', 'Seventeen', 'Sixteen', 'Fifteen', 'Fourteen', 'Thirteen', 'Twelve', 'Eleven', 'Ten', 'Nine', 'Eight', 'Seven', 'Six'
                            , 'Five', 'Four', 'Three', 'Two', 'One', 'Exit', 'EnterMaze', 'StartMaze']:
            return self.get_class_from_full_path('scenes.Maze.' + class_name)
        elif class_name in ['Ogre', 'HappyOgre']:
            return self.get_class_from_full_path('scenes.OgreInCabin.' + class_name)
        elif class_name in ['Plane', 'LeavePlane', 'Mountains', 'Cave', 'Forest', 'Goat', 'Cabin', 'Cliff']:
            return self.get_class_from_full_path('scenes.Stage1Scenes.' + class_name)

    def save_game(self, game_state):
        print ('Enter the name of your game to save:')
        game_name = input()
        try:
            saved_game_path = self.saved_games_location_path_string
            if not os.path.exists(saved_game_path):
                os.mkdir(saved_game_path)
            if not os.path.exists(saved_game_path + '\\' + game_name):
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
                file_name_map[count] = file_name
                count += 1
        print ('Which game do you want to load?')
        try:
            load_game_nr = int(input())
            load_file = open(self.saved_games_location_path_string + '\\' + file_name_map[load_game_nr], 'r')
            game_data = json.loads(load_file.read())
            game_class = game_data.get('current_class')
            # prevent saving more than X nr games
            # allow deleting of games
            load_file.close()
            imported_class = self.get_class_from_class_name(game_class)
            return imported_class(game_data)
        except Exception as err:
            print ('Error trying to save your game, sorry! Error is: %s' % str(err))
            print ('Did you enter a valid number?')

# Testing
# file_helper = FileHelper()
# the_class = file_helper.get_class_from_class_name('BaseScene')
# sda = 2