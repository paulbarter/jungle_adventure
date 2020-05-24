import random

class Attacking():
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def fighting(self):
        while self.monster.is_alive() and self.player.is_alive():
            self.player.wound(self.monster.fight())
            if not self.player.is_alive():
                return True, False
            self.monster.receive_damage(self.player)
            if not self.monster.is_alive():
                return False, True

class Player():
    def __init__(self, life, weapon_power, weapon_accuracy, weapon_adjective, weapon):
        self.life = life
        self.weapon_power = weapon_power
        self.weapon_accuracy = weapon_accuracy
        self.weapon_adjective = weapon_adjective
        self.weapon = weapon

    def wound(self, damage):
        self.life -= damage
        if damage > 0:
            print ('You life is now: %d' % self.life)

    def is_alive(self):
        return self.life > 0

class Monster():
    def __init__(self, life, name, attack, attack_adjective, power, accuracy):
        self.life = life
        self.name = name
        self.attack = attack
        self.power = power
        self.accuracy = accuracy
        self.attack_adjective = attack_adjective

    def describe_monster(self):
        return

    def is_alive(self):
        return self.life > 0

    def fight(self):
        damage = 0
        print ('The %s %s and hits you with its %s' % (self.name, self.attack_adjective, self.attack))
        random.seed()
        attack_success = random.randint(1, 10) + self.accuracy > 10
        if attack_success:
            random.seed()
            damage = random.randint(1, self.power)
            print ('The %s HITs you for %d damage!' % (self.name, damage))
        else:
            print ('The %s MISSES you!' % self.name)
        print ('Press enter...')
        input ()
        return damage

    def receive_damage(self, player):
        players_weapon = player.weapon
        players_power = player.weapon_power
        players_accuracy = player.weapon_accuracy
        players_weapon_adjective = player.weapon_adjective
        print ('You %s and attack the %s with your %s' % (players_weapon_adjective, self.name, players_weapon))
        random.seed()
        attack_success = random.randint(1, 10) + players_accuracy > 10
        if attack_success:
            random.seed()
            damage = random.randint(1, players_power)
            print ('You HIT the %s for %d damage!' % (self.name, damage))
            self.life -= damage
        else:
            print ('You MISS the %s' % self.name)
        print ('Press enter...')
        input ()

class Bat(Monster):
    def describe_monster(self):
        print('A Giant Bat swoops in from no-where what will you fight it with?')
        print("  ._.                  _.____.	")
        print("     ) \.              /    .(	")
        print("     )  |            .'   .(	")
        print("     ). ).          .'  .(		")
        print("       ) |.        .'  (		")
        print("       ). ;      ./  .(			")
        print("        ) |      )  (			")
        print("        ).;      :.(			")
        print("         )|    .|.;				")
        print("         .^--^./ (.				")
        print("         ;0..0;   \				")
        print("          'vv'_.:_.;     		")
        print("               m  M				")

class Snake(Monster):
    def describe_monster(self):
        print('A snake strikes from the shadows! What will you fight it with?')
        print("                         __				")
        print("           ---_ ...... _/_ -			")
        print("          /  .      ./ .'*\ \			")
        print("          : '         /__-'   \.		")
        print("         /                      )		")
        print("       _/                  >   .'		")
        print("     /   .   .       _.-' /  .'			")
        print("     \           __/'     /.'/|			")
        print("       \ '--  .-' /     //' |\|			")
        print("        \|  \ | /     //_ _ |/|			")
        print("         `.  \:     //|_ _ _|\|			")
        print("         | \/.    //  | _ _ |/| 		")
        print("          \_ | \/ /    \ _ _ \\\		")
        print("              \__/      \ _ _ \|\		")

class Minotaur(Monster):
    def describe_monster(self):
        print('A MINOTAUR storms into view!!! What will you fight it with?')
        print("                   (    )			")
        print("                  ((((()))			")
        print("                  |o\ /o)|			")
        print("                  ( (  _')			")
        print("                   (._.  /\__		")
        print("                  ,\___,/ '  ')		")
        print("    '.,_,,       (  .- .   .    )	")
        print("     \   \\     ( '        )(    )	")
        print("      \   \\    \.  _.__ ____( .  |	")
        print("       \  /\\   .(   .'  /\  '.  )	")
        print("        \(  \\.-' ( /    \/    \)	")
        print("         '  ()) _'.-|/\/\/\/\/\|		")
        print("             '\\ .( |\/\/\/\/\/|		")
        print("               '((  \    /\    /		")
        print("               ((((  '.__\/__.')		")
        print("                ((,) /   ((()   )	")
        print("                 '..-,  (()('   /	")
        print("                  _//.   ((() .'		")
        print("          _____ //,/' ___ ((( ', ___ ")
        print("                           ((  )		")
        print("                            / /		")
        print("                          _/,/'		")
        print("                        /,/,'		")