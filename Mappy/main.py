from user import user
from location import location

Me = user("michaeldubya", "1337", "Michael", "Wiedner", "Program Finance Analyst", "Leidos", location("United States of America", "Florida", "Stuart", "Fern Street", 142))
Boom = user("bknrn", "spadefish", "Boom", "Na Ranong", "Goat", "Thailand", location("Thailand", "", "Bangkok", "Watchback Street", 42))

print(Me.company)
Me.close_friends_list.append(Boom)

