from scenes.BaseScene import BaseScene
import random

class Ogre(BaseScene):

    def describe(self):
        print ("Oi what are you doing here and what do you want!!!")
        print ("Yells a ferocious looking man who looks exactly like an Ogre (but is actually the Woodsman.)")
        print ("I heard a gunshot and came back to my house to see what was going on...")
        print("")
        print("           __,='`````'=/__						")
        print("          '//  (o) \(o) \ `'         _,-,       ")
        print("          //|     ,_)   (`\      ,-'`_,-\       ")
        print("        ,-~~~\  `'==='  /-,      \==```` \__    ")
        print("       /        `----'     `\     \       \/    ")
        print("    ,-`                  ,   \  ,.-\       \    ")
        print("   /      ,               \,-`\`_,-`\_,..--'\   ")
        print("  ,`    ,/,              ,>,   )     \--`````\  ")
        print("  (      `\`---'`  `-,-'`_,<   \      \_,.--'`	")
        print("   `.      `--. _,-'`_,-`  |    \				")
        print("    [`-.___   <`_,-'`------(    /				")
        print("    (`` _,-\   \ --`````````|--`				")
        print("     >-`_,-`\,-` ,          |					")
        print("   <`_,'     ,  /\          /					")
        print("    `  \/\,-/ `/  \/`\_/V\_/					")
        print("       (  ._. )    ( .__. )						")
        print("       |      |    |      |						")
        print("        \,---_|    |_---./						")
        print("           __,='`````'=/__        				")
        print("        ooOO(_)    (_)OOoo 						")
        print()
        if self.have('gun'):
            print("And YOU HAVE MY GUN!!! You thief... With a mighty swing of his Axe the \
                   Ogre, I means woodsman chops your head off")
            self.dead = True
        else:
            print ("What are you doing here?")
            print ("You say:")
            print ("-------------------------------------------")
            print ("1: None of your business")
            print("2: Just out camping")
            print("3: Come to bring you a basket of food grandma")
            print("4: I heard the gun shot too and came to help")

    def adjust_humour(self, amount):
        humour = self.current_state['game_status'].get('giant_humour', False)
        if humour or humour == 0:
            humour = humour + amount
        else:
            humour = amount

    def calc_humour(self):
        if random.randint(1, 2) < 2:
            print ("BBBBBUUUUHAHAHAHAAHAHA that is hilarious! Go on tell me another!")
            self.adjust_humour(1)
        else:
            joke_result = random.randint(1, 3)
            if joke_result == 1:
                print ("That's a terrible joke!")
            elif joke_result == 2:
                print ("I dont get it?")
            else:
                print ("My goat outside could tell better jokes than that!")
            self.adjust_humour(-1)

    def tell_joke(self):
        print ("Think you are funny hey! Well funny man, tell me a joke...")
        joke = input()
        if 'knock' in joke:
            print ("whos there?")
            ans = input()
            print (ans + " who")
            input()
        elif 'how' in joke or 'what' in joke or 'where' in joke:
            print ("I don't know, tell me?")
            ans3 = input()
        self.calc_humour()
        if self.current_state['game_status'].get('giant_humour', 0) == 3:
            return HappyOgre(self.current_state)
        else:
            return self

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == '1':
            print ("Why you rude little tike!")

        elif command == '2':
            scene = self.tell_joke()
        elif command == '3':
            scene = self.tell_joke()
        elif command == '4':
            scene = self.tell_joke()
        elif command == 'hint':
            print('I would try to get on his good side')
        else:
            print('You cant do that')
        return scene


