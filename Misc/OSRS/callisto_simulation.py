import random
import math

artio_drop_rate = 1 / 912
callisto_drop_rate = 1 / 360

def simulate_boss_kills(drop_rate, player_count, trials):
    total_kills = 0

    for _ in range(trials):
        hilt_dropped = False
        kills = 0

        while hilt_dropped == False:
            kills += 1
            if random.random() < (drop_rate / player_count):
                hilt_dropped = True
                print("Dropped at " + str(kills) + " kill count")

        total_kills += kills

    return total_kills / trials

print(simulate_boss_kills(callisto_drop_rate, 3, 1000))