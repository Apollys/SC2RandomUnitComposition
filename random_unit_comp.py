'''
Python script to generate random "viable" unit compositions for a given race.
This may be upgraded to take the opponent's race into account also.
'''

import random


class SC2Unit:
    def __init__(self, name, value, tier, attacks_ground, attacks_air):
        self.name = name
        self.value = value
        self.tier = tier
        self.attacks_ground = attacks_ground
        self.attacks_air = attacks_air
        
    
# List of Protoss units
kProtossUnits = [
    SC2Unit('Zealot', 4, 1, True, False),
    SC2Unit('Stalker', 10, 1.5, True, True),
    SC2Unit('Sentry', 3, 1.5, True, True),
    SC2Unit('Adept', 2.5, 1.5, True, False),
    # TODO: decide how to handle choosing if HTs/DTs can morph to Archons
    # (For now, archons are rolled independently, but this isn't ideal)
    SC2Unit('High Templar', 3, 3, False, False),
    SC2Unit('Dark Templar', 4, 3, True, False),
    SC2Unit('Archon', 7, 3, True, True),
    SC2Unit('Immortal', 4, 2, True, False),
    SC2Unit('Colossus', 5, 3, True, False),
    SC2Unit('Disruptor', 4, 3, True, False),
    SC2Unit('Oracle', 3, 2, True, False),
    SC2Unit('Phoenix', 5, 2, False, True),
    SC2Unit('Void Ray', 9, 2, True, True),
    SC2Unit('Tempest', 6, 3, True, True),
    SC2Unit('Carrier', 8, 3, True, True)
]

kTerranUnits = [
    SC2Unit('Marine', 12, 1, True, True),
    SC2Unit('Reaper', 4, 1, True, False),
    SC2Unit('Marauder', 5, 1.5, True, False),
    SC2Unit('Ghost', 6, 2, True, True),
    SC2Unit('Hellion/Hellbat', 5, 2, True, False),
    SC2Unit('Siege Tank', 7, 2, True, False),
    SC2Unit('Widow Mine', 7, 2, True, True),
    SC2Unit('Cyclone', 10, 2, True, True),
    SC2Unit('Thor', 6, 2.5, True, True),
    SC2Unit('Banshee', 4, 3, True, False),
    # Note: Ravens are always allowed to be used as a detector,
    # but abilities only allowed if the Raven is selected
    SC2Unit('Raven', 4, 3, False, False),
    SC2Unit('Liberator', 6, 3, True, True),
    SC2Unit('Battlecruiser', 8, 3, True, True)
]

kZergUnits = [
    SC2Unit('Zergling + Baneling', 6, 1, True, False),
    SC2Unit('Roach + Ravager', 8, 1.5, True, False),
    SC2Unit('Hydralisk', 6, 2, True, True),
    SC2Unit('Lurker', 5, 2, True, False),
    SC2Unit('Swarm Host', 3, 2, True, False),
    SC2Unit('Mutalisk', 8, 2.5, True, True),
    SC2Unit('Corruptor', 7, 2.5, False, True),
    SC2Unit('Brood Lord', 5, 3, True, False),
    SC2Unit('Ultralisk', 4, 3, True, False),
    SC2Unit('Infestor', 4, 2, False, False),
    SC2Unit('Viper', 6, 3, False, False)
]
    

# Generate a random unit combination with value in the given range
def TryRollCombination(units_list, min_total_value, max_total_value):
    total_value = 0
    unit_combination = []
    while (total_value < min_total_value):
        new_unit = random.choice(units_list)
        if (new_unit in unit_combination):
            continue
        total_value += new_unit.value
        unit_combination.append(new_unit)
        # Reset if exceeded maximum
        if (total_value > max_total_value):
            unit_combination = []
            total_value = 0
    return unit_combination


# Check if a unit combination is valid
# Currently, this means checking if it can attack both air and ground
def UnitCombinationIsValid(unit_combination):
    attacks_ground = False
    attacks_air = False
    for unit in unit_combination:
        attacks_ground = attacks_ground or unit.attacks_ground
        attacks_air = attacks_air or unit.attacks_air
    return attacks_ground and attacks_air
    

# Generates a valid unit combination from the given units list    
def RollCombination(units_list, min_total_value, max_total_value):
    success = False
    while (not success):
        unit_combination = TryRollCombination(units_list, min_total_value, max_total_value)
        success = UnitCombinationIsValid(unit_combination)
    return unit_combination


# Checks if the unit combination contains any tier 1 (or 1.5) unit(s)
def ContainsTier1Unit(unit_combination):
    for unit in unit_combination:
        if (unit.tier < 2):
            return True
    return False


# Main loop: queries the user for their race, then outputs a random unit composition
def main():
    while (True):
        # Get user input
        race = ''
        units_list = []
        while(units_list == []):
            print('\n------------------------------\n')
            race = input('Enter your race: ')
            race = race[0].lower()
            if (race == 't'):
                units_list = kTerranUnits
            elif (race == 'p'):
                units_list = kProtossUnits
            elif (race == 'z'):
                units_list = kZergUnits
            else:
                print('Please input either "t", "p", or "z"')
        print()
                
        # Roll a unit combination for the given race
        unit_combination = RollCombination(units_list, 10, 15)
        for unit in unit_combination:
            print(unit.name, ' [', unit.value, '] ', sep='')
        if (not ContainsTier1Unit(unit_combination)):
            if (race == 'z'):
                print('+ 6 Zerglings')
            else:
                print('+ 4 Tier 1(.5) units')


if __name__ == '__main__':
    main()
