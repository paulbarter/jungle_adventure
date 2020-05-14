# from scenes.BaseScene import BaseScene, InTree, InitialScene
from scenes.BaseScene import InitialScene
from scenes.BaseScene import print_plane

print ()
print ('----------------------------------------------------------------')
print ('**************** Welcome to Jungle adventure!!! ****************') 
print ('Type "hint" if you are stuck and type "exit" if you want to quit')
print ('Type "inv" to see what you are carrying')
print ('----------------------------------------------------------------')
print ()
print ('Your plane crashed in a dense jungle, you are thrown from your plane in the crash...')
print_plane()
print ('Press Enter...')
input()
from os import system
system('cls')

def print_dead():
	print("								")
	print("		     -|-				")
	print("		      |					")
	print("	   	  .-'~~~`-.				")
	print("	 	.'         `.			")
	print("	 	|  R  I  P  |			")
	print("	 	|           |			")
	print("	 	|           |			")
	print("     |           |			")
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^	")

### Testing ###
state = {'score' : 0, 'score_elements' : {}, 'life' : 10, 'game_status' : {'torch_has_batteries' : True}, 'items' :
	{'radio' : True, 'parachute' : True, 'torch' : True, 'batteries' : True, 'gun' : True, 'bullets' : True}}
from scenes.Stage1Scenes import Cave
scene = Cave(state)
###############

# state = {'score' : 0, 'score_elements' : {}, 'life' : 10, 'items' : {}, 'game_status' : {}}
# scene = InitialScene(state)
command = ''
while not(scene.dead or scene.success or command == 'exit'):
	if not scene.same_scene:
		scene.describe()
	command = input()
	if command == 'exit':
		break
	elif command == 'inv':
		scene.clear()
		scene.print_inventory(scene.current_state['items'])
		scene.same_scene = True
	else:
		scene = scene.apply_action(command)
if scene.dead:
	print ('*** GAME OVER ***')
	print ('*** Thanks for playing! ***')
	print ()
	print_dead()
elif scene.success:
	print ('Well done! You made it!!!')
else:
	print ('Thanks for playing, go well!')
