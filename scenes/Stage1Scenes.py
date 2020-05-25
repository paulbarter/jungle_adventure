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
            if not scene.game_status('bury stan'):
                print ('The co-pilot Stan is dead on the floor.')
        elif command == 'look seat':
            print ('Its a normal plane seat. Strange its not also broken')
        elif scene.contains_key(command, ['look Stan', 'look co-pilot', 'look stan']):
            print ('Stan lies heroically in a slump on the floor. You only hope that you can be as brave as him.')
        elif scene.contains_key(command, ['search stan', 'search Stan', 'search co-pilot']):
            print ('You would never violate the memory of your friend by searching him!')
        elif scene.contains_key(command, ['bury Stan', 'bury stan', 'bury co-pilot']):
            print ('A noble thing to do. You bury Stan in the jungle and return to your plane')
            scene.inc_score(3, 'bury stan')
            scene.set_game_status('bury stan', True)
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
        if self.game_status('out_maze'):
            print ('You made it out of the maze!!! Well done!!! A flood of fresh air and light fills you with joy!')
            print (
                'You have come out of a tunnel in the ground that you didn"t notice before and find yourself back at the mountains.')
        else:
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
        elif command == '4':
            scene = Cliff(self.current_state)
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
            if scene.game_status('wolf_dead'):
                print (
                    'The entrance to the cave is blocked because of the rock fall. Anyways, you dont want to go back in there, it was nasty!')
            else:
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
        if self.game_status('wolf_dead'):
            print ('The cave is dark')
        else:
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
                print (
                    'You cant see anything except for the dead wolf lying on the floor. The rest of the cave is pitch black')
            else:
                self.describe()
        elif self.contains_key(command, ['kill', 'attack', 'touch', 'kick', 'stroke']) and not self.game_status(
                'wolf_dead'):
            print ('The wolf takes one swift bite and you die!')
            self.dead = True
        elif command == 'leave':
            if self.game_status('wolf_dead'):
                print ('There seems to be no way out!')
            else:
                scene = Mountains(self.current_state)
        elif self.contains_key(command, ['shoot', 'use gun', 'fire']) and self.have('gun') and not self.game_status(
                'wolf_dead'):
            if scene.game_status('gun_loaded'):
                print (
                    'With a mighty bang you slay the wolf! The huge explosion causes a rockfall blocking the exit to the cave!')
                if not self.game_status('torch_has_batteries'):
                    print ('Without any light it is hopeless, you search for what seems like days and eventually you ' \
                           'starve to death trying to find a way out.')
                    self.dead = True
                else:
                    self.current_state['game_status']['wolf_dead'] = True
            else:
                print ('Your gun has no bullets... darn!')
        elif self.contains_key(command, ['use torch', 'turn on torch', 'switch on torch']):
            if self.have('torch'):
                if self.game_status('torch_has_batteries'):
                    if self.game_status('wolf_dead'):
                        scene.inc_score(2, 'used_torch')
                        print(
                            'You switch on the torch and notice what looks like a tunnel, you walk closer and stumble ' \
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
            if self.have('map'):
                print ('No need to go in there any more, you have what you need from the woodsman.')
            elif self.game_status('giant_humour') >= 3:
                from scenes.OgreInCabin import HappyOgre
                scene = HappyOgre(self.current_state)
            elif self.game_status('wolf_dead'):
                from scenes.OgreInCabin import Ogre
                scene = Ogre(self.current_state)
            else:
                scene = Cabin(self.current_state)
        elif command == 'leave' or command == '2':
            scene = LeavePlane(self.current_state)
        elif command == 'hint':
            print ('Go in the cabin! ... then again you remember little red riding hood...')
        else:
            print ('You cant do that')
        return scene

class Goat(BaseScene):

    def describe(self):
        if self.have('bullets'):
            print ("The goat is munching away")
        else:
            print(
                'The goat looks at you in surprise. You can see a store cupboard behind the goat. But the goat looks like it wont budge.')

        print("")
        print("                                                .--____.				")
        print("                     ,_____._,                ,~-__,__,;\				")
        print("                   ,/ /  / /~,\              ~'-_ ,~_/__--\				")
        print("                 ,~'\/__:_; / ~\,_          /-__ ~\/  \ ;/,\			")
        print("                / \ ,/\_\_~\ /  /|,';;;;`,|\  /\/     \=/- |			")
        print("               ~--,/_/__  \ ~\ |  `._____.'  |/\/     __---=--			")
        print("              /==/./ \ /\  ;\~\_\          _/\/,,__--'._/-' `			")
        print("             |==|/    \==\;  ;\|  , \ \ / /L /::/ \,~~ |==|-|			")
        print("             |//\\,__/== |: ;  |L_\  \ V / /L::/-__/  /=/-,|			")
        print("              \ / | | \ /: ;  ;\ |\\  \ / //|: |__\_/=/--/,,			")
        print("               \______,/; ;   ;;\ @|\  | /|@|;: \__\__\_/  ``,,			")
        print("                     ,;  ;   ;;;|\/' \ |/ '\/;;               '',=``,	")
        print("                    ,;  ;   ;;;;\  {  \|' }/;:'                  ,;;;	")
        print("                    ,;  ;  ;;;;;:| {   |  }|;'                    , ;;;		")
        print("                   ,; ;' ::::::;/    ./ \  \                        :, --	")
        print("                  ,;;;;`,'`'`';/   ./    \  \_                       :,	")
        print("                  ,;;     '''|____/   \__/\___|                       :,	")
        print("                  ,;;             \_.  / _/                            :,	")
        print("                  ,;;                \/\/                               :,	")
        print("                  ,;;                                                    :,	")
        print("                  ,;;                                                    :,	")
        print("                  ,;;,                         ,--------.,       :;      :,	")
        print("                   `:';__--                   /       .   \,     :;      :,	")
        print("        .___________--`                      |        \    \___  :;      :,	")
        print("       /                                    |:        | ;  \  \ :;       :,	")
        print("      |                                     ;;;      / ;    |   :;      :.	")
        print("     |:                       /             ;;;     | ,;    |  :;    ,,:'	")
        print("     ;;;     /--;:,:;,,:;;;,;/';,,,,,,,,,,';;:    /  ;      |,;:,,,;:'		")
        print("     ;:;    |`'';;;';';;'';;;         |   ;;:     / :;      |;;;'  |		")
        print("     ;;    /                          |  ;;:     / :;-_____/   |   |		")
        print("     ;:   |                           / ;;:     / :;           |   \		")
        print("     ;     |                         |:,;;     | :;            /    |		")
        print("    ;      |                         /-;'   ':| ;:            |:,,;/		")
        print("    |:  ,;/                         |  ;      |:;             /-__-\		")
        print("     ;   |                          \  ::,,,:/:;             |      |		")
        print("     /   |                           \/`\    |:;             \  /\  /		")
        print("    /-____\                              |    \'              \/'`\/		")
        print("   |      `)                            /-____-\							")
        print("   | ^   /                             |        |							")
        print("   |/`\/                               |        |							")
        print("                                        \  /\  /							")
        print("                                         \/'`\/								")
        print()

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'feed goat':
            print ('What are you going to feed the goat with?')
        elif self.contains_key(command,
                               ['give flowers', 'offer flowers', 'feed goat with flowers', 'feed goat flowers']):
            if self.have('flowers'):
                print('The goat takes the flowers greedily, allowing you to open the store cupboard. You find...')
                print ('press enter...')
                input()
                print ('a torch with no batteries and some shot gun bullets!')
                self.take('bullets')
                self.take('torch')
                self.inc_score(3, 'bullets')
                self.set_game_status('fed_goat', True)
                self.drop('flowers', silent=True)
            else:
                print ('You dont have any flowers')
        elif self.contains_key(command, ['hit', 'kick', 'punch', 'stroke', 'ride', 'pet']):
            print('The goat doesnt like that! He butts you a good shot. Ow!')
            self.damage(4)
        elif command == 'hint':
            print('You need to get that goat to move somehow.')
        elif command == 'leave':
            scene = Cabin(self.current_state)
        else:
            print('You cant do that')
        return scene


class Cabin(BaseScene):

    def describe(self):
        print ('The cabin is empty')
        print ("")
        if self.game_status('fed_goat') or self.have('flowers'):
            print("")
            print("0================================================0	")
            print("|'.                    (|)                     .'|	")
            print("|  '.                   |                    .'  |	")
            print("|    '.                |O|                 .'    |	")
            print("|      '. ____________/===\_____________ .'      |	")
            print("|        :            `\\ /`  ______     :     .. |	")
            print("|        :     mmmmmmm  V   |--%%--|    :   .'|| |	")
            print("|        :     |  |  |      |-%%%%-|    :  |  || |	")
            print("|        :     |--|--|      |=_||_=|    :  I  || |	")
            print("|        :     |__|__|      |_\__/_|    :  |  || |	")
            print("|        :                   ____       :  |  || |	")
            print("|  |''.  :;;       .'``(_)```\__/````:  :  |  || |	")
            print("|  |   | :||___   :================:'|  :  | ++| |	")
            print("|  |   | :||===)  | |              | |  :  |  || |	")
            print("|  |  +| ://``\|__|_|______________|_|__:  I  || |	")
            print("|  |   |.'/'   | '| '              | '   '.|  || |	")
            print("|  |   |.'        |                |       '. || |	")
            print("|  |.'                                       '|| |	")
            print("|.'                                            '.|	")
            print("0================================================0	")
        else:
            print (" 0================================================0	")
            print (" |'.                    (|)                     .'|	")
            print (" |  '.                   |                    .'  |	")
            print (" |    '.                |O|                 .'    |	")
            print (" |      '. ____________/===\_____________ .'      |	")
            print (" |        :            `\\ /`  ______     :      ..|	")
            print (" |        :     mmmmmmm  V   |--%%--|    :   .'|| |	")
            print (" |        :     |  |  |      |-%%%%-|    :  |  || |	")
            print (" |        :     |--|--| @@@  |=_||_=|    :  I  || |	")
            print (" |        :     |__|__|@@@@@ |_\__/_|    :  |  || |	")
            print (" |        :             \\|/   ____       :  |  || |	")
            print(" |  |''.  :;;       .'``(_)```\__/````:  :  |  || |	")
            print(" |  |   | :||___   :================:'|  :  | ++| |	")
            print(" |  |   | :||===)  | |              | |  :  |  || |	")
            print(" |  |  +| ://``\|__|_|______________|_|__:  I  || |	")
            print(" |  |   |.'/'   | '| '              | '   '.|  || |	")
            print(" |  |   |.'        |                |       '. || |	")
            print(" |  |.'                                       '|| |	")
            print(" |.'                                            '.|	")
            print(" 0================================================0	")
        print ()

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'look cabin':
            print ('The cabin looks as charming from the inside and it does from the outside.')
            print ('Chair, table, cupboard and door leading off')
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
        elif command == 'look flowers':
            print ('The flowers look beautiful')
        elif command == 'look door':
            print ('The door looks unlocked')
        elif command == 'open door':
            print ('You walk through the door to the back garden where you are greeted by a goat.')
            scene = Goat(self.current_state)
        elif self.contains_key(command, ['get flowers', 'take flowers']) and not self.game_status(
                'taken_flowers') and not self.have('flowers'):
            print ('You take the flowers and notice a piece of paper in the empty vase')
            print ('The paper says: "17462"')
            scene.set_game_status('taken_flowers', True)
            scene.inc_score(2, 'flowers')
            scene.current_state['items']['flowers'] = True
            scene.describe()
        elif command == 'leave':
            scene = Forest(self.current_state)
        elif scene.contains_key(command, ['look cupboard', 'open cupboard']):
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


class Cliff(BaseScene):

    def describe(self):
        print ('You come to a massive cliff where a raging river thunders over the edge...')
        print ("")
        print ("                              _____,,, //,, ,/,     ")
        print ("                             /-- --- --- -----      ")
        print ("                            ///--- --- -- - ----    ")
        print ("                           o////- ---- --- --       ")
        print ("                           !!//o/---  -- --         ")
        print ("                         o*) !///,~,,  ,\/,,/,//,,  ")
        print ("                           o!*!o'(\          /\     ")
        print ("                         | ! o ',) \/\  /\  /  \/\  ")
        print ("                        o  !o! !!|    \/  \/     /  ")
        print ("                       ( * (  o!'; |\   \       /   ")
        print ("                        o o ! * !` | \  /       \   ")
        print ("                       o  |  o 'o| | :  \       /   ")
        print ("                        *  o !*!': |o|  /      /    ")
        print ("                            (o''| `| : /      /     ")
        print ("                            ! *|'`  \|/       \     ")
        print ("                           ' !o!':\  \         \    ")
        print ("                            ( ('|  \  `._______/    ")
        print ("////\\\,,\///,,,,\,/oO._*  o !*!'`  `.________/     ")
        print ("  ---- -- ------- - -oO*OoOo (o''|           /      ")
        print ("    --------  ------ 'oO*OoO!*|'o!!          \      ")
        print ("-------  -- - ---- --* oO*OoO *!'| '         /      ")
        print (" ---  -   -----  ---- - oO*OoO!!':o!'       /       ")
        print (" - -  -----  -  --  - *--oO*OoOo!`         /        ")
        print ()

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'look river':
            print ('The river is powerful!')
        elif self.contains_key(command, ['swim']):
            print (
                'You foolishly take a running leap into the deadly river. You fight for breath and the river swirls you around, but you cannot break free and drown.')
            self.dead = True
        elif self.contains_key(command, ['jump', 'leap']):
            print ('You say a quick prayer and jump off the cliff and die instantly on the rocks below.')
            self.dead = True
        elif command == 'look cliff':
            print ('You edge slowly to the edge of the cliff and peer down. It is 100"s of metres to the bottom!')
        elif command == 'look down':
            print ('Never, ever look down!')
        elif self.contains_key(command, ['climb']):
            print (
                'You start climbing your way down the immense cliff. It is going well until you realise that the wet rocks make it impossible to climb.')
            print (
                "Defeated you start climbing back up. A rock comes loose! You swing one handed into the cliff face and crash your head into the rock.")
            print ("Stunned for a moment, you recover and drag your aching body back up the cliff")
            self.damage(4)
        elif self.contains_key(command, ['parachute']):
            if self.have('map'):
                print ('With the map and compass you feel confident you will be able to find your way wherever you land. You put on the parachute, wait for a gust of wind and take to the skies, like an..... <press enter>')
                input()
                print (
                    'Like an EAGLE!!! You glide down the cliff and land with a bump safely on the ground. Well done!!! You have made it to level 2!')
                print (
                    'Now you will just have to wait until Paul makes level 2... Until then, happy adventuring!')
                self.inc_score(10, 'parachute')
            else:
                print (
                    'You would never take a leap off the cliff unless you knew exactly where you were going when you landed.')
        elif command == 'leave':
            scene = LeavePlane(self.current_state)
        elif command == 'hint':
            print ('The way down the cliff could be your only way out, if only you could find a safe way to do that.')
        else:
            print ('You cant do that')
        return scene

