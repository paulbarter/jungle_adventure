from scenes.BaseScene import BaseScene
try:
    from scenes.Stage1Scenes import Cave, LeavePlane
except Exception as err:
    h = 3

class FourWay(BaseScene):
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

class TUp(BaseScene):
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

class TDown(BaseScene):
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

class TLeft(BaseScene):
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

class TRight(BaseScene):
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

class LeftBend(BaseScene):
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

class LeftBendBottom(BaseScene):
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

class RightBendBottom(BaseScene):
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

class RightBend(BaseScene):
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

class Passage(BaseScene):
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

class FlatPassage(BaseScene):
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

class DeadEndTop(BaseScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  ___ ')
        print(' | # |')
        print(' |   | ')
        print ()
        print ('You can: ')
        print ('"d" : go down')

class DeadEndLeft(BaseScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  ____ ')
        print(' | # ')
        print('  ---- ')
        print ()
        print ('You can: ')
        print ('"r" : go right')

class DeadEndRight(BaseScene):
    def describe(self):
        print ('You reach a dead end (you are the "#")')
        print ("")
        print('  ____ ')
        print('    # |')
        print('  ---- ')
        print ()
        print ('You can: ')
        print ('"l" : go left')

class Eighteen(Passage):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'u':
            self.set_game_status('out_maze', True)
            from scenes.Stage1Scenes import LeavePlane
            scene = LeavePlane(self.current_state)
        elif command == 'd':
            scene = Seventeen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Seventeen(RightBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Eighteen(self.current_state)
        elif command == 'r':
            scene = Sixteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Sixteen(FlatPassage):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Seventeen(self.current_state)
        elif command == 'r':
            scene = Fifteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Fifteen(LeftBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Thirteen(self.current_state)
        elif command == 'l':
            scene = Sixteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Fourteen(DeadEndLeft):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Thirteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Thirteen(TDown):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Fourteen(self.current_state)
        elif command == 'r':
            scene = Nine(self.current_state)
        elif command == 'd':
            scene = Fifteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class TwentyTwo(RightBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Eleven(self.current_state)
        elif command == 'u':
            scene = TwentyOne(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class TwentyOne(RightBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'd':
            scene = TwentyTwo(self.current_state)
        elif command == 'r':
            scene = Twelve(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Twelve(LeftBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = TwentyOne(self.current_state)
        elif command == 'd':
            scene = Eleven(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Eleven(TUp):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
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
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Twenty(DeadEndRight):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Ten(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Ten(RightBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Twenty(self.current_state)
        elif command == 'd':
            scene = Nine(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Nine(TUp):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
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
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Eight(LeftBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Nine(self.current_state)
        elif command == 'd':
            scene = Five(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Seven(LeftBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Three(self.current_state)
        elif command == 'u':
            scene = Six(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Six(LeftBend):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = Five(self.current_state)
        elif command == 'd':
            scene = Seven(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Five(TRight):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
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
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Nineteen(DeadEndTop):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'd':
            scene = Four(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Four(RightBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = Three(self.current_state)
        elif command == 'u':
            scene = Nineteen(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Three(FourWay):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
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
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class Two(Passage):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'u':
            scene = Three(self.current_state)
        elif command == 'd':
            scene = One(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
        else:
            print ('You cant do that')
        return scene

class One(LeftBendBottom):
    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'l':
            scene = EnterMaze(self.current_state)
        elif command == 'u':
            scene = Two(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                    situation. Ah yes... Always build with triangles!')
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
            print ('Now what was it your pappy always used to say... surely his advice will come in handy one day in a dangerous \
                situation. Ah yes... Always build with triangles!')
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