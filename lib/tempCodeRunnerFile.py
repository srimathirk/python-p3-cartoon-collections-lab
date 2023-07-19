def roll_call_dwarves(list_dwarfs):
    for list_dwarf in list_dwarfs:
        print(f"{list_dwarfs.index(list_dwarf)+1}. {list_dwarf}")
    #for index,list_dwarf in enumerate(list_dwarfs):
        #print(f"{index+1}. {list_dwarf}")
roll_call_dwarves(["dopey", "Bashful"])
def summon_captain_planet(planeteer_calls):
    list = [f"{planeteer_call.capitalize()}!" for planeteer_call in planeteer_calls]
    print(list)
    return list
summon_captain_planet(["mercury", "venus", "earth"])
def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            print(True)
            return True #return true if any calls greater than 4char
    print(False)
    return False
long_planeteer_calls(["Fire", "Earth", "wind", "axe"])
def find_the_cheese(cheese_strings):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for cheese_string in cheese_strings:
        if cheese_string in cheese_types:
            print(cheese_string)
            return cheese_string
    return None

find_the_cheese(["tomato soup", "gouda", "cheddar", "oyster crackers", "gouda"])
