from dataclasses import dataclass, field
from typing import Optional

@dataclass 
class Match:
    date: str
    home_team: str
    away_team: str
    ht_moneyline: float
    ht_spread : float
    ht_prediction: float
    league: str
    gamecast_url: str
    home_team_score: Optional[int] = 0
    away_team_score: Optional[int] = 0
    #discrepancy_figure: float = 0.0

"""
For a given match, the moneyline figure and prediction figure are expected to correlate.
It would be an outlier but not impossible scenario for these two figures to be disconnected.

In a perfectly even match, the prediction would be 0.5, the moneyline would be 0, and the spread would be 0.

In a perfectly uneven match, the prediction would asymptotically approach 1, moneyline would be -infinity, and the spread would be -infinity.

"""