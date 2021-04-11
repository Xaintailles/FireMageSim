# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:12:38 2021

@author: Gebruiker
"""

import random

# %% Classes
class Player:
    def __init__(self,spell_power
                 ,crit_rating
                 ,haste_rating):
        
        self.spell_power = spell_power
        self.crit_rating = crit_rating
        self.haste_rating = haste_rating

class Spell:
    def __init__(self,name
                 ,crit_chance
                 ,spell_power_modifier
                 ,cast_time
                 ,crit_modifier
                 ,cooldown,school
                 ,charges):
        
        self.name = name
        self.crit_chance = crit_chance
        self.spell_power_modifier = spell_power_modifier
        self.cast_time = cast_time
        self.crit_modifier = crit_modifier
        self.cooldown = cooldown
        self.school = school
        self.charges = charges
        
class Buff:
    def __init__(self,present,base_duration,present_duration):
        self.present = present
        self.base_duration = base_duration
        self.present_duration = present_duration
        
class History:
    def __init__(self,time,total_damage,gcd):
        self.time = time
        self.total_damage = total_damage
        self.gcd = gcd
        
        
# %% functions

def cast_spell(player: Player
               , spell: Spell
               , history: History
               , heating_up: Buff
               , hot_streak: Buff):

    damage = spell.spell_power_modifier * player.spell_power
    roll = random.randrange(0,10000)
    
    if spell.charges > 0:
        spell.charges -= 1
       
    if spell.crit_chance >= roll: ## it's a crit

        damage = damage * spell.crit_modifier
        
        if spell.name == 'fireball':
            spell.crit_chance = player.crit_rating
        
        ## checking up and updating heatingup and hotstreak
        if heating_up.present:
            hot_streak.present = True
            heating_up.present = False
        elif spell.school == 'fire' and not(hot_streak.present):
            heating_up.present = True
            
    else:
        if spell.name == 'fireball':
            spell.crit_chance += 1000
    
    history.total_damage += damage
    history.time += spell.cast_time

























