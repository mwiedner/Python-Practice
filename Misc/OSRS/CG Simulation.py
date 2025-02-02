import random
import math

starting_kc = 212
starting_armor_seeds = 5
starting_enh = 0

def simulate_boss_kills(p_weapon, p_armor, num_weapons_needed, num_armors_needed, trials):
    total_kills = 0

    for _ in range(trials):
        weapon_seeds = starting_enh
        armor_seeds = starting_armor_seeds
        kills = starting_kc

        # Continue until the required number of both seeds are obtained
        while weapon_seeds < num_weapons_needed or armor_seeds < num_armors_needed:
            kills += 1
            # Simulate getting the enhanced crystal weapon seed
            if random.random() < p_weapon:
                weapon_seeds += 1
            # Simulate getting the crystal armor seed
            if random.random() < p_armor:
                armor_seeds += 1

        total_kills += kills

    # Average number of kills per trial
    return total_kills / trials

# Probability of enhanced crystal weapon seed
probability_weapon = 0.0025
# Probability of crystal armor seed
probability_armor = 0.02
# Number of each seed needed
needed_weapon_seeds = 1
needed_armor_seeds = 6
# Number of simulation trials
number_of_trials = 10000

average_kills = simulate_boss_kills(probability_weapon, probability_armor, needed_weapon_seeds, needed_armor_seeds, number_of_trials)
print(f"Average: {average_kills}, so you need to complete the Corrupted Gauntlet {math.ceil(average_kills) - starting_kc} more times")
