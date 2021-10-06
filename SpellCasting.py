import json


# DAMAGE TAG (Cantrips)
# "damage type, modifier(optional) NS(no scale optional) dice_effect1 dice_effect2,
# modifier(optional) NS(no scale optional) dice_effect1 dice_effect2..."

# EFFECTS TAG
# Active - spell happens without an attack or a save

# Ranged Spell Attack - don't include damage thats taken care of in damage
# "Ranged Spell Attack, Effect_1, Effect_2..."
# Melee Spell Attack - don't include damage thats taken care of in damage
# "Melee Spell Attack, Effect_1, Effect_2..."
# Saving Throw - two types some then just cause an effect, some then cause damage roll.
# "Saving Throw, Stat, Effect_n..."
# Melee Attack -
# "Melee Attack, Effect_N..."

# 'modifier' tag might need to be looked at, make more specific
# 'modifier' and 'NS' tag in damage might need an easier way to read, where/when do you check for it?


# Spell Levels 1-9


# Effect Tag (Multieffect) - ['Tag_1', 'Tag_2']

# Effect Tag (Weapon Upgrade) - "Weapon Upgrade, What occurs"
# Effect Tag (Continuous) - "Continuous, When to take damage, how to end effect"
# Effect Tag (Ranged Spell Attack) - "Ranged Spell Attack, Effect"
# Effect Tag (Melee Spell Attack) - "Melee Spell Attack, Effect"
# Effect Tag (Melee Attack) - "Melee Attack, Effect"
# Effect Tag (Saving Throw) - "Saving Throw, Type, Effect"
# Effect Tag (Active) - "Active" spell just occurs without any roll

# Smite needs a special connection to the melee attack so that you can chose to add it to a roll on a weapon once cast
# Could this be included in the concentration GUI ?
# Effect Tag (Smite) - "Smite, Next Melee Attack Deals extra Damage, EXTRA EFFECT TYPICALLY SAVE"
# Damage Tag (Smite) - "type, dice, scale"

# Healing won't happen automatically as it's rare you heal yourself
# Effect Tag (Healing Spells) - "Healing Spell, Roll for Heal, Additional Effects"
# Damage Tag (HEALING SPELLS) - "heal, base level roll, higher level bonus"

# you're not always rolling for yourself here so not automatically applied here
# Effect Tag (Temp HP) - "Temp HP, what you do to get it"
# Damage Tag (Temp HP) - "temp, base gain, level scaling"

# Dealing Damage to Yourself SHOULD happen on auto it only makes sense
# Effect Tag (Inflicting Damage to Self) - "Self Damage, what you do to get it"
# Damage Tag (Inflicting Damage to Self) - "type, dice, scale"

# Effect Tag (Table) - "Table, Roll for Effect_Name", spells with a special roll
# Damage Tag (Table) - "table, die to roll"

# use this info (with effect) to create damage buttons that you can push to roll the dice needed for the spell
# Damage Tag (Leveled Spells) - "type, damage, bonus per higher spell level, max number of dice" SUBJECT TO CHANGE
# multiple damage types in one effect - "type1 type2, dice1 dice2, scale1 scale2"


# WEAPON UPGRADE
# Damage tag needs update, Spells dont all increase each spell level RIGHT NOW, those that work diff get 1-9 []
# Spells whose damage doesn't scale with each spell level; Flame Blade (2), Shadow Blade(2),
# Spiritual Weapon(2), Spirit Shroud(3)
# This problem relates only to weapon upgrade/giving spells may be good reason for full effect tag
# NEEDED, FIRST TO DO

# Summon, tie summon to the creatures that are relevant, USEFUL but not important till late stages, need creatures in
# LATE STAGE, useful and really helps streamline

# table effects, Have roll available
# NEEDED, quick roll button for whatever table roll the spell needs


# spike growth, life transference, elemental bane, Tsunami weird as hell
# vitriolic sphere has diff damage on success and save
# NEW EFFECT TAG GRAPPLE
# descruction wave, FLAME STRIKE

# Shillelagh, changes damage die of basic weapon
# Magic Weapon, makes weapon a +1 +2 +3, Elemental Weapon Has same Issue

# weird damage; sleep, blind, AC

# AURA, this is part of the CONCENTRATION GUI
# AC Modifier, DO THIS AS BUTTON NEXT TO AC IN GUI, when temp change color (up or down) and have turn on and off for it

# uses EXHAUSTION - 6 charges, long rest, number recovered



# Background Equptmnet - Equiptment - ['item, amount', 'item, amount', 'option 1, amount, option 2, amount, option N, amount']

cantrip_scale = [0, 1, 2, 3] # on level 1, 5, 11, 17 each effect gets additional dice equal to the scale value


# INFO THAT MIGHT BE BETTER SOTRED IN OTHER JAVA FILES BUT IS SMALL ENOUGH TO NOT NEED ITS OWN JSON FILE
# level 1-20
proficiency_bonus = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
# stats 1 to 30
stat_bonus = [-5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]
# alignments top left to bottom right
alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

# initiative bonus is equal to your Dex Mod
# passive perception is 10 + perception bonus


def test_function():
    fc = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Cantrips.json')
    f1 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_One_Spells.json')
    f2 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Two_Spells.json')
    f3 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Three_Spells.json')
    f4 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Four_Spells.json')
    f5 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Five_Spells.json')
    f6 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Six_Spells.json')
    f7 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Seven_Spells.json')
    f8 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Eight_Spells.json')
    f9 = open('/Users/drduf/PycharmProjects/DiceRoller/Spell Files/Level_Nine_Spells.json')

    lvlc = json.load(fc)
    lvl1 = json.load(f1)
    lvl2 = json.load(f2)
    lvl3 = json.load(f3)
    lvl4 = json.load(f4)
    lvl5 = json.load(f5)
    lvl6 = json.load(f6)
    lvl7 = json.load(f7)
    lvl8 = json.load(f8)
    lvl9 = json.load(f9)

    # print(lvl2["Druid Grove"]['effect'])

    for spell in lvl1:
        print(spell)
        print(lvl1[spell]['effect'])
        print(lvl1[spell]['damage'])
        print()






