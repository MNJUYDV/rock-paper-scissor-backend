from app import ma
from app.models.player import Player

class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
