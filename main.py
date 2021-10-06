import os
from random import randrange
import json
import SpellCasting

d2 = 2
d3 = 3
d4 = 4
d5 = 5
d6 = 6
d8 = 8
d10 = 10
d12 = 12
d20 = 20
d100 = 100

SpellCasting.test_function()

# rolls given die and returns the value rolled
def roll(die):
    return randrange(die) + 1


# when making a skill check you need to know
# skill, which skill modifier to add
# modifier, stat modifier plus possible proficiency modifier
def skill_check(skill):
    fake = 0


# when making a saving throw you need to know
# skill, which of 6 skills you're saving
# modifier, the skill's modifier with or without proficiency bonus based on class
def saving_throw(skill):
    fake = 0


# when an attack roll is made you need to know
# weapon type, for proficiency and damage later (This is used for spell attacks too)
# attack modifier, made of proficiency and additional bonus'
def attack_roll(modifier):
    fake = 0


# when rolling damage you need to know
# amount and type of dice to roll
# the damage modifier, typically str or dex otherwise none, maybe some from class effects
# damage type, should spit it out to help
def roll_damage(d4s, d6s, d8s, d10s, d12s, modifier):
    fake = 0
