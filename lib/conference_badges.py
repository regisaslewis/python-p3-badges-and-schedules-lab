def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    list = [f"Hello, my name is {n}." for n in names]
    return list

def assign_rooms(names):
    list = [f"Hello, {n}! You'll be assigned to room {names.index(n) + 1}!" for n in names]
    return list

def printer(names):
    for n in batch_badge_creator(names):
       print(n)
    for n in assign_rooms(names):
        print(n)