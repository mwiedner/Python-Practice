from betski_classes import Match
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date
import os
import csv


# Define global variables
leagues = ["nfl", "nba", "nhl", "mlb"]
# Mimic a real browser (Chrome)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

import csv

def write_to_csv(M, path):
    # If the file does not exist, write the header first
    file_exists = os.path.isfile(path)
    with open(path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow([
                "date", "home_team", "away_team", "ht_moneyline", "ht_spread",
                "ht_prediction", "league", "gamecast_url", "home_team_score", "away_team_score"
            ])
        writer.writerow([
            M.date,
            M.home_team,
            M.away_team,
            M.ht_moneyline,
            M.ht_spread,
            M.ht_prediction,
            M.league,
            M.gamecast_url,
            M.home_team_score,
            M.away_team_score
        ])

def calculate_correlation(data_path = os.getcwd() + r"completed_matches_data_collection.csv"):
    # Calculate the linear regression of moneyline - prediction; moneyline - spread
    a=5

# Call the ESPN API to find all matches in a day
# Returns a list of Match objects
def api_call(league, yesterday_collection=False):
    matches = []
    if yesterday_collection:
        url = "something_else"
    else:
        url = f"https://www.espn.com/{league}/scoreboard"

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Debug: print all <a> tag texts
    for link in soup.find_all("a", href=True):
        #print(f"Link text: '{link.text.strip()}' | href: {link['href']}")
        if link.text.strip().lower() == "gamecast":
            gamecast_url = link["href"]
            if not gamecast_url.startswith("http"):
                gamecast_url = "https://www.espn.com" + gamecast_url
            #print(f"Found Gamecast URL: {gamecast_url}")
            gc_response = requests.get(gamecast_url, headers=headers)
            gc_soup = BeautifulSoup(gc_response.text, "html.parser")

            print(gc_soup)

            #date =
            #home_team = 
            #away_team = 
            #ht_moneyline = 
            #ht_spread =
            #ht_prediction =
            #home_team_score = 
            #away_team_score = 
            
            #M = Match(date=,home_team=,away_team=,ht_moneyline=,ht_spread=,ht_prediction=,league=league,gamecast_url=gamecast_url,home_team_score=home_team_score if yesterday_collection else None, away_team_score=away_team_score if yesterday_collection else None)
            #matches.append(M)
    return matches

def notifier(M):
    #print(f"{M.away_team} vs {M.home_team} on {M.date} identified. Home Team Prediction: {M.ht_prediction}, Moneyline: {M.ht_moneyline}, Spread: {M.ht_spread}")
    return
"""
Main loop logic

#1 Data Collection Loop
    1. For each league, open the Scores page on ESPN
    2. Construct a Match object for each match on the page
    3. Calculate discrepancy figure
    4. If 
"""

print(api_call("nba"))

for league in leagues:
    today_matches = api_call(league)
    for read_Match in today_matches:
        if (read_Match.ht_prediction > 0.5 and read_Match.ht_moneyline >= 0) or (read_Match.ht_prediction < 0.5 and read_Match.ht_moneyline <= 0):
            notifier(read_Match)
    yesterday_matches = api_call(league, True)
    for read_Match in yesterday_matches:
        write_to_csv(M, path=os.getcwd() + r"completed_matches_data_collection.csv")