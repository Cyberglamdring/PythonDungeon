import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = "\nUse only A, B, or C\n"

stop = time.sleep


def status():
    attack = 0
    health = 100
    weapon = "empty"
    print(f"\n===========\nHERO STATUS\n==========="
          f"\n♥ {health}"
          f"\n⚔ {attack}"
          f"\nWeapon is {weapon}"
          f"\n===========\n")


def intro():
    # name
    name = input("What is your name, adventurer?\n")
    print(f"Greetings, {name}. Let us go on a quest!"
          "\nYou find yourself on the edge of a dark forest")
    stop(1)
    # status
    status()

    # first step
    stop(1)
    it = open('texts/intro', 'r')
    text = it.read()
    print(text)

    # first choice
    stop(3)
    ia = open('texts/intro_answer', 'r')
    text = ia.read()
    print(text)

    choice = input("You choice >>> ")
    if choice in answer_A:
        option_rock()
    elif choice in answer_B:
        print("\nWell, that was quick.\n\n")

        death = open('texts/death', 'r')
        text = death.read()
        print(text)

    elif choice in answer_C:
        option_run()
    else:
        print(required)
        intro()


def option_rock():
    print("step option_rock")


def option_run():
    print("step option_run")


intro()
