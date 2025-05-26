from betski_classes import Match

# Define global variables
leagues = ["NFL", "NBA", "NHL", "MLB"]
discrepancy_threshold = 0.142

def api_call(league):
    matches = []
    for m in league:
        M = Match()
        matches.append(M)
    return matches

def notifier(M):
    print(f"{M.away_team} vs {M.home_team} on {M.date} identified. Home Team Prediction: {M.ht_prediction}, Moneyline: {M.ht_moneyline}, Spread: {M.ht_spread}")
    return
"""
Main loop logic

#1 Data Collection Loop
    1. For each league, open the Scores page on ESPN
    2. Construct a Match object for each match on the page
    3. Calculate discrepancy figure
    4. If 
"""


for league in leagues:
    all_matches = api_call(league)
    for read_Match in all_matches:
        if (read_Match.ht_prediction > 0.5 and read_Match.ht_moneyline >= 0) or (read_Match.ht_prediction < 0.5 and read_Match.ht_moneyline <= 0):
            notifier(read_Match)
