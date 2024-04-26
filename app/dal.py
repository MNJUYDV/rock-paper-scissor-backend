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
        sql = '''CREATE TABLE IF NOT EXISTS players (
                    player_id INTEGER PRIMARY KEY,
                    player_name TEXT
                )'''
        self.execute_sql(sql)

    def create_game_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS games (
                    game_id INTEGER PRIMARY KEY,
                    game_name TEXT,
                    game_type TEXT
                )'''
        self.execute_sql(sql)

    def create_game_status_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS game_status (
                    game_id INTEGER,
                    player_id INTEGER,
                    status TEXT,
                    FOREIGN KEY (game_id) REFERENCES games(game_id),
                    FOREIGN KEY (player_id) REFERENCES players(player_id)
                )'''
        self.execute_sql(sql)

    def get_all_players(self):
        sql = "SELECT * FROM players"
        players = self.execute_sql(sql, fetch_all=True)
        res = [{"player_name": player[1], "wins": 4, "losses": 3, "ties": 6} for player in players]
        return res
    
    def create_player(self, player_name):
        sql = "INSERT INTO players (player_name) VALUES (?)"
        player_id = self.execute_sql(sql, (player_name,))
        return player_id

    # Implement methods for CRUD operations on game, game status, etc.
