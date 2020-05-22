import os
from os import walk
from pathlib import Path
import json

class FileHelper():
    def __init__(self):
        self.saved_games_location_path_string = 'lib\\saved_games\\'

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

    def delete_game(self):
        file_name_map = self.list_files()
        print('Which game do you want to delete?')
        try:
            delete_game_nr = int(input())
            if delete_game_nr != 99:
                print ('Are you sure you want to delete: "%s"? (y / n))' % file_name_map[delete_game_nr])
                sure = input()
                if sure.lower() == 'y':
                    os.remove(self.saved_games_location_path_string + '\\' + file_name_map[delete_game_nr])
                    print('Your game was deleted succesfully')
        except Exception as err:
            print('Error trying to delete your game, sorry! Error is: %s' % str(err))
            print ('Did you type a valid number?')

    def save_game(self, game_state):
        print ('Enter the name of your game to save:')
        game_name = input()
        try:
            saved_game_path = self.saved_games_location_path_string
            if not os.path.exists(saved_game_path):
                os.mkdir(saved_game_path)
            if len([name for name in os.listdir(saved_game_path)]) > 9:
                print ("There are already 10 saved games, please delete one first'")
                self.delete_game()
            else:
                if not os.path.exists(saved_game_path + '\\' + game_name):
                    saved_game_file = open('lib\\saved_games\\' + game_name, 'w')
                    game_state.current_state['current_class'] = game_state.__class__.__name__
                    saved_game_file.write(json.dumps(game_state.current_state))
                    saved_game_file.close()
                    print ('Your game was saved succesfully')
                else:
                    print ('That name already exists - please choose another name')
                    self.save_game(game_state)
        except Exception as err:
            print ('There was a problem saving your game, tell Paul about it! Error is: %s' % str(err))

    def list_files(self):
        count = 1
        file_name_map = {}
        for (dirpath, dirnames, filenames) in walk(self.saved_games_location_path_string):
            for file_name in filenames:
                print('%d: %s' % (count, file_name))
                file_name_map[count] = file_name
                count += 1
        print ('99: Never mind')
        return file_name_map

    def load_game(self, scene):
        print ('Saved games:')
        print ('------------')
        file_name_map = self.list_files()
        print ('Which game do you want to load?')
        try:
            load_game_nr = int(input())
            if load_game_nr != 99:
                load_file = open(self.saved_games_location_path_string + '\\' + file_name_map[load_game_nr], 'r')
                game_data = json.loads(load_file.read())
                game_class = game_data.get('current_class')
                load_file.close()
                imported_class = self.get_class_from_class_name(game_class)
                return imported_class(game_data)
            else:
                return scene
        except Exception as err:
            print ('Error trying to save your game, sorry! Error is: %s' % str(err))
            print ('Did you enter a valid number?')
            return scene

# Testing
# file_helper = FileHelper()
# the_class = file_helper.get_class_from_class_name('BaseScene')
# sda = 2