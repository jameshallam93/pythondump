import random
import time
import pickle
# fight simulator
#the og dictionary of all monsters, created both in code and by functions - a copy of this is made when each game begins to maintain original stats (i.e. health)

monsters1 = []
# a game with different monsters with different abilities that you can fight in a simulator to see who wins
#auto fills with every instantiation creation
#used for strength/weakness function
types = {"Earth": "Fire", "Fly" : "Earth" , "Fire": "Fly"}


#class definition for all monsters  
class monster:
    def __init__(self, name, type, dps, dodge, hp, speed):
        self.name = name
        self.type = type
        self.dps = dps
        self.dodge = dodge
        self.hp = hp
        self.speed = speed


        monsters1.append(self)
#returns False if attack is dodged (don't judge me)
    def dodge_success(self):
        chance = 100 - self.dodge
        interger = random.randrange(1,100)
        if interger <= chance:
            return True
        else:
            return False
#checks to see if either monster has lost all health - returns other monster's name attribute as victor.      
    def victory(monster1, monster2):
            if monster1.hp <= 0:
                return monster1.name
            elif monster2.hp <= 0:
                return monster2.name
            else:
                return 0

        
#runs monsters through turn based battle, printing health and misses as it goes

    def battle_seq(self, monster2):
        #for while loop below
        victor = 0
        speed_count_self = 0
        speed_count_opponent = 0
        #checks to see if either monster gets super effective bonus
        is_super_self = is_super(self, monster2)
        is_super_monster = is_super(monster2, self)
        if is_super_self == True:
            print("Your monster is super effective against the enemy!")
        elif is_super_monster == True:
            print("%s is super effective against your monster!"%(monster2.name))
        #while loop is broken when victory function returns either monsters name attribute, rewriting victor variable.
                  #victory function is run after every occurence of a monster taking damage.
        while victor == 0:

            victor = victory(self, monster2)
            #calling on function to establish if either monster will dodge this round
            #function generates random no. btn 0-100, and monster dodges if the number generated is the same as or lower than the monsters dodge chance
            
            while speed_count_self < 30 and speed_count_opponent < 30:
                speed_count_self += self.speed
                speed_count_opponent += monster2.speed
                
            if speed_count_self >= 30:
                
                hit_success = self.dodge_success()
                if hit_success:
                    #super_eff returns 1 if monster has no advantage, and a floating point between 1 and 3 if it does. is_super variables are truth values
                    damage = super_eff(is_super_self) * self.dps
                    print("%s hits %s for %s damage!"%(self.name, monster2.name, damage))
                    time.sleep(1)
                    #updating instantiation attributes
                    monster2.hp = monster2.hp - damage
                    print("%s hp is %s"%(monster2.name, monster2.hp))
                    time.sleep(1)
                    speed_count_self = 0
                    victor = victory(self, monster2)
                    #checking to see if monster 2 has run out of health and breaking loop here if it has, to avoid running through the rest of the loop.
                    if victor != 0:
                        break
                else:
                    print("%s has missed!"%(self.name))
                    speed_count_self = 0
                    time.sleep(1)
                    
            elif speed_count_opponent >= 30:
                
                enemy_hit_success = monster2.dodge_success()
                if enemy_hit_success:
                    damage2 = super_eff(is_super_monster) * monster2.dps 
                    print("%s hits %s for %s damage!"%(monster2.name, self.name, damage2))
                    time.sleep(1)
                    self.hp = self.hp - damage2
                    print("%s hp is %s"%(self.name, self.hp))
                    time.sleep(1)
                    speed_count_opponent = 0
                    victor = victory(self, monster2)
                else:
                    print("%s has missed"%(monster2.name))
                time.sleep(1)
                speed_count_opponent = 0
        print(victor, " has won!")
    



