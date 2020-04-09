import adventure_dictionaries as ad

x, y = 0, 0
movements = ad.movements
objects = ad.objects
allowed_verbs = ad.allowed_verbs
place = ad.place
backpack = []
counter = 0
action = "dont read this"

def get_command():
    while True:
        command = input("What now ")
        directed_dict = allowed_verbs[action][1]
        action, sec_action = command
        if sec_action in directed_dict:
            break
    return action, sec_action

def move_actor():
    global movements
    global action
    global sec_action
    global x, y
    dx, dy = movements[sec_action]
    x += dx
    y += dy
    if action == "go":
        print("You went", sec_action, "and you are in the", place[x, y])

def find_objects():
    global objects
    global found_objects
    global backpack
    found_objects = []
    for key in objects:
        if objects[key] == (x, y):
            if objects[key] not in backpack:
                found_objects.append(key)
    return found_objects

def analyse_actions():
    global allowed_verbs
    global backpack
    global action, sec_action
    global x, y
    global found_objects
    for i in found_objects:
        if action == "get" or action == "drive":
            if sec_action in found_objects:
                if sec_action not in backpack:
                    backpack.append(sec_action)
    if action == "drop":
        if sec_action in backpack:
            backpack.remove(sec_action)
    return backpack

def analyse_found_objects():
    global found_objects
    backpack = analyse_actions()
    for object in found_objects:
        if object in backpack:
            found_objects.remove(object)
    if len(found_objects) == 0:
        print("You have found nothing")
    else:
        print("You have found a", ", ".join(found_objects))
    if len(backpack) == 0:
        print("You have nothing")
    else:
        print("You have a", ", ".join(backpack))


while True:
    if counter == 0:
        find_objects()
        analyse_actions()
        analyse_found_objects()
    action, sec_action = get_command()
    move_actor()
    find_objects()
    analyse_actions()
    analyse_found_objects()
    counter += 1