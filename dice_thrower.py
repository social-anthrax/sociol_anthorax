import random


def dice(*args):
    term = "".join(args)
    rolls = []
    totalDice = ""
    total = 0

    for dice in term.split(" "):
        num = 0
        type = dice.lower().find("d")

        if type == "-1":
            exit()

        char = list(dice)
        number = int("".join(char[:type]))
        dice = "".join(char[type + 1:])
        if int(number) >= 300:
            print("no")
            return None

        totalDice = totalDice + "("
        totalDice = totalDice + "d" + dice + ": "

        rolls = []
        for i in range(0, number):
            rolls.append(str(random.randint(1, int(dice))))
        for x in rolls:
            totalDice = totalDice + "{" + x + "} "
            total = total + int(x)
        totalDice = totalDice + ")"

    totalDice = totalDice + " = " + str(total)

    return totalDice
