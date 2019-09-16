import random
import time


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]


def hero_status(hero_health, hero_attack, hero_weapon):
    print("\n===========\nHERO STATUS\n==========="
          f"\n♥ {hero_health}"
          f"\n⚔ {hero_attack}"
          f"\nWeapon is {hero_weapon}"
          "\n===========\n")


def enemy_status(e_health, e_attack, e_weapon):
    print("\n===========\nENEMY STATUS\n==========="
          f"\n♥ {e_health}"
          f"\n⚔ {e_attack}"
          f"\nWeapon is {e_weapon}"
          "\n===========\n")

def fight():
    print("You fight with Ork! He look angry:\n")
    time.sleep(1)

    e_health = 60
    e_attack = 25
    e_weapon = "Battle axe"
    enemy_status(e_health, e_attack, e_weapon)

    print("You feel good:\n")
    time.sleep(1)
    hero_health = 100
    hero_attack = 30
    hero_weapon = "Long sword"
    hero_status(hero_health, hero_attack, hero_weapon)

    time.sleep(1)
    print(f"\nA. Hit with {hero_weapon}"
          "\nB. Run\n")

    time.sleep(1)
    choice = input(">>> ")
    if choice in answer_A:
        hit = random.uniform(1 - hero_attack, 100)
        if hit < 60:
            print("You hit the Orc")
            e_health = e_health - hero_attack
            e_attack = 25
            e_weapon = "Battle axe"
            enemy_status(e_health, e_attack, e_weapon)
            print(f"\nA. Hit with {hero_weapon}"
                  "\nB. Run\n")
            choice = input(">>> ")
            if choice in answer_A:
                hit = random.uniform(1 - hero_attack, 100)
                if hit < 60:
                    print("You kill the Orc")
                    e_health = e_health - hero_attack
                    e_attack = 25
                    e_weapon = "Battle axe"
                    enemy_status(e_health, e_attack, e_weapon)
                else:
                    print("Miss, Orc truing hit you")
                    hit = random.uniform(1 - e_attack, 100)
                    if hit < 40:
                        print("Orc hit you")
                        hero_health = hero_health - e_attack
                        hero_attack = 30
                        hero_weapon = "Long sword"
                        hero_status(hero_health, hero_attack, hero_weapon)
                    else:
                        print("Ork missing, you turn!")
            elif choice in answer_B:
                print("death")
        else:
            print("Miss, Orc truing hit you")
            hit = random.uniform(1 - e_attack, 100)
            if hit < 40:
                print("Orc hit you")
                hero_health = hero_health - e_attack
                hero_attack = 30
                hero_weapon = "Long sword"
                hero_status(hero_health, hero_attack, hero_weapon)
            else:
                print("Ork missing, you turn!")
    elif choice in answer_B:
        print("death")
    else:
        fight()


fight()
