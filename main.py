# from scenes.BaseScene import BaseScene, InTree, InitialScene
from scenes.BaseScene import InitialScene
from scenes.BaseScene import print_plane
def print_menu():
	print('----------------------------------------------------------------')
	print('**************** Welcome to Jungle adventure!!! ****************')
	print('Useful Commands:')
	print()
	print('"hint" if you are stuck')
	print('"exit" if you want to quit')
	print('"status" to see what you are carrying, your score and your life')
	print('"load game" to load a saved game')
	print('"save game" to save your game')
	print('"delete game" to delete a saved game')
	print('"help" for information about how to play this kind of game')
	print('"menu" to show this menu')
	print('----------------------------------------------------------------')

print ()
print_menu()
print ()
print ('Press Enter to begin...')
input ()
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

GLOBAL_COMMANDS = ['load gun', 'put bullets in gun', 'look radio', 'menu', 'help', 'delete game', 'load game', 'save game', 'take batteries out', 'take batteries out of torch', 'take batteries out torch', 'take batteries out radio', 'take batteries out of radio', 'take out batteries', 'put batteries in torch', 'put batteries in radio', 'put batteries into torch', 'put batteries into radio']

def apply_global_action(command, scene):
	if command == 'take batteries out' or command == 'take out batteries' or command == 'take batteries out of torch' or command == 'take batteries out of radio'\
			or command == 'take batteries out torch' or command == 'take batteries out radio':
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
				scene.drop('batteries', silent=True)
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
				scene.drop('batteries', silent=True)
			else:
				print ("The radio already has batteries!")
		else:
			print ("You dont have any batteries!")
	elif scene.contains_key(command, ['load gun', 'put bullets in gun']):
		if scene.have('gun') and scene.have('bullets'):
			if scene.game_status('gun_loaded'):
				print ('The gun is already loaded')
			else:
				print ('You load the gun. Ahhhh, you feel 10 feet tall... However you wish you spent more time in the shooting range...')
				scene.set_game_status('gun_loaded', True)
				scene.drop('bullets', silent=True)
		else:
			print ('You dont have that')
	elif command == 'look radio':
		if scene.have('radio'):
			print ('A standard T1000 army issue 2 way radio.')
			print("     .       ")
			print("   \   /     ")
			print(" -=  o  =-   ")
			print("   / | \     ")
			print("     |       ")
			print("     |       ")
			print("     |       ")
			print("     |=====. ")
			print("     |.---.| ")
			print("     ||=o=|| ")
			print("     ||   || ")
			print("     ||   || ")
			print("     ||___|| ")
			print("     |[:::]| ")
			print("     '-----' ")
		else:
			print ('You dont have a radio')
	elif command == 'save game':
		file_helper.save_game(scene)
	elif command == 'load game':
		scene = file_helper.load_game(scene)
	elif command == 'delete game':
		file_helper.delete_game()
	elif command == 'help':
		scene.print_help()
	elif command == 'menu':
		print_menu()
	else:
		print ("Be more specific")
	return scene

def run_game(scene, command):
	while not (scene.dead or scene.success or command == 'exit'):
		if not scene.same_scene:
			scene.describe()
		command = input()
		if command == 'exit':
			print ('Thanks for playing, come back soon!')
			input()
			break
		elif command.startswith('drop '):
			string_tokens = command.split(' ')
			scene.drop(string_tokens[1])
		elif command == 'status':
			scene.clear()
			scene.print_status()
			scene.same_scene = True
		elif scene.contains_key(command, GLOBAL_COMMANDS):
			scene = apply_global_action(command, scene)
			if scene:
				if command == 'load game':
					scene.same_scene = False
				else:
					scene.same_scene = True
		else:
			scene = scene.apply_action(command)

	if scene.dead:
		print('*** GAME OVER ***')
		print('*** Thanks for playing! ***')
		print('Your score is: %d' % scene.current_state['score'])
		print()
		print_dead()
		print()
		print('Type: "L": to load a saved game, "S": start from the beginning or anything else to exit')
		ans = input()
		if ans.lower() == 'l':
			scene = file_helper.load_game(scene)
			run_game(scene, '')
		elif ans.lower() == 's':
			state = {'score': 0, 'score_elements': {}, 'life': 10, 'items': {}, 'game_status': {}}
			scene = InitialScene(state)
			run_game(scene, '')
		else:
			print('Thanks for playing, come back soon!')
			input()
	elif scene.success:
		print('Well done! You made it!!!')
		input()

### Testing ###
# state = {'score' : 0, 'score_elements' : {}, 'life' : 10, 'game_status' : {'torch_has_batteries' : True}, 'items' :
# 	{'radio' : True, 'parachute' : True, 'torch' : True, 'batteries' : True, 'gun' : True, 'bullets' : True}}
# from scenes.Stage1Scenes import Cabin
# scene = Cabin(state)
###############

state = {'score' : 0, 'score_elements' : {}, 'life' : 10, 'items' : {}, 'game_status' : {}}
scene = InitialScene(state)
command = ''
run_game(scene, command)

