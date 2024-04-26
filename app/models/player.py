class Player:
    def __init__(self, player_id, player_name, player_score=0):
        self.player_id = player_id
        self.player_name = player_name
        self.player_score = player_score

    def update_score(self, new_score):
        self.player_score = new_score

    # Methods for CRUD operations on player details
