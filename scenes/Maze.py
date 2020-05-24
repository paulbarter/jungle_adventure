from scenes.BaseScene import BaseScene
try:
    from scenes.Stage1Scenes import Cave, LeavePlane
except Exception as err:
    h = 3

from lib.Monsters import Bat, Snake, Minotaur, Player, Attacking

class MazeScene(BaseScene):

    def _do_the_fight(self, monster, scene):
        monster.describe_monster()
        print('1: Fists')
        print('2: Gun')
        print('3: Torch')
        if scene.have('knife'):
            print('4: Knife')
        weapon = input()
        if weapon == '1':
            player = Player(scene.current_state['life'], 2, 5, 'swing your fists', 'fists')
        elif weapon == '2':
            player = Player(scene.current_state['life'], 1, 1, 'shoot blindly into the dark', 'gun')
        elif weapon == '3':
            player = Player(scene.current_state['life'], 1, 1, 'swing your torch wildly', 'torch')
        elif scene.have('knife') and weapon == '4':
            player = Player(scene.current_state['life'], 4, 8, 'Stab', 'knife')
        else:
            print('That was not an option... fists it is...')
            player = Player(scene.current_state['life'], 2, 5, 'swing your fists', 'fists')
        maze_attack = Attacking(monster, player)
        player_dead, monster_dead = maze_attack.fighting()
        if player_dead:
            scene.dead = True
        if monster_dead:
            print('You have slain the monster, well done! Lets hope thats the last of them...')
        scene.current_state['life'] = player.life
        return scene

    def _fight_in_maze(self, scene):
        import random
        random.seed()
        if random.randint(1, 100) > 90:
            random.seed()
            monster_type = random.randint(1,100)
            if monster_type < 8:
                monster = Snake(2, 'Viper', 'fangs', 'strikes', 8, 5)
            else:
                monster = Bat(4, 'Giant Bat', 'fangs', 'swoops', 2, 4)
            scene = self._do_the_fight(monster, scene)
        return scene

    def apply_action(self, command):
        return self._fight_in_maze(self)

class FourWay(MazeScene):
    def describe(self):
        print ('You come to a 4 way junction (you are the "#")')
        print ("")
        print('_| |_')
        print('_ # _')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"u" : Go up')
        print ('"r" : go right')
        print ('"l" : go left')
        print ('"d" : go down')

class TUp(MazeScene):
    def describe(self):
        print ('You come to a T junction (you are the "#")')
        print ("")
        print('_| |_')
        print('  # ')
        print('-----')
        print ()
        print ('You can: ')
        print ('"r" : go right')
        print ('"l" : go left')
        print ('"u" : go up')

class TDown(MazeScene):
    def describe(self):
        print ('You come to a T junction (you are the "#")')
        print ("")
        print('_____')
        print('_ # _')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"r" : go right')
        print ('"l" : go left')
        print ('"d" : go down')

class TLeft(MazeScene):
    def describe(self):
        print ('You come to an exit on the left and it continues straight on (you are the "#")')
        print ("")
        print('_| | ')
        print('_ #| ')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"u" : go up')
        print ('"l" : go left')
        print ('"d" : go down')

class TRight(MazeScene):
    def describe(self):
        print ('You come to an exit on the right and it continues straight on (you are the "#")')
        print ("")
        print(' | |_ ')
        print(' |# _ ')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"u" : go up')
        print ('"r" : go right')
        print ('"d" : go down')

class LeftBend(MazeScene):
    def describe(self):
        print ('You come to an exit on the left (you are the "#")')
        print ("")
        print('___ ')
        print('_ #|')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"l" : go left')
        print ('"d" : go down')

class LeftBendBottom(MazeScene):
    def describe(self):
        print ('You come to an exit on the left (you are the "#")')
        print ("")
        print('_| | ')
        print('  #|')
        print('---')
        print ()
        print ('You can: ')
        print ('"l" : go left')
        print ('"u" : go up')

class RightBendBottom(MazeScene):
    def describe(self):
        print ('You come to an exit on the right (you are the "#")')
        print ("")
        print(' | |_ ')
        print(' |# ')
        print('  ---')
        print ()
        print ('You can: ')
        print ('"r" : go right')
        print ('"u" : go up')

class RightBend(MazeScene):
    def describe(self):
        print ('You come to an exit on the right (you are the "#")')
        print ("")
        print('  ___ ')
        print(' |# _')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"r" : go right')
        print ('"d" : go down')

class Passage(MazeScene):
    def describe(self):
        print ('You continue in the passage (you are the "#")')
        print ("")
        print(' | | ')
        print(' |#|')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"u" : go up')
        print ('"d" : go down')

