#user pick door
#eliminate one of two non picked doors
#offer choice to swap
#compare choice (orig or swap) to winning door
#if same, successes+=1
#run 999 more times
import random

def monty_hall_no_switch():
    successes = 0
    for i in range(999):
        door_list = [1, 2, 3]
        winning_door = random.randint(1, 3)
        user_index = random.randint(0, 2)
        user_door = user_index + 1
        #door choice is user_door + 1
        del door_list[user_index]
        #door choice removed from options
        #doorlist has 2 things in it.
        if user_door == winning_door:
            successes += 1
            i += 1
        else:
            i+= 1
    print(successes/10)


def monty_hall_switch():




monty_hall_no_switch()
