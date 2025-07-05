from dataclasses import dataclass, field
from typing import Optional

@dataclass 
class Match:
    date: Optional[str] = None
    home_team: Optional[str] = None
    away_team: Optional[str] = None
    ht_moneyline: Optional[float] = None
    ht_spread: Optional[float] = None
    ht_prediction: Optional[float] = None
    league: Optional[str] = None
    gamecast_url: Optional[str] = None
    home_team_score: Optional[int] = None
    away_team_score: Optional[int] = None
    #discrepancy_figure: Optional[float] = None

"""
For a given match, the moneyline figure and prediction figure are expected to correlate.
It would be an outlier but not impossible scenario for these two figures to be disconnected.

In a perfectly even match, the prediction would be 0.5, the moneyline would be 0, and the spread would be 0.

In a perfectly uneven match, the prediction would asymptotically approach 1, moneyline would be -infinity, and the spread would be -infinity.

"""