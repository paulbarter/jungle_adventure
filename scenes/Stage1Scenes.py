from scenes.BaseScene import BaseScene
from scenes.BaseScene import print_plane
from scenes.Maze import StartMaze

class Plane(BaseScene):

	def describe(self):
		print_plane()
		
	def print_chair(self):
		print("")
		print("   i______i")
		print("   I______I")
		print("   I      I")
		print("   I______I")
		print("  /      /I")
		print(" (______( I")
		print(" I I    I I")
		print(" I      I")
		print("")
		
	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look':
			self.describe()
		elif command == 'look plane':
			print ('Standard passenger plane, with a standard huge hole through the engine. It will never fly again.')
			print ('The only things left unbroken are the seat and the roof.')
		elif command == 'look seat':
			print ('Its a normal plane seat. Strange its not also broken')
		elif command == 'look under seat':
			self.clear()
			if not self.current_state['items'].get('parachute', False):	
				print ('You look under the seat and find a parachute!')
				self.print_chair()
				self.inc_score(2, 'parachute')
				self.current_state['items']['parachute'] = True
			else:
				print ('Nothing interesting left under the seat')
		elif 'exit plan' in command or 'leave' in command:
			scene = LeavePlane(self.current_state)
		elif command == 'hint':
			print ('There might be something useful in this cockpit...')
		else:
			print ('You cant do that')
		return scene
		
class LeavePlane(BaseScene):

	def describe(self):
		self.clear()
		print ('It is beautiful out here, and you could enjoy it if you werent lost, tired and starving')
		print ()
		print ("  .                    .-.    .  _   *     _   .						")
		print ("           *          /   \     ((       _/ \       *    .			")
		print ("         _    .   .--'\/\_ \     `      /    \  *    ___			")
		print ("     *  / \_    _/ ^      \/\'__        /\/\  /\  __/   \ *			")
		print ("       /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .		")
		print ("  .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _		")
		print ("     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \		")
		print ("   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \		")
		print ("  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.	")
		print ("@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%	")
		print ()
		print ("Directions:")
		print ("1: Forest")
		print ("2: Plane")
		print ("3: Mountains")
		print ("4: Cliff")
		print ()
		
	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look':
			self.describe()
		elif command == '1':
			scene = Forest(self.current_state)
		elif command == '2':
			scene = Plane(self.current_state)
		elif command == '3':
			self.clear()
			print ('You walk down a path to the mountains and come upon a cave')
			scene = Mountains(self.current_state)
		elif command == 'hint':
			print ('You really need to go somewhere...')
		else:
			print ('You cant do that')
		return scene
		
class Mountains(BaseScene):

	def describe(self):
		print ("		___..-.  			")            
		print ("     ._/  __ \_`-.__       	")
		print ("     / .'/##\_ `-.  \--.  	")
		print ("     .-_/#####\  /-' `\_    ")
		print ("      /###@@###\_  \._   `- ")
		print ("    _|###########\_`.  -' \ ") 
		print ()
		print ("Directions:")
		print ("1: Cave")
		print ("2: Back to Plane")
		print ()
		
	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look':
			print ('The cave dominates your view')
			self.describe()
		elif command == 'look cave':
			print ('The cave looks dangerous')
		elif command == '1':
			scene = Cave(self.current_state)
		elif command == '2':
			scene = LeavePlane(self.current_state)
		elif command == 'hint':
			print ('Wouldnt go in that cave if I were you')
		else:
			print ('You cant do that')
		return scene
		
