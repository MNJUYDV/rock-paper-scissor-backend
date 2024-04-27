import sqlite3

class DAL:
    _instance = None

    def __new__(cls, db_name):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.db_name = db_name
        return cls._instance

    def connect(self):
        return sqlite3.connect(self.db_name)

    def execute_sql(self, sql, params=None, fetch_all=False):
        print("Params are ", params)
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
        if fetch_all:
            result = cursor.fetchall()
        else:
            result = cursor.lastrowid
        conn.close()
        return result

    def create_player_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS player (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )'''
        self.execute_sql(sql)

    def create_game_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS game (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    type TEXT
                )'''
        self.execute_sql(sql)
        
    def create_leaderboard(self):
        sql = '''CREATE TABLE IF NOT EXISTS leaderboard (
                    id INTEGER PRIMARY KEY, 
                    game_id INTEGER,
                    player_id INTEGER,
                    player_score INTEGER,
                    computer_score INTEGER,
                    last_modified DATE,
                    FOREIGN KEY (game_id) REFERENCES game(id),
                    FOREIGN KEY (player_id) REFERENCES player(id)
                )'''
        self.execute_sql(sql)

    def get_all_players(self):
        sql = "SELECT * FROM player"
        players = self.execute_sql(sql, fetch_all=True)
        res = [{"player_name": player[1]} for player in players]
        return res
    
    def get_all_games(self):
        sql = "SELECT * FROM game"
        games = self.execute_sql(sql, fetch_all=True)
        res = [{"game_id": game[0], "game_name": game[1]} for game in games]
        return res
    
    def get_leaderboard(self):
        sql = "SELECT * FROM leaderboard"
        leaderboard = self.execute_sql(sql, fetch_all=True)
        res = [{"entry_id": entry[0], "player_id": entry[2], "player_score": entry[3], "computer_score": entry[4]} for entry in leaderboard]
        return res
    
    # def create_player(self, name):
    #     sql = "INSERT INTO player(name) VALUES (?)"
    #     player_id = self.execute_sql(sql, (name))
    #     return player_id
    
    def create_player(self, player_name):
        sql = "INSERT INTO player (name) VALUES (?)"
        player_id = self.execute_sql(sql, (player_name,))
        return player_id
    
    def create_game(self):
        sql = "INSERT INTO game (name, type) VALUES (?, ?)"
        game_id = self.execute_sql(sql, ('game', 'human vs computer'))
        return game_id
    
    def create_leaderboard_entry(self, data):
        player_name = data.get('player_name')
        player_score = data.get('player_score')
        computer_score = data.get('player_score')
        player_id = self.create_player(player_name)
        game_id = self.create_game()
        sql = "INSERT INTO leaderboard (game_id, player_id, player_score, computer_score) VALUES (?, ?, ?, ?)"
        entry_id = self.execute_sql(sql, (game_id, player_id, player_score, computer_score))
        return entry_id      
