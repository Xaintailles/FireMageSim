# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:12:48 2021

@author: Gebruiker
"""

import utilities as u

p_xaint = u.Player(4000, 3100, 650)

total_duration = 60

history = u.History(time = 0
                    , total_damage = 0
                    , gcd = 1)

# %% spell declaration
sp_fireball = u.Spell(name = 'fireball'
                      ,crit_chance = p_xaint.crit_rating
                      ,spell_power_modifier = 0.65
                      ,cast_time = 2.25
                      ,crit_modifier = 2
                      ,cooldown = -1
                      ,school = 'fire'
                      ,charges = -1)

sp_pyroblast = u.Spell(name = 'pyroblast'
                      ,crit_chance = p_xaint.crit_rating
                      ,spell_power_modifier = 1.363
                      ,cast_time = 4.5
                      ,crit_modifier = 2
                      ,cooldown = -1
                      ,school = 'fire'
                      ,charges = -1)

sp_fireblast = u.Spell(name = 'fireblast'
                      ,crit_chance = 10000 ## auto-crit
                      ,spell_power_modifier = 0.792
                      ,cast_time = 0
                      ,crit_modifier = 2
                      ,cooldown = 12
                      ,school = 'fire'
                      ,charges = 4)
# %% buffs declaration
buffs = {}
bu_heatingup = u.Buff(False,8,0)
bu_hotstreak = u.Buff(False,14,0)

buffs['heatingup'] = bu_heatingup
buffs['hotstreak'] = bu_hotstreak


# %% main script

while history.time < total_duration:
    if bu_heatingup.present and sp_fireblast.charges > 0 and not(bu_hotstreak.present):
        print('cast fireblast')
        u.cast_spell(player = p_xaint
                     ,spell = sp_fireblast
                     ,history = history
                     ,heating_up = bu_heatingup
                     ,hot_streak = bu_hotstreak)
    
    elif bu_hotstreak.present:
        print('cast pyroblast')
        u.cast_spell(player = p_xaint
                     ,spell = sp_pyroblast
                     ,history = history
                     ,heating_up = bu_heatingup
                     ,hot_streak = bu_hotstreak)
        
        bu_hotstreak.present = False
    
    else:
        print('cast fireball')
        u.cast_spell(player = p_xaint
                     ,spell = sp_fireball
                     ,history = history
                     ,heating_up = bu_heatingup
                     ,hot_streak = bu_hotstreak)

# reseting the loop
history = u.History(time = 0
                    , total_damage = 0
                    , gcd = 1)
