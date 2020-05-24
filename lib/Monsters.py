import random

class Attacking():
    def __init__(self, monster, player):
        self.monster = monster
        self.player = player

    def fighting(self):
        while self.monster.is_alive and self.player.is_alive:
            self.player.wound(self.monster.fight())
            if not self.player.is_alive:
                return True, False
            self.monster.receive_damage(self.player)
            if not self.monster.is_alive:
                return False, True

class Player():
    def __init__(self, life, weapon_power, weapon_accuracy, weapon_adjective):
        self.life = life
        self.weapon_power = weapon_power
        self.weapon_accuracy = weapon_accuracy
        self.weapon_adjective = weapon_adjective

    def wound(self, damage):
        self.life +- damage

class Monster():
    def __init__(self, life, name, attack, power, accuracy):
        self.life = life
        self.name = name
        self.attack = attack
        self.power = power
        self.accuracy = accuracy

    def is_alive(self):
        self.life > 0

    def fight(self):
        damage = 0
        print ('The %s and hits you with its %s' % (self.name, self.attack))
        random.seed()
        attack_success = random(1, 10) + self.accuracy > 10
        if attack_success:
            random.seed()
            damage = random(1, self.power)
            print ('The % HITs you for %d damage!' % self.name)
        else:
            print ('The %s MISSES you!')
        print ('Press enter...')
        input ()
        return damage

    def receive_damage(self, players_weapon, players_power, players_accuracy, players_weapon_adjective):
        print ('You %s and attack the %s with your %s' % (players_weapon_adjective, self.name, players_weapon))
        random.seed()
        attack_success = random(1, 10) + players_accuracy > 10
        if attack_success:
            random.seed()
            damage = random(1, players_power)
            print ('You HIT the %s for %d damage!' % (self.name, damage))
            self.life -= damage
        else:
            print ('You MISS the %s' % self.name)
        print ('Press enter...')
        input ()