class FlatPassage(MazeScene):
    def describe(self):
        print ('You continue in the passage (you are the "#")')
        print ("")
        print(' _____ ')
        print('   *   ')
        print(' ----- ')
        print ()
        print ('You can: ')
        print ('"l" : go left')
        print ('"r" : go right')

class DeadEndTop(MazeScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  ___ ')
        print(' | # |')
        print(' |   | ')
        print ()
        print ('You can: ')
        print ('"d" : go down')

class DeadEndLeft(MazeScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  ____ ')
        print(' | # ')
        print('  ---- ')
        print ()
        print ('You can: ')
        print ('"r" : go right')

class DeadEndLeftTreasure(MazeScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  ____ ')
        print(' |+# ')
        print('  ---- ')
        print ()
        print ('You can: ')
        print ('"r" : go right')

class DeadEndRight(MazeScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  ____ ')
        print('    # |')
        print('  ---- ')
        print ()
        print ('You can: ')
        print ('"l" : go left')

class DeadEndBottom(MazeScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  |   |')
        print('  | # |')
        print('   --- ')
        print ()
        print ('You can: ')
        print ('"u" : go up')

class Thirty(DeadEndBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = DeadEndBottom.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = TwentyNine(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentyNine(RightBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = RightBend.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = TwentyOne(self.current_state)
        elif command == 'd':
            scene = Thirty(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentyEightKnife(DeadEndLeftTreasure):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = DeadEndLeftTreasure.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = TwentySeven(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentySeven(TUp):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            if not self.game_status('have_knife'):
                print ('You notice something glinting on the floor... you stoop to pick it up. You find... (press enter)')
                print ('A Knife!')
                print ("                                                       ___			")
                print ("                                                      |_  |										")
                print ("                                                        | |										")
                print ("__                      ____                            | |										")
                print ("\ ````''''----....____.'\   ````''''--------------------| |--.               _____      .-.		")
                print (" :.                      `-._                           | |   `''-----''''```     ``''|`: :|	")
                print ("  '::.                       `'--.._____________________| |                           | : :|	")
                print ("    '::..       ----....._______________________________| |                           | : :|	")
                print ("      `'-::...__________________________________________| |   .-''-..-'`-..-'`-..-''-.  : :|	")
                print ("           ```'''---------------------------------------| |--'                         `'-'		")
                print ("                                                        | |										")
                print ("                                                       _| |										")
                print ("                                                      |___| 									")
                scene.take('knife')
                self.inc_score(2, 'have_knife')
                self.set_game_status('have_knife', True)
            scene = TwentyEightKnife(self.current_state)
        elif command == 'r':
            scene = TwentyFive(self.current_state)
        elif command == 'u':
            scene = TwentySix(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentySix(RightBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = RightBend.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Seventeen(self.current_state)
        elif command == 'd':
            scene = TwentySeven(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentyFive(TUp):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = TUp.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = TwentySeven(self.current_state)
        elif command == 'r':
            scene = TwentyThree(self.current_state)
        elif command == 'u':
            scene = Seventeen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentyFour(DeadEndRight):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = DeadEndRight.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = TwentyThree(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentyThree(FourWay):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = FourWay.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Sixteen(self.current_state)
        elif command == 'd':
            scene = TwentyOne(self.current_state)
        elif command == 'l':
            scene = TwentyFive(self.current_state)
        elif command == 'r':
            scene = TwentyFour(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Eighteen(DeadEndTop):

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'd':
            scene = Seventeen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Exit(Passage):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'u':
            self.clear()
            print ('You come across a door - could this be the exit to the maze!!!')
            print ()
            print("|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..")
            print("`-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  ")
            print("   | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  ")
            print("_  |     |`-!._ | `.| |_______________||.''|  _!.;'   |     _|..")
            print("|``'..__ |    |`';.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    ")
            print("|      |``--..|_ | `;!| |MMoMMMMoMMM| |.'j   |_..!-'|     |     ")
            print("|      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     ")
            print("|______|____!.,.!,.!,!| |MMMo * loMM| |,!,.!.,.!..__|_____|_____")
            print("   |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  ")
            print("   |     |    |..!-;'i| |MPYMoMMMMoM| | |`-..|   |    |      |  ")
            print("   |    _!.-j'  | _!,'|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  ")
            print("  _!.-'|    | _.'|  !;| |MbdMMoMMMMM| |`.| `-._|    |``-.._  |  ")
            print("i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``'..")
            print("|      |.|    |.|  !| | |MoMMMMoMMMM| ||`. |`!   | `'.    |     ")
            print("|  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     ")
            print("!''|     !.'|  .'| .'|[ ]MMMMMMMMMMM[ ] \|  `. | `._  |   `-._  ")
            print("   |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-")
            print("   |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  ")
            print("  .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  ")
            print(".'     !'|   .' | /                       \|  `  |  `.    |`.|  ")
            print ()
            print ("You walk through the door and...")
            print ('press Enter...')
            input()
            self.set_game_status('out_maze', True)
            from scenes.Stage1Scenes import LeavePlane
            scene = LeavePlane(self.current_state)
        elif command == 'd':
            scene = Seventeen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class LockedExit(Passage):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'u':
            self.clear()
            print ('You come across a door - could this be the exit to the maze!!! You push and push but the door is locked!')
            print ()
            print("|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..")
            print("`-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  ")
            print("   | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  ")
            print("_  |     |`-!._ | `.| |_______________||.''|  _!.;'   |     _|..")
            print("|``'..__ |    |`';.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    ")
            print("|      |``--..|_ | `;!| |MMoMMMMoMMM| |.'j   |_..!-'|     |     ")
            print("|      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     ")
            print("|______|____!.,.!,.!,!| |MMMo * loMM| |,!,.!.,.!..__|_____|_____")
            print("   |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  ")
            print("   |     |    |..!-;'i| |MPYMoMMMMoM| | |`-..|   |    |      |  ")
            print("   |    _!.-j'  | _!,'|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  ")
            print("  _!.-'|    | _.'|  !;| |MbdMMoMMMMM| |`.| `-._|    |``-.._  |  ")
            print("i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``'..")
            print("|      |.|    |.|  !| | |MoMMMMoMMMM| ||`. |`!   | `'.    |     ")
            print("|  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     ")
            print("!''|     !.'|  .'| .'|[ ]MMMMMMMMMMM[ ] \|  `. | `._  |   `-._  ")
            print("   |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-")
            print("   |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  ")
            print("  .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  ")
            print(".'     !'|   .' | /                       \|  `  |  `.    |`.|  ")
            print ()
        elif scene.contains_key(command, ['go back', 'leave', 'turn around', 'walk back', 'retreat', 'd']):
            scene = Thirteen(self.current_state)
        elif self.contains_key(command, ['push', 'kick', 'shoot', 'stab', 'ram']):
            print ('The door doesnt budge')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Seventeen(TLeft):

    def _fight_minotaur(self):
        monster = Minotaur(100, 'Minotaur', 'Axe', 'swings', 15, 12)
        scene = self._do_the_fight(monster, self)
        return scene

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = TLeft.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = self._fight_minotaur()
            if scene.dead:
                return scene
            else:
                scene = Eighteen(self.current_state)
        elif command == 'l':
            scene = TwentySix(self.current_state)
        elif command == 'd':
            scene = TwentyFive(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Sixteen(TRight):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = TRight.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Fourteen(self.current_state)
        elif command == 'r':
            scene = Fifteen(self.current_state)
        elif command == 'd':
            scene = TwentyThree(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Fifteen(LeftBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = LeftBendBottom.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Thirteen(self.current_state)
        elif command == 'l':
            scene = Sixteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Fourteen(RightBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = RightBend.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Thirteen(self.current_state)
        elif command == 'd':
            scene = Sixteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Thirteen(FourWay):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = FourWay.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Fourteen(self.current_state)
        elif command == 'r':
            scene = Nine(self.current_state)
        elif command == 'd':
            scene = Fifteen(self.current_state)
        elif command == 'u':
            if scene.game_status('pulled_maze_lever'):
                scene = Exit(self.current_state)
            else:
                scene = LockedExit(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentyTwo(RightBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = RightBendBottom.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Eleven(self.current_state)
        elif command == 'u':
            scene = TwentyOne(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class TwentyOne(FourWay):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = FourWay.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'd':
            scene = TwentyTwo(self.current_state)
        elif command == 'r':
            scene = Twelve(self.current_state)
        elif command == 'l':
            scene = TwentyNine(self.current_state)
        elif command == 'u':
            scene = TwentyThree(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Twelve(LeftBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = LeftBend.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = TwentyOne(self.current_state)
        elif command == 'd':
            scene = Eleven(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Eleven(TUp):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = TUp.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = EnterMaze(self.current_state)
        elif command == 'l':
            scene = TwentyTwo(self.current_state)
        elif command == 'u':
            scene = Twelve(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Twenty(DeadEndRight):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = DeadEndRight.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Ten(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Ten(RightBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = RightBend.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Twenty(self.current_state)
        elif command == 'd':
            scene = Nine(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Nine(TUp):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = TUp.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Eight(self.current_state)
        elif command == 'l':
            scene = Thirteen(self.current_state)
        elif command == 'u':
            scene = Ten(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Eight(LeftBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = LeftBend.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Nine(self.current_state)
        elif command == 'd':
            scene = Five(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Seven(LeftBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = LeftBendBottom.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Three(self.current_state)
        elif command == 'u':
            scene = Six(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Six(LeftBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = LeftBend.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Five(self.current_state)
        elif command == 'd':
            scene = Seven(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Five(TRight):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = TRight.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Eight(self.current_state)
        elif command == 'r':
            scene = Six(self.current_state)
        elif command == 'd':
            scene = Three(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Nineteen(DeadEndTop):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = DeadEndTop.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'd':
            scene = Four(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Four(RightBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = RightBendBottom.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Three(self.current_state)
        elif command == 'u':
            scene = Nineteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Three(FourWay):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = FourWay.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Five(self.current_state)
        elif command == 'd':
            scene = Two(self.current_state)
        elif command == 'r':
            scene = Seven(self.current_state)
        elif command == 'l':
            scene = Four(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class Two(Passage):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = Passage.apply_action(self, command)
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Three(self.current_state)
        elif command == 'd':
            scene = One(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class One(LeftBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        scene = LeftBendBottom.apply_action(self, command)
        if scene.dead:
            return scene
        if scene.dead:
            return scene
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = EnterMaze(self.current_state)
        elif command == 'u':
            scene = Two(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class EnterMaze(BaseScene):

    def describe(self):
        print ('You come to a T junction (you are the "#")')
        print ("")
        print('_____')
        print('_ # _')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"r" : go right')
        print ('"l" : go left')
        print ('"d" : go down')

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = One(self.current_state)
        elif command == 'l':
            scene = Eleven(self.current_state)
        elif command == 'd':
            scene = StartMaze(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print ('Chin up, stay positive, you are sure the end is just around the corner.')
        else:
            print ('You cant do that')
        return scene

class StartMaze(BaseScene):

    def describe(self):
        print ('Yup... this could definitely be a maze')
        print ("")
        print('88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  ."|   |."|     |  _..88')
        print('88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  ."  |.;"   |   _.!-"|  88')
        print('88      | `-!._  |  `;!  ;.                  ,"| .-" |   _!.i"    |  88')
        print('88..__  |     |`-!._ | `.| |               |.""|  _!.;"   |     _|.. 88')
        print('88   |``"..__ |    |`";.| i|               | | _!-|   |   _|..-|"    88')
        print('88   |      |``--..|_ | `;!|               |."j   |_..!-"|     |     88')
        print('88   |      |    |   |`-,!_|               |. !-;"  |    |     |     88')
        print('88___|______|____!.,.!,.!,!|               |,!,.!.,.!..__|_____|_____88')
        print('88      |     |    |  |  | |               |  |   |   |    |      |  88')
        print('88      |     |    |..!-;"i|               | |`-..|   |    |      |  88')
        print('88      |    _!.-j"  | _!,"|               ||!._|  `i-!.._ |      |  88')
        print('88     _!.-"|    | _."|  !;|               |`.| `-._|    |``-.._  |  88')
        print('88..-i"     |  _.""|  !-| !|               |.|`-. | ``._ |     |``"..88')
        print('88   |      |.|    |.|  !| |               ||`. |`!   | `".    |     88')
        print('88   |  _.-"  |  ."  |." |/|               |! |`!  `,.|    |-._|     88')
        print('88  _!""|     !."|  ."| ."||               | \|  `. | `._  |   `-._  88')
        print('88-"    |   ."   |.|  |/| /                 \|`.  |`!    |.|      |`-88')
        print('88      |_."|   ." | ." |/                   \  \ |  `.  | `._    |  88')
        print('88     ."   | ."   |/|  /                     \ |`!   |`.|    `.  |  88')
        print ()
        print ('You notice writing on the wall:')
        print ()
        print ('THIS DEADLY MAZE, THROUGH TWISTS AND TURNS, CONTAINS AN EXIT FOR YOUR PLEASURE ')
        print ('IF YOU SURVIVE BEFORE YOU GET OUTSIDE, YOU MAY EVEN FIND SOME TREASURE!')

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif self.contains_key(command, ['enter', 'go in', 'walk in', 'go inside']):
            print ('You take a deep breath and walk into the maze...')
            scene = EnterMaze(self.current_state)
        elif self.contains_key(command, ['leave']):
            from scenes.Stage1Scenes import Cave, LeavePlane
            scene = Cave(self.current_state)
        elif command == 'hint':
            print ('The maze looks scary... but on the other hand are there any other choices?')
        else:
            print ('You cant do that')
        return scene