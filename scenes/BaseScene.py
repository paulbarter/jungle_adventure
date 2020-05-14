
def print_plane():
	print ()
	print ("                                    ___			")
	print ("                                   /  /]		")
	print ("                                  /  / ]		")
	print ("                         _____,. '  /__]		")
	print ("             )        ,-'             _>		")
	print ("               (    _/           ,. '`			")
	print ("              )    / |     _,. '`				")
	print ("              (   /. /    |						")
	print ("               ) ,  /`  ./						")
	print ("              (  \_/   //_ _					")
	print ("               ) /    //  (_)					")
	print ("             _,~'#   (/.						")
	print ("~~~~~~~~~~~~~~~#~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~	")
	print ()

class BaseScene():
	
	def __init__(self, state):
		self.current_state = state
		self.same_scene = False
		self.dead = False
		self.success = False
		
	def take(self, item):
		self.current_state['items'][item] = True

	def drop(self, item):
		self.current_state['items'][item] = False

	def have(self, item):
		return self.current_state['items'].get(item, False)
		
	def game_status(self, item):
		return self.current_state['game_status'].get(item, False)

	def set_game_status(self, status, value):
		self.current_state['game_status'][status] = value
		
	def contains_key(self, command, substring_list):
		for element in substring_list:
			if element in command:
				return True
		return False
		
	def print_inventory(self, inventory):
		print ("You are carrying the following:")
		for key, item in inventory.items():
			print (key)
		
		if len(inventory.items()) == 0:
			print ('Zippy zap, nada, nothing, zuco, nil, zero... You really wish you were carrying something')
	
	def clear(self):
		from os import system
		system('cls')
	
	def describe(self):
		print ('not implemented')
		
	def apply_action(self, command):
		print ('no actions defined')
		
	def inc_score(self, amount, score_keyword):
		if not self.current_state['score_elements'].get(score_keyword, False):
			self.current_state['score'] = self.current_state['score'] + amount
			print ('Congrats! Your score is now: %d' % self.current_state['score'])
			self.current_state['score_elements'][score_keyword] = True
	
from scenes.Stage1Scenes import Plane
	
class InitialScene(BaseScene):

	def my_picture(self):
		print ()
		print ("                                                        ,")
		print ("                                            .__ ._       \_. ")         
		print ("                                     _, _.  '  \/   \.-  /   ")         
		print ("                                      \/     .-_`   // |/     \,")      
		print ("                     .-''''-.          \.   '   \`. ||  \.-'  /   ")    
		print ("                    F        Y        .-.`-(   _/\ V/ \\//,-' >-'   ._,")
		print ("                   F          Y   .__/   `. \.   ' J   ) ./  / __._/  ")
		print ("                  J         \, I    '   _/ \  \  | |  / /  .'-'.-' `._,")
		print ("           (       L   \_.--.| \_.      ' .___ `\: | / .--'.-'      \ ")
		print ("         \ '\    .  L   /    \\/        ._/`-.`  \ .'.' .'---./__   ' ")
		print ("    \__  '\ ) \._/   `-.__. ` \\_. '   .---.  \     /  /  ,   `  `    ")
		print ("  --'  \\  ): // \,            `-.`__.'     `- \  /   / _/-.---.__.- . ")
		print ("     _.-`.'/ /'\_, ._     >--.-'''____.-- `_     '   /.'..' \   \   _/`")
		print (" _ .---._\ \'/ '__./__.-..  / .-|(    x_.-'___  |   :' /    _..---_' \ ")
		print (" .:' /`\ `. `..'.--'\      /.' /`-`._  `-,'   ` '   I '_.--'__--..___.--._.-")
		print ("     `  `. `\/'/  _.   _.-'      _.____./ .-.--''-. .-'    ' _..-.---'   \ ")
		print ("  -._ .--.\ / /-./     /   .---'-//.___. .-'       \__ .--.  `    `.     '`-")
		print (" ,--'/.-. ^.   .-.--.  ` _/    _//     ./   _..   .'  `.    \ \    |_.")
		print ("    /' | >.   ' | \._.-       '    _..'  `.' . `.       )    | |\  `    ")      
		print ("  ./ \ \'  ) c| /  \     \_..  .--'    ,\ \_/`  :    )  (`-. `.|`\\       ")     
		print ("   \'  / ,-.  | ` ./`  ._/ `\\'.--.,-((  `.`.__ |   _/   \    |)  `--._/`   ")  
		print ("______'\   |  < __________  //'  //  _)   )/-._`.  (,-')  )  / \_.    /\. _____")
		print ("            |  |        .__./    //  '\  |//    `.\ '\ (  (  <`   ._  '")
		print ("           >  |      _.  /   ..-\ _    _/ \_.  \ `\    \_ `---.-'__   ")
		print ("        . /  `-   _.'        /   `   _/|       J  /`     `-,,-----.`-.")
		print ("            '  .:'          '`      '          < `   f  I //        `�\_,")

	def describe(self):
		self.clear()
		print ('Thick jungle is all around')
		print ()
		self.my_picture()

	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look':
			scene.clear()
			print ('There are trees all around you. Too thick to move.')
			print ()
			self.my_picture()
		elif command == 'look tree':
			print ('There are all kinds of interesting trees totally blocking your view.')
		elif 'climb' in command:
			print ('you climb the nearest tree and see your plane smoking in the distance')
			self.inc_score(1, 'climb')
			scene = InTree(self.current_state)
		elif 'look' in command and ('pocket' in command or 'clothes' in command):
			if not self.current_state['items'].get('radio', False):	
				print ('You find a 2 way radio in your pocket!')
				self.inc_score(1, 'radio')
				self.current_state['items']['radio'] = True
			else:
				print ('Your pocket has some fluff in it')
		elif 'radio' in command:
			if self.current_state['items'].get('radio', False):
				print ('You radio your plane for help and your co-pilot finds you!')
				self.inc_score(5, 'copilot')
				print ('You are inside your plane. Your co-pilot is injured and after saving you dies...')
				scene = Plane(self.current_state)
			else:
				print ('You really wish you had a radio :(')
		elif command == 'hint':
			print ('You cant see anything from down here, if only you could get a better view...')
		else:
			print ('You cant do that')
		return scene		

class InTree(BaseScene):
		
	def describe(self):
		print ('Your plane is just out of reach')
		
	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look':
			self.describe()
		elif command == 'look plane':
			print ('You notice that your co-pilot is still alive in the plane!')
			self.inc_score(1, 'look copilot')
		elif 'climb' in command:
			scene = InitialScene(self.current_state)
			scene.same_scene = False
		elif 'jump' in command:
			print ('From way up here your jump down is deadly. You fall hard hitting your head and die')
			scene.dead = True
		elif command == 'hint':
			print ('If only you had a way to contact someone. Didnt the company give you something...')
		elif 'look' in command and ('pocket' in command or 'clothes' in command):
			if not self.current_state['items'].get('radio', False):	
				print ('You find a 2 way radio in your pocket!')
				self.inc_score(1, 'radio')
				self.current_state['items']['radio'] = True
			else:
				print ('Your pocket has some fluff in it')
		elif 'radio' in command:
			if self.current_state['items'].get('radio', False):
				print ('You radio your plane for help and your co-pilot finds you!')
				self.inc_score(5, 'copilot')
				print ('You are inside your plane. Your co-pilot is injured and after saving you dies...')
				scene = Plane(self.current_state)
			else:
				print ('You really wish you had a radio :(')
		else:
			print ('You cant do that')
		return scene