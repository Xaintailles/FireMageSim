# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:12:38 2021

@author: Gebruiker
"""

import random

class player:
    def __init__(self,spell_power,crit_rating,haste_rating):
        self.spell_power = spell_power
        self.crit_rating = crit_rating
        self.haste_rating = haste_rating

class spell:
    def __init__(self,crit_chance,spell_power_modifier,cc_cast,nm_cast,cast_time,crit_modifier):
        self.crit_chance = crit_chance
        self.spell_power_modifier = spell_power_modifier
        self.cc_cast = cc_cast
        self.nm_cast = nm_cast
        self.cast_time = cast_time
        self.crit_modifier = crit_modifier

def cast_spell(player: player, spell: spell):

    damage = spell.spell_power_modifier * player.spell_power
    roll = random.randrange(0,10000)
       
    if spell.crit_chance >= roll:
        spell_state = 'cc'
        damage = spell.spell_power_modifier * player.spell_power * spell.crit_modifier
    else:
        spell_state = 'nc'
        
    if
    
    return {  'cast_time': spell.cast_time
            , 'damage_done': damage
            , 'spell_state': spell_state
            , 'roll': roll
            }
    
def crit_counter_check(crit_counter: int, previous_spell_state: str):
    if previous_spell_state == 'cc':
        crit_counter += 1
    else:
        crit_counter = 0
    
    return crit_counter