from scenes.BaseScene import BaseScene
import random

class Ogre(BaseScene):

    def print_options(self):
            print ("What are you doing here?")
            print ("You say:")
            print ("-------------------------------------------")
            print ("1: None of your business")
            print ("2: Just out camping")
            print ("3: Come to bring you a basket of food grandma")
            print ("4: I heard the gun shot too and came to help")

    def describe(self):
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
            print("And YOU HAVE MY GUN!!! You thief... With a mighty swing of his Axe the Ogre, I mean woodsman chops your head off")
            self.dead = True
        else:
            self.print_options()

    def adjust_humour(self, amount):
        humour = self.current_state['game_status'].get('giant_humour', 0)
        if humour < 0:
            humour = 0
        humour = humour + amount
        self.set_game_status('giant_humour', humour)

    def calc_humour(self):
        random.seed()
        if random.randint(1, 5) < 4:
            print ("BBBBBUUUUHAHAHAHAAHAHA that is hilarious! Go on tell me another!")
            self.adjust_humour(1)
        else:
            random.seed()
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
        if ans.upper() == 'Y':
            print ("Ok here is another joke... you say:")
            self.tell_joke()
        else:
            if not self.current_state['game_status'].get('giant_humour', 0) >= 3:
                self.print_options()

    def tell_joke(self):
        joke = input()
        if 'knock' in joke:
            print ("whos there?")
            ans = input()
            print (ans + " who")
            input()
        elif 'how' in joke or 'what' in joke or 'where' in joke or 'why' in joke:
            print ("I don't know, tell me?")
            ans3 = input()
        self.calc_humour()
        if self.current_state['game_status'].get('giant_humour', 0) >= 3:
            self.inc_score(5, 'jokes')
            return HappyOgre(self.current_state)
        return self

    def inc_ogre_anger(self):
        ogre_anger = self.game_status('ogre_anger')
        if ogre_anger:
            ogre_anger = ogre_anger + 1
        else:
            ogre_anger = 1
        self.set_game_status('ogre_anger', ogre_anger)
        if ogre_anger > 4:
            print ("You have insulted the ogre for the last time! He reaches over and rips off your head. Maybe next time dont irritate him so much.")
            self.dead = True

    def hurl_insult(self):
        print ("")
        random.seed
        random_selection = random.randint(1, 8)
        if random_selection == 1:
            print ("ArrrGGGHHH what a rude little person you are!")
        elif random_selection == 2:
            print ("You liar, lousy little maggot!")
        elif random_selection == 3:
            print ("You liar, you flea bitten piece of tomato sauce!")
        elif random_selection == 4:
            print ("You liar, you flame grilled chicken burger!")
        elif random_selection == 5:
            print ("You liar, you home grown fungus!")
        elif random_selection == 6:
            print ("You liar, you lemon eating, toothpaste using, tree smelling rascal!")
        elif random_selection == 7:
            print ("You liar, you ungrateful tooth mouse!")
        else:
            print ("You liar, you ... you .... something!!!")
        self.inc_ogre_anger()
        if self.dead:
            return
        print("")
        self.print_options()

    def apply_action(self, command):
        scene = self
        scene.same_scene = True
        if self.have('gun'):
            return scene
        if command == 'look':
            self.describe()
        elif command == '1':
            self.hurl_insult()
        elif command == '2':
            self.hurl_insult()
        elif command == '3':
            print("Think you are funny hey! Well funny man, tell me a joke...")
            scene = self.tell_joke()
        elif command == '4':
            self.hurl_insult()
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
        elif command == 'radio' or command == 'offer radio' or command == 'trade radio':
            print ("Oh I like that yes... let me take a little look.")
            print ('(you hand over the radio to the Woodsman...)')
            print ('Ah yes, very nice, a model T1000, excellent workmanship, quality craftmanship... max range of 1000m... very nice very nice...')
            if not self.game_status('radio_has_batteries'):
                print ('But there are NO BATTERIES!!! What kind of a fool do you take me for! And with a thunderous punch, the woodsman punches you through the window and you die!')
                print ('press enter...')
                input()
                self.dead = True
            else:
                print ('Lovely, lovely, I will trade! Thank you!')
                print ('The woodsman hands over a map and compass and you leave')
                self.inc_score(3, 'made_trade')
                self.take('map')
                self.take('compass')
                print ('press enter...')
                input()
                from scenes.Stage1Scenes import Forest
                scene = Forest(self.current_state)
        else:
            print('Nah, not interested in that thank you')
        return scene