class Cave(BaseScene):

	def describe(self):
		print ('The cave is home to a fierce wolf!!!')
		print ()
		print ("                            .d$$b		")
		print ("                          .' TO$;\		")
		print ("                         /  : TP._;		")
		print ("                        / _.;  :Tb|		")
		print ("                       /   /   ;j$j		")
		print ("                   _.-'       d$$$$		")
		print ("                 .' ..       d$$$$;		")
		print ("                /  /P'      d$$$$P. |\	")
		print ("               /   '      .d$$$P' |\^'l	")
		print ("             .'           `T$P^'''''  :	")
		print ("         ._.'      _.'                ;	")
		print ("      `-.-'.-'-' ._.       _.-'    .-'	")
		print ("    `.-' _____  ._              .-'		")
		print ("   -(.g$$$$$$$b.              .'		")
		print ("     ''^^T$$$P^)            .(:			")
		print ("       _/  -'  /.'         /:/;			")
		print ("    ._.'-'`-'  ')/         /;/;			")
		print (" `-.-'..--''   ' /         /  ;			")
		print (".-' ..--''        -'          :			")
		print ("..--''--.-'         (\      .-(\		")
		print ("  ..--''              `-\(\/;`			")
		print ("    _.                      :			")
		print ("                            ;`-			")
		print ("                           :\			")

	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look': 
			if self.game_status('wolf_dead'):
				print ('You cant see anything except for the dead wolf lying on the floor. The rest of the cave is pitch black')
			else:
				self.describe()
		elif self.contains_key(command, ['kill', 'attack', 'touch', 'kick', 'stroke']) and not self.game_status('wolf_dead'):
			print ('The wolf takes one swift bite and you die!')
			self.dead = True
		elif command == 'leave':
			if self.game_status('wolf_dead'):
				print ('There seems to be no way out!')
			else:
				scene = Mountains(self.current_state)
		elif self.contains_key(command, ['shoot', 'use gun', 'fire']) and self.have('gun') and not self.game_status('wolf_dead'):
			if self.have('bullets'):
				print ('With a mighty bang you slay the wolf! The huge explosion causes a rockfall blocking the exit to the cave!')
				if not self.game_status('torch_has_batteries'):
					print ('Without any light it is hopeless, you search for what seems like days and eventually you ' \
						   'starve to death trying to find a way out.')
					self.dead = True
				else:
					self.current_state['game_status']['wolf_dead'] = True
					self.drop('bullets')
			else:
				print ('Your gun has no bullets... darn!')
		elif self.contains_key(command, ['use torch', 'turn on torch', 'switch on torch']):
			if self.have('torch'):
				if self.have('batteries') and self.game_status('torch_has_batteries'):
					if self.game_status('wolf_dead'):
						print('You switch on the torch and notice what looks like a tunnel, you walk closer and stumble ' \
							  'into what looks like a maze!!!')
						scene = StartMaze(self.current_state)
					else:
						print ('No time to use the torch - there is a deadly wolf in front of you!')
				else:
					print ('The torch has no batteries... its useless!')
			else:
				print ('Yes a torch would be soooo useful right now!')
		elif command == 'hint':
			print ('There is no taming that wolf')
		else:
			print ('You cant do that')

		return scene

class Forest(BaseScene):

	def describe(self):
		print ('You find a cabin in the wood')
		print ("                                            /\ 							")
		print ("/\                                         /%%\  /\						")
		print ("%%\            ,                          /%%%%\/%%\					")
		print ("%%%\          ,~,                /\       /%%%%/%%%%\    ,   /\			")
		print ("%%%\         ,~~~,   /\         /%%\  /\ /%%%%%//\%%\/\ ,~, /%%\		")
		print ("%%%%\  /\   ,~~~~~, /%%\   /\   /%%\ /%%\%/\%/\/%%\%/%%\~~~/%%%%\		")
		print ("%%%%\ /%%\ /\~~~~~~/%%%%\ /%%\ /%%%%\/%%\/%%\%%\%%%/%(%%\~~/%%%%\		")
		print ("%%%%%\/%%\/%%\~/\~~/%%%%\/%%%%/%%%%%%\%%/%%%%\%%\%%/)%%%\~/%%%%%%\		")
		print ("%/\%%/%%%%\%%%/%%\/%%%%%%\%%/\/%%/\%%\%%/\%%%\%%\%%(%%%%%/%%%%%%%%\ 	")
		print ("/%%\/%%%%%%\/\/%%\/%%%%%%\%/%%\%/%%\%%\/%%\_______[_]________%%%%%\		")
		print ("%%%%/%%%%%%/%%\%%/%%%%%%%%\/%%\%/%%\%%/%%%%\ _-       _-  _- \%%%%%\	")
		print ("%%%/%%%%%%%/%%\%%/%%/\%%%%/%%%%\%%%%\/%%%%%%\______-__________\''','	")
		print ("lc/%%%%%%%/%%%%\/%%/%%\%%%/%%%%\%%%%\/%%%%%%\__===______====_]   ,~,  _-")
		print ("''/%%%%%%/%%%%%%,%%/%%\%%/%%%%%%\%%%/%%%%%%%%\_|_|______|  |_]  ,~~~,	")
		print (" /%%%%%%%/%%%%%,~,/%%%%\/%%%%%%%%\%/%%%%%%%%%%\_________|- |_] ,~~~~~,	")
		print (" /%%%%%%/%%%%%,~~~,%%%%\/%%%%%%%%\%/%%%%%%%%%%\___#__#__|__|_],~~~~~~~,	")
		print ("/%%%%%#%/#%%%,~~~~~,%%%/%%%%%%%%%%/%%%%%%%%%%%%\'''\/'''/  \'  ,~~;~~,	")
		print ("'''''''\/''',~~~~~~~,''/%%%%%%%%%/%%%%%%%%%%%%%%\   _-            |		")
		print (" -_          ,~~;~~,   ''''''''''/%%%%%%%%%%%%%%\       ^^      ~'''~	")
		print ("      ^^        |   ,    _-     /%%%%%%%%%%%%#%%#\        _-			")
		print ("            _-    ,`|`,         ''''''''''''''\/''   _-          _-		")
		print ("  _-               \ /           _-         _-   ~~  					")
		print ("                  ~'''~													")
		print ("Directions:")
		print ("1: Cabin")
		print ("2: Back to Plane")
		print ()
		
	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look': 
			self.describe()
		elif command == 'look cabin':
			print ('The cabin looks charming')
		elif command == '1':
			scene = Cabin(self.current_state)
		elif command == 'leave' or command == '2':
			scene = LeavePlane(self.current_state)
		elif command == 'hint':
			print ('Go in the cabin! ... then again you remember little red riding hood...')
		else:
			print ('You cant do that')
		return scene
		
