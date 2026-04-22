
user_input = input('Press x to stop\nEnter your calculations - ')
calc_list = []
while user_input != "x":
    user_input = input('Enter your calculations')
    if user_input == del:
        clear_memory(calc_list)
    else:
    calc_list += user_input
else:
    print(calc_list)


def clear_memory(calc_list):
    return calc_list == calc.list.clear()
