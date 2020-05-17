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
        print ("Tell the woodsman another joke? Type: 'Y' or 'N'?")
        ans = input()
        if ans.upper == 'Y':
            self.tell_joke()

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
            self.inc_score(5, 'jokes')
            return HappyOgre(self.current_state)

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

class HappyOgre(BaseScene):

    def describe(self):
        print ("Ah you are a funny one, I have grown to like you! Say... I like trading, and I have this lovely map and compass.")
        print ("Is there anything you would like to trade for them?")

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if command == 'look':
            self.describe()
        elif command == 'radio':
            print ("Oh I like that yes... let me take a little look.")
            print ('(you have over the radio to the Woodsman...)')
            print ('Ah yes, very nice, a model T1000, excellent workmanship, quality craftmanship... max range of 1000m... very nice very nice...')
            if not self.game_status('radio_has_batteries'):
                print ('But there are NO BATTERIES!!! What kind of a fool do you take me for! And with a thunderous punch, the woodsman punches you through the winodow and you die!')
                self.dead = True
            else:
                print ('Lovely, lovely, I will trade! Thank you!')
                print ('The woodsman handover a map and compass and you leave')
                self.inc_score(3, 'made_trade')
                self.take('map')
                self.take('compass')
                from scenes.Stage1Scenes import Forest
                scene = Forest(self.current_state)
        else:
            print('Nah, not interested in that thank you')
        return scene
