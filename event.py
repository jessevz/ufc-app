class Fight:
    def __init__(self, id, fighter1, fighter2, fighter1_won):
        self.id = id
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        self.fighter1_won = fighter1_won

    def __str__(self):
        return(f"fighter1: {self.fighter1} fighter2: {self.fighter2}")
    
    def to_json(self):
        return {"fighter1": self.fighter1, "fighter2": self.fighter2, "fighter1_won": self.fighter1_won}

class Event:
    def __init__(self, id, name, date, location):
        self.id = id
        self.name = name
        self.date = date
        self.fights = []
        self.location = location

    def to_json(self):
        fights_dict = [fight.to_json() for fight in self.fights]
        return {"id": self.id, "name": self.name, "date": self.date, 
                "location": self.location, "fights": fights_dict}

    def __str__(self):
        string = f"date: {self.date} event: {self.name}\n"
        for fight in self.fights:
            string = string + str(fight) + "\n"
        return(string)


