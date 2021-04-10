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
    def __init__(self,name,crit_chance,spell_power_modifier,cc_cast,nm_cast,cast_time,crit_modifier):
        self.name = name
        self.crit_chance = crit_chance
        self.spell_power_modifier = spell_power_modifier
        self.cc_cast = cc_cast
        self.nm_cast = nm_cast
        self.cast_time = cast_time
        self.crit_modifier = crit_modifier
        
class crit_counter:
    value = 0
    
class History:
    def __init__(self,time,total_damage,gcd):
        self.time = time
        self.total_damage = total_damage
        self.gcd = gcd

def cast_spell(player: player, spell: spell):

    damage = spell.spell_power_modifier * player.spell_power
    roll = random.randrange(0,10000)
       
    if spell.crit_chance >= roll:
        spell_state = 'cc'
        damage = spell.spell_power_modifier * player.spell_power * spell.crit_modifier
        if spell.name == 'fireball':
            spell.crit_chance = player.crit_rating
    else:
        spell_state = 'nc'
        if spell.name == 'fireball':
            spell.crit_chance += 1000

    
    return {  'spell_name': spell.name
            , 'cast_time': spell.cast_time
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

def reset_counters(crit_counter, time, gcd, total_damage):
    crit_counter = 0
    time = 0
    gcd = 1
    total_damage = 0
    
    return(crit_counter, time, gcd, total_damage)

def run_a_sim(
        total_duration: int 
        ,player: player
        ):
    
    crit_counter = 0
    history = History(0, 0, 1)
    
    sp_fireball = spell('fireball',player.crit_rating,0.65,0,0,2.25,2)
    sp_pyroblast = spell('pyroblast',player.crit_rating,1.363,0,0,4.5,2)
    
    
    while history.time < total_duration:
        d = cast_spell(player, sp_fireball)
        crit_counter = crit_counter_check(crit_counter, d['spell_state'])
        
        history.total_damage += d['damage_done']
        history.time += d['cast_time']
        
        if crit_counter == 2:
            d = cast_spell(player, sp_pyroblast)
            crit_counter = 0
            
            history.total_damage += d['damage_done']
            history.time += history.gcd
           
    return history