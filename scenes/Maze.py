from scenes.BaseScene import BaseScene
from scenes.Stage1Scenes import Cave

class EnterMaze(BaseScene):

    def describe(self):
        print ('You come to a T junction (you are the "#")')
        print ("")
        print('_____')
        print('_ # _')
        print(' | | ')
        print ()
        print ('You can: ')
        print ('"r" : Turn to the right and walk forward')
        print ('"l" : Turn to the left and walk forward')
        print ('"b" : Turn around and walk forward')

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'r':
            scene = FirstRight(self.current_state)
        elif self.contains_key(command, ['leave']):
            print ('You cant leave, you are in a maze, you must keep going...')
        elif command == 'hint':
            print ('Always build with triangles!')
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
            scene = Cave(self.current_state)
        elif command == 'hint':
            print ('The maze looks scary... but on the other hand are there any other choices?')
        else:
            print ('You cant do that')
        return scene