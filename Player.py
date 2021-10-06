class PlayerCharacter:

    def __init__(player, name, character_class, race, level, str, dex, con, int, wis, cha):
        player.name = name
        player.character_class = character_class
        player.race = race
        player.level = level
        player.strength = str
        player.dexterity = dex
        player.constitution = con
        player.intelligence = int
        player.wisdom = wis
        player.charisma = cha
