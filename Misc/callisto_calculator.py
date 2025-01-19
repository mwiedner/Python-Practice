def tick_rounder(n):
    if (n / 0.6) % 1 == 0:
        return round(n,1)
    ticks_within = round(n / 0.6,0)
    return round(ticks_within * 0.6,1)

artio_drop_rate = 1 / 912
callisto_drop_rate = 1 / 360

count_of_players = 0
callisto_ttk = 0
artio_ttk = 62
if count_of_players > 0:
    if callisto_ttk > 0:
        artio_ttk = (callisto_drop_rate**(-1) * count_of_players * callisto_ttk) / artio_drop_rate**(-1)
        result = artio_ttk
    else:
        callisto_ttk = (artio_drop_rate**(-1) * artio_ttk) / (callisto_drop_rate**(-1) * count_of_players)
        result = callisto_ttk
    print(result)
print()

print("If you can kill Artio in " + str(tick_rounder(artio_ttk)) + " seconds, then Callisto will be more efficient if you can kill him in less than the following times with the following group sizes:")
n = 1
while n <= 8:
    print(str(n) + " players: " + str(tick_rounder(912/(360 * n)*artio_ttk)))
    n+=1