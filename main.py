import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = "\nUse only A, B, or C\n"

stop = time.sleep

# health = 100
# attack = 0
# weapon = "empty"


def status(health, attack, weapon):
    print(f"\n===========\nHERO STATUS\n==========="
          f"\n♥ {health}"
          f"\n⚔ {attack}"
          f"\nWeapon is {weapon}"
          f"\n===========\n")


def intro():
    # name
    name = input("What is your name, adventurer?\n")
    print(f"Greetings, {name}. Let us go on a quest!"
          "\nYou find yourself on the edge of a Dark Forest!")
    stop(1)
    # status
    status(100, 0, "empty")

    # first step
    stop(1)
    it = open('texts/intro', 'r')
    text = it.read()
    print(text)

    # first choice
    stop(2)
    ia = open('texts/intro_answer', 'r')
    text = ia.read()
    print(text)

    choice = input("You choice >>> ")
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print("\nWell, that was quick.\n\n")
        option_death()
    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_death():
    status(0, 0, "empty")

    death = open('texts/death', 'r')
    text = death.read()
    print(text)


def option_rock():
    rt = open('texts/rock', 'r')
    text = rt.read()
    print(text)
    stop(1)

    rt = open('texts/rock_answer', 'r')
    text = rt.read()
    print(text)
    stop(1)
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another rock, as if the first "
              "rock thrown did much damage. The rock flew well over the "
              "orcs head. You missed.")
        option_death()
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_run():
    print("step option_run")


def option_cave():
    print("step option_cave")


intro()
