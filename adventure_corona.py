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
        while True:
            command = input("What now ").lower()
            if len(command.split()) == 2:
                action, sec_action = command.split()
                if action in allowed_verbs:
                    if action == "go":
                        if sec_action in movements:
                            break
                    else:
                        if sec_action in allowed_verbs[action][0]:
                            break
        directed_dict = allowed_verbs[action][0]
        if sec_action in directed_dict:
            break
    return action, sec_action

def move_actor():
    #global movements
    #global action
    #global sec_action
    global x, y
    global current_room
    if action == "go":
        dx, dy = movements[sec_action]
    else:
        dx, dy = 0, 0
    x += dx
    y += dy
    if counter != 0:
        if action == "go":
            print(sec_action, ",", movements[sec_action])
    if counter == 0:
        current_room = place[x, y]
    if (x, y) not in place:
        return "hit"
    else:
        current_room = place[x, y]
        if action == "go":
            print(allowed_verbs[sec_action][1], sec_action, "and you are in the", current_room)
        else:
            print("You are in the", current_room)
        return "not hit"
    if counter == 0:
        if action == "go":
            print(allowed_verbs[sec_action][1], sec_action, "and you are in the", current_room)
        else:
            print("You are in the", current_room)

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
    global action, sec_action
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
    #global found_objects
    backpack = analyse_actions()
    for object in reversed(found_objects):
        if object in backpack:
            found_objects.remove(object)
    if len(found_objects) != 2:
        joined_found_objects = ", ".join(found_objects)
    else:
        joined_found_objects = " and a ".join(found_objects)
    if len(found_objects) == 0:
        print("You have found nothing")
    else:
        print("You have found a", joined_found_objects)
    if len(backpack) == 0:
        print("You have nothing")
    else:
        print("You have a", ", ".join(backpack))

while True:
    if counter == 0:
        move_actor()
        find_objects()
        analyse_actions()
        analyse_found_objects()
    action, sec_action = get_command()
    while True:
        status = move_actor()
        if status == "not hit":
            break
        else:
            print("You have hit a boundary.\nGo somewhere else.")
            action, sec_action = get_command()
    find_objects()
    analyse_actions()
    analyse_found_objects()
    counter += 1