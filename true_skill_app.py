# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 18:36:38 2023

@author: yaobv
"""

import streamlit as st
import pickle

from trueskillthroughtime import Player, Game

with open('smaller_dict.pickle', 'rb') as file:
    ts_dict = pickle.load(file)

with open('players.pickle', 'rb') as players:
    players = pickle.load(players)


def get_win_prob(p_1='Rafael Nadal', p_2='Pete Sampras', surface='Hard'):
    
  player_1 = Player(ts_dict[p_1][-1])
  player_1_surface = Player(ts_dict[p_1 + surface][-1])
  player_2 = Player(ts_dict[p_2][-1])
  player_2_surface = Player(ts_dict[p_2 + surface][-1])
  
  proba = Game([[player_1, player_1_surface], [player_2, player_2_surface]]).evidence
  return round(proba, 3)


st.title('True Skill Win Probabilities')

player_1 = st.selectbox('Player One', sorted(players))
player_2 = st.selectbox('Player Two', sorted(players))
surface_pick = st.selectbox('Surface', ['Hard', 'Clay', 'Grass', 'Carpet'])

data = str(get_win_prob(p_1=player_1, p_2=player_2, surface=surface_pick))

st.text(f'Player 1 Win Probability: {data}')