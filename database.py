import sqlite3

class SimpleSQLiteDB:
    db_file = "ufc.db"

    def __init__(self):
        self.db_file = self.db_file
        self.connection = sqlite3.connect(self.db_file)

#create tables
    def create_tables(self):
        self.create_event_table()
        self.create_fight_table()

    def create_event_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS Event (
                event_ID INTEGER PRIMARY KEY,
                event_name TEXT NOT NULL,
                event_date INTEGER NOT NULL,
                location TEXT NOT NULL
            )
        '''
        self.connection.execute(query)
        self.connection.commit()

    def create_fight_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS Fight (
                ID INTEGER PRIMARY KEY,
                first_fighter TEXT NOT NULL,
                second_fighter TEXT NOT NULL,
                first_fighter_won INTEGER,
                new_fight INTEGER,
                event_ID INTEGER NOT NULL,
                FOREIGN KEY (event_ID) REFERENCES Event (event_ID)
            )
        '''
        self.connection.execute(query)
        self.connection.commit()

#insert data
    def add_event(self, event):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Event (event_name, event_date, location) VALUES (?,?,?)",
                                (event.name, event.date, event.location))
        self.connection.commit()
        event_id = cursor.lastrowid

        for fight in event.fights:
            self.add_fight(fight, event_id)

    def add_fight(self, fight, event_id):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Fight (first_fighter, second_fighter, first_fighter_won, new_fight, event_ID) VALUES (?,?,?,?,?)", (fight.fighter1, fight.fighter2, fight.fighter1_won, 1, event_id))
        self.connection.commit()

#access data
    def retrieve_events(self):
        query = 'SELECT * FROM Event'
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def retrieve_event(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * From Event WHERE event_ID = ?", (id,))
        return cursor.fetchone()

    def retrieve_fights(self, id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT ID, first_fighter, second_fighter, first_fighter_won FROM Fight where event_ID = ?', (id,))
        return cursor.fetchall()
        
