from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game
from models.players import players_list

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/player2')
def player2():
    play_1_choice = request.form['player_1_choice']
    player1 = Player("Player 1", play_1_choice)
    players_list.append(player1)
    return render_template('player2.html')

@app.route('/result')
def result():
    play_2_choice = request.form['player_2_choice']
    player2 = Player("Player 2", play_2_choice)
    players_list.append(player2)
    print(players_list)
    return render_template('result.html')