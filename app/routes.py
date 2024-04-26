from flask import Flask, request, jsonify
from app.models.player import Player
from app.models.game import Game
from app.models.game_status import GameStatus
from app.dal import DAL
from werkzeug.urls import quote
from app import app

dal = DAL("database.db")

# Create database tables if they don't exist
dal.create_player_table()
dal.create_game_table()
dal.create_game_status_table()

@app.route('/players', methods=['GET'])
def get_players():
    players = dal.get_all_players()
    return jsonify(players)

@app.route('/players', methods=['POST'])
def create_player():
    data = request.json
    player_name = data.get('player_name')
    
    player_id = dal.create_player(player_name)
    return jsonify({"player_id": player_id}), 201

