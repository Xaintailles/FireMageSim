# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:53:52 2021

@author: Gebruiker
"""

import utilities as u

p_xaint = u.Player(4000, 3100, 650)

sp_fireblast = u.Spell(name = 'fireblast'
                      ,crit_chance = 10000 ## auto-crit
                      ,spell_power_modifier = 0.792
                      ,cast_time = 0
                      ,crit_modifier = 2
                      ,cooldown = 12
                      ,school = 'fire'
                      ,charges = 4)

bu_heatingup = u.Buff(False,8,0)
bu_hotstreak = u.Buff(False,14,0)

history = u.History(time = 0
                    , total_damage = 0
                    , gcd = 1)

print('hu present: {}, hs present: {}'.format(bu_heatingup.present,bu_hotstreak.present))

u.cast_spell(player = p_xaint
           ,spell = sp_fireblast
           ,history = history
           ,heating_up = bu_heatingup
           ,hot_streak = bu_hotstreak
           )

print('hu present: {}, hs present: {}'.format(bu_heatingup.present,bu_hotstreak.present))

print(not(bu_hotstreak.present))


test = 2
test -= 1
print(test)
    