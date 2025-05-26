from location import location

class user:
    close_friends_list = []
    friends_list = []
    connections_list = []

    def __init__(self, username, password, first_name, last_name, job_title, company, location):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.company = company
        self.location = location
        self.close_friends_list = []
        self.friends_list = []
        self.connections_list = []