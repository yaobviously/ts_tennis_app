# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:10:32 2023

@author: yaobv
"""
import os
import streamlit as st
import pickle

from trueskillthroughtime import Player, Game

current_dir = os.getcwd()

# Go up one directory
small_dict_path = os.path.join(current_dir, "womens_small_dict.pickle")
womens_names = os.path.join(current_dir, "women_names.pickle")

with open(small_dict_path, 'rb') as file:
    wta_dict = pickle.load(file)
    

with open('women_names.pickle', 'rb') as players:
    wta_players = pickle.load(players)


def get_win_prob_women(p_1='Jennifer Elie', p_2='Iga Swiatek', surface='Clay'):
    
  player_1 = Player(wta_dict[p_1][-1])
  player_1_surface = Player(wta_dict[p_1 + surface][-1])
  player_2 = Player(wta_dict[p_2][-1])
  player_2_surface = Player(wta_dict[p_2 + surface][-1])
  
  proba = Game([[player_1, player_1_surface], [player_2, player_2_surface]]).evidence
  return round(proba, 3)


st.title('True Skill Win Probabilities')

player_1 = st.selectbox('Player One', sorted(wta_players))
player_2 = st.selectbox('Player Two', sorted(wta_players))
surface_pick = st.selectbox('Surface', ['Clay', 'Hard', 'Grass', 'Carpet'])

data = str(get_win_prob_women(p_1=player_1, p_2=player_2, surface=surface_pick))

st.text(f'Player 1 Win Probability: {data}')