"""
def battle_seq(monster1, monster2):
    while monster1.hp >0 and monster2.hp > 0:
        monster1_hit = monster1.dodge_success
        monster2_hit = monster2.dodge_success
        print(monster2_hit)
        if monster2_hit == False:
            monster2.hp = monster2.hp - monster1.dps
            print("Monster 2's hp is %s"%monster2.hp)
        if monster2_hit == False:
            monster1.hp = monster1.hp - monster2.dps
            print("Monster 1's hp is %s"%monster1.hp)
        """


#class instantiations, the different monsters

charmander = monster("Charmander", "Fire", 5, 10, 15, 8)

rat= monster("Rat", "Earth", 3, 30, 20, 6)

owl = monster("Owl", "Fly", 4, 35, 15, 3)


#battle_seq(rat, owl)






def choose_monster():
    print("These are the monsters available to battle:")
    for monster in monsters:
        print(monster.name)
    global user_monster
    user_monster = 1
    while user_monster == 1:
        user_choice = input("Choose your monster")       
        for monster in monsters:
            if monster.name == user_choice:
                user_monster = monster
                print("Monster chosen")
                break
        break
    
        print("Monster not found, please try again")
        continue
            
                

def choose_opponent():
    global opponent
    opponent = 1
    while opponent ==1:
        try:
            opponent_choice = input("Choose your opponent")
            for monster in monsters:
                if monster.name == opponent_choice:
                    opponent = monster
                    print("Opponent chosen")
                    break
            break
            print("Monster not found, please try again")
            continue
        except AttributeError:
            print("Sorry, that monster is not recognised, please try again")
            continue

        
def super_eff(truth):
    if truth:
        return int(random.randrange(10,30) / 10)
    if truth == False:
        return 1
    
def victory(monster1, monster2):
    if monster1.hp <= 0:
        return monster2.name
    elif monster2.hp <= 0:
        return monster1.name
    else:
        return 0
    
def is_super(monster1, monster2):
    type_key1 = monster1.type
    type_key2 = monster2.type
    if types[type_key1] == type_key2:
        return True
    else:
        return False            

def create_monster():
    created = False
    while created == False:
        print("You have 25 points to spend on HP, DPS, Speed and Dodge. You can spend a max of ten points on one skill")
        hp_stat = int(input("How many points do you want to spend on HP?"))
        dps_stat = int(input("How many on DPS?"))
        speed_stat = int(input("How many on speed?"))
        dodge_stat = int(input("And how many on dodge?"))
        type_stat = input("And what is it's type? Fire, Earth or Fly?")
        name_stat = input("And what do you want to call your monster?")    
        if hp_stat + dps_stat + speed_stat + dodge_stat <=25 and hp_stat and dps_stat and speed_stat and dodge_stat <=10:
            global new_monster
            new_monster = monster(name_stat, type_stat, dps_stat, (dodge_stat*5), (hp_stat*3), speed_stat)
            pickle.dump(monsters1, open("monsters.dat", "wb"))
            print(new_monster.name, new_monster.dodge, new_monster.hp)
            created = True
            break
        
        
        elif hp_stat + dps_stat + speed_stat + dodge_stat >25:
            print("You've spent too many points, try again")
            continue
        elif hp_stat or dps_stat or speed_stat or dodge_stat <=10:
            print("You've spent too many points on one skill, try again")
        else:
            print("nokay")
        
monsters1 = []
charmander = monster("Charmander", "Fire", 5, 10, 15, 8)

rat= monster("Rat", "Earth", 3, 30, 20, 6)

owl = monster("Owl", "Fly", 4, 35, 15, 5)

pickle.dump(monsters1, open("monsters.dat", "wb"))
    
playing = True
creation = True
while playing:
    

    while creation:
        proceed = input("Do you want to create a new monster?")
        if proceed == "Yes":
            create_monster()
            continue
        if proceed == "No":
            creation == False
            break
    monsters = pickle.load("monsters.dat")
    choose_monster()
    choose_opponent()

    print(user_monster.name, " VS. ", opponent.name)

    user_monster.battle_seq(opponent)
    leave = input("Do you want to play again? Yes/No")
    if leave == "Yes":
        continue
    elif leave == "No":
        playing = False
    else:
        print("Sorry, please type Yes or No")
        continue