class Cabin(BaseScene):

	def describe(self):
		print ('The cabin is empty')
		print ("")
		print ("0================================================0	")
		print ("|'.                    (|)                     .'|	")
		print ("|  '.                   |                    .'  |	")
		print ("|    '.                |O|                 .'    |	")
		print ("|      '. ____________/===\_____________ .'      |	")
		print ("|        :            `\"/`  ______     :     .. |	")
		print ("|        :     mmmmmmm  V   |--%%--|    :   .'|| |	")
		print ("|        :     |  |  |      |-%%%%-|    :  |  || |	")
		print ("|        :     |--|--| @@@  |=_||_=|    :  I  || |	")
		print ("|        :     |__|__|@@@@@ |_\__/_|    :  |  || |	")
		print ("|        :             \|/   ____       :  |  || |	")
		print ("|        :;;       .'``(_)```\__/````:  :  |  || |	")
		print ("|        :||___   :================:'|  :  | ++| |	")
		print ("|        :||===)  | |              | |  :  |  || |	")
		print ("|        ://``\|__|_|______________|_|__:  I  || |	")
		print ("|      .'/'   |\' | '              | '   '.|  || |	")
		print ("|    .'           |                |       '. || |	")
		print ("|  .'                                        '|| |	")
		print ("|.'                                            '.|	")
		print ("0================================================0	")
		print ()
		
	def apply_action(self, command):
		scene = self
		scene.same_scene = True
		if command == 'look': 
			self.describe()
			if self.have('flowers'):
				print ('but the flowers are gone')
		elif command == 'look cabin':
			print ('The cabin looks as charming from the inside and it does from the outside.')
			print ('Chair, table and cupboard')
		elif command == 'look chair':
			print ('The chair is just right')
		elif self.contains_key(command, ['sit', 'sit down', 'use chair']):
			print ('Aaaaaaah... comfortable')
		elif command == 'look table':
			print ('A lovely bunch of flowers and an empty fruit bowl sit on the table')
		elif command == 'look bowl':
			print ('The bowl is empty... pitty, you are hungry')
		elif command == 'look window':
			print ('The view is amazing!')
		elif self.contains_key(command, ['get flowers', 'take flowers']) and not self.have('flowers'):
			print ('You take the flowers and notice a piece of paper in the empty vase')
			print ('The paper says: "17462"')
			self.inc_score(2, 'flowers')
			self.current_state['items']['flowers'] = True
		elif command == 'leave':
			scene = Forest(self.current_state)
		elif command == 'look cupboard':
			if self.have('gun'):
				print ('The cuboard is now empty')
			else:
				print ('The cupboard has a combination lock on it... what code do you try?')
				code = input()
				if code == '17462':
					self.inc_score(2, 'gun')
					self.take('gun')
					print ('The cupboard swings open...')
					print (" ,______________________________________       						")
					print ("|_________________,----------._ [____]  ''-,__  __....-----=====	")
					print ("               (_(||||||||||||)___________/   ''                |	")
					print ("                  `----------'        [ ))'-,                   |	")
					print ("                                       ''    `,  _,--....___    |	")
					print ("                                               `/           ''''	")
					print ('You help yourself to the shotgun... pity its not loaded :(')
				else:
					print ('No good... wrong code!')
		elif command == 'hint':
			print ('Wood cabins like this one are usually owned by dangeous woodsmen')
		else:
			print ('You cant do that')
		return scene