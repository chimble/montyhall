import random


def monty_hall_no_switch(num_doors):
    x = (int(num_doors) - 1)
    successes = 0
    for i in range(1000):
        door_list = list(range(int(num_doors)))
        winning_door = random.randint(0, x)
        user_door = random.randint(0, x)
        if door_list[user_door] == door_list[winning_door]:
            successes += 1
        else:
            continue
    return(successes/10)


def monty_hall_switch():
    successes = 0
    for i in range(1000):
        winning_door = random.randint(1, 3)
        user_door = random.randint(1, 3)
        if user_door == winning_door:
            continue
        else:
            successes += 1
    return(successes/10)


def fifty_fifty():
    successes = 0
    for i in range(1000):
        winning_door = random.randint(1, 3)
        user_door = random.randint(1, 3)
        switch = random.randint(0, 1)
        if switch:
            if user_door == winning_door:
                continue
            else:
                successes += 1
        else:
            if user_door == winning_door:
                successes += 1
            else:
                continue
    return(successes/10)


doors = input("number of doors? ")
print("Never switch %: {} \nAlways switch %: {}\n50/50 Switch/No switch %: {}"
      .format(monty_hall_no_switch(doors), monty_hall_switch(), fifty_fifty()))
