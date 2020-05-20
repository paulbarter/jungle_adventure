# from scenes.BaseScene import BaseScene, InTree, InitialScene
from scenes.BaseScene import InitialScene
from scenes.BaseScene import print_plane

print ()
print ('----------------------------------------------------------------')
print ('**************** Welcome to Jungle adventure!!! ****************') 
print ('Useful Commands:')
print ('Type "hint" if you are stuck')
print ('"exit" if you want to quit')
print ('"inv" to see what you are carrying')
print ('"load game" to load a saved game')
print ('"save game" to save your game')
print ('----------------------------------------------------------------')
print ()
print ('Your plane crashed in a dense jungle, you are thrown from your plane in the crash...')
print_plane()
print ('Press Enter...')
input()
from os import system
system('cls')
from lib.FileFunctions import FileHelper
file_helper = FileHelper()

def print_dead():
	print("								")
	print("		     -|-				")
	print("		      |					")
	print("	   	  .-'~~~`-.				")
	print("	 	.'         `.			")
	print("	 	|  R  I  P  |			")
	print("	 	|           |			")
	print("	 	|           |			")
	print("		|           |			")
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^	")

GLOBAL_COMMANDS = ['load game', 'save game', 'take batteries out', 'take batteries out of torch', 'take batteries out of radio', 'take out batteries', 'put batteries in torch', 'put batteries in radio', 'put batteries into torch', 'put batteries into radio']

def apply_global_action(command, scene):
	if command == 'take batteries out' or command == 'take out batteries' or command == 'take batteries out of torch' or command == 'take batteries out of radio':
		if (scene.have('radio') or scene.have('torch')):
			if scene.have('batteries'):
				print ("You already took the batteries out!")
			else:
				print ('You take out the batteries')
				scene.set_game_status('radio_has_batteries', False)
				scene.set_game_status('torch_has_batteries', False)
				scene.take('batteries')
				scene.inc_score(2, 'take batteries out')
		else:
			print ("You dont have anything that has batteries!")
	elif command == 'put batteries in torch' or command == 'put batteries into torch':
		if scene.have('batteries'):
			if not scene.game_status('torch_has_batteries'):
				print ("You put the batteries in the torch.")
				scene.set_game_status('torch_has_batteries', True)
				scene.inc_score(5, 'torch_batteries')
				scene.drop('batteries')
			else:
				print ("The torch already has batteries!")
		else:
			print ("You dont have any batteries!")
	elif command == 'put batteries in radio' or command == 'put batteries into radio':
		if scene.have('batteries'):
			if not scene.game_status('radio_has_batteries'):
				print ("You put the batteries in the radio.")
				scene.set_game_status('radio_has_batteries', True)
				scene.inc_score(2, 'radio_batteries')
				scene.drop('batteries')
			else:
				print ("The radio already has batteries!")
		else:
			print ("You dont have any batteries!")
	elif command == 'save game':
		file_helper.save_game(scene)
	elif command == 'load game':
		file_helper.load_game()
	else:
		print ("Be more specific")

### Testing ###
# state = {'score' : 0, 'score_elements' : {}, 'life' : 10, 'game_status' : {'torch_has_batteries' : True}, 'items' :
# 	{'radio' : True, 'parachute' : True, 'torch' : True, 'batteries' : True, 'gun' : True, 'bullets' : True}}
# from scenes.Stage1Scenes import Cabin
# scene = Cabin(state)
###############

state = {'score' : 0, 'score_elements' : {}, 'life' : 10, 'items' : {}, 'game_status' : {}}
scene = InitialScene(state)
command = ''
while not(scene.dead or scene.success or command == 'exit'):
	if not scene.same_scene:
		scene.describe()
	command = input()
	if command == 'exit':
		break
	elif command.startswith('drop '):
		string_tokens = command.split(' ')
		scene.drop(string_tokens[1])
	elif command == 'inv':
		scene.clear()
		scene.print_inventory(scene.current_state['items'])
		scene.same_scene = True
	elif scene.contains_key(command, GLOBAL_COMMANDS):
		apply_global_action(command, scene)
		scene.same_scene = True
	else:
		scene = scene.apply_action(command)
if scene.dead:
	print ('*** GAME OVER ***')
	print ('*** Thanks for playing! ***')
	print ('Your score is: %d' % scene.current_state['score'])
	print ()
	print_dead()
	input()
elif scene.success:
	print ('Well done! You made it!!!')
	input()
else:
	print ('Thanks for playing, go well!')
	input()
