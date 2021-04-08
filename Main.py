# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:12:48 2021

@author: Gebruiker
"""

import random
import utilities as u


        
      
crit_counter = 0
time = 0
gcd = 1
total_damage = 0
       
Xaint = u.player(3500,3097,2253)
spells = {}
spells['fireball'] = u.spell(Xaint.crit_rating,0.65,0,0,2.25,2)
spells['pyroblast'] = u.spell(Xaint.crit_rating,1.363,0,0,4.5,2)

while time < 60:
    print('cast fireball')
    d = u.cast_spell(Xaint, spells['fireball'])
    
    total_damage += d['damage_done']
    time += d['cast_time']
    
    crit_counter += d['was_crit']
    if d['was_not_crit'] == 1:
        crit_counter = 0
    
    if crit_counter == 2:
        print('cast pyroblast')
        
        d = u.cast_spell(Xaint, spells['pyroblast'])
        
        total_damage += d['damage_done']
        time += d['cast_time']
        
        crit_counter = 0
        crit_counter += d['was_crit']
        if d['was_not_crit'] == 1:
            crit_counter = 0

print('total_damage = {}, duration = {}, dps = {}'.format(total_damage,time,total_damage / time))
