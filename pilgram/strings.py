from typing import List

from pilgram.globals import ContentMeta


WORLD = ContentMeta.get('world.name')
MONEY = ContentMeta.get("money.name")
TOWN = ContentMeta.get("world.city.name")


class Strings:
    """
    class that contains all the interface-related strings that will be sent to the players.
    """

    # character creation
    character_already_created = "You already have a character! Their name is {name} and they are very sad now :("
    character_creation_get_name = "Ok, let's start by naming your character. Send me a name (4 - 20 characters)."
    character_creation_get_description = "Ok now send me your character's description (10 - 300 characters)."
    welcome_to_the_world = f"Your character has been created! Welcome to the world of {WORLD}!"

    # guild creation
    guild_already_created = "You already created a guild! You can't create another guild, you can only modify your current guild or join another."
    guild_creation_get_name = "Ok, let's start by naming your guild. Send me a name (2 - 30 characters)."
    guild_creation_get_description = "Ok now send me your guild's description (10 - 300 characters)."
    guild_creation_success = "Your guild '{name}' has been created!"

    # joining guilds
    guild_join_success = "You successfully joined guild '{guild}'!"
    player_joined_your_guild = "Player {player} joined your guild ({guild})!"
    guild_is_full = "The guild is full! Tell the owner to upgrade it or make your own."

    # quests
    check_board = "You check the quest board, you see there are quests available in the following zones:\n\n"
    already_on_a_quest = "You already are on a quest!"
    embark_underleveled = "You can still choose zones for which you are under-leveled, but you will be more likely to fail quests. Make sure to upgrade your gear!"
    embark_underleveled_confirm = "Are you sure you want go to {zone}? You should be at least level {lv} for this zone.\n\nWrite 'y' or 'n' (yes or no)"
    embark_underleveled_cancel = "Good riddance."
    not_on_a_quest = "You are not on a quest!"
    quest_embark = "You have embarked on the quest:\n\n{quest}\n\nGood luck!"
    quest_success = "\n\nYou have completed the quest '*{name}*'!"
    quest_fail = f"\n\nYou have failed to complete the quest '*{{name}}*'. An higher power lets you reappear at {TOWN}, the Ouroboros contract remains unbroken."

    # guilds
    rank_guilds = "Here are the top guilds:\n\n*guild name | prestige*"
    here_are_your_mates = "You have {num} guild mates:\n\n"
    not_in_a_guild = "You are not in a guild!"
    guild_not_owned = "You don't own a guild!"
    no_guild_yet = "You haven't created a guild yet!"

    # messages
    write_your_message = "Write the message you want to send"
    message_sent = "Your message has been sent."
    no_self_message = "You can't send a message to yourself. Weirdo."

    # upgrade
    you_paid = f"you paid {{paid}} {MONEY}."
    upgrade_object_confirmation = "Are you sure you want to upgrade your {obj}? It will cost you {price}"
    not_enough_money = f"You don't have enough {MONEY}. You need {{amount}} more."
    upgrade_successful = "The upgrade to your {obj} was successful, " + you_paid
    upgrade_cancelled = "The upgrade was cancelled."
    guild_already_maxed = "Your guild is already at the maximum level."

    # modify
    obj_attr_modified = f"{{obj}} {{attr}} has been modified correctly. You paid {ContentMeta.get('modify_cost')}"

    # kick
    player_not_in_own_guild = "player '{name}' is not in your guild."
    player_kicked_successfully = "player '{name}' has been successfully kicked from guild '{guild}'. Note that guild members may take some time to update."
    you_have_been_kicked = "You have been kicked from guild {guild}."

    # donations
    donation_received = f"{{donor}} just donated you {{amm}} {MONEY}!"
    donation_successful = f"You successfully sent {{amm}} {MONEY} to {{rec}}. They are certainly going to be happy :)"
    invalid_money_amount = "The specified amount must be greater than zero!"

    # retiring
    you_retired = "You retire from adventuring for a year."
    you_came_back = f"You ended your retirement, resuming your adventures in the world of {WORLD}."

    # player meeting
    players_meet_in_town = "While in town you meet {name} and you"
    players_meet_on_a_quest = "You stumble upon {name} and you"
    town_actions: List[str] = ContentMeta.get("meeting events.town")
    quest_actions: List[str] = ContentMeta.get("meeting events.zones")
    xp_gain = "You gain {xp} xp"

    # minigames
    how_much_do_you_bet = f"How much {MONEY} do you want to bet? (min: {{min}}, max: {{max}})"
    money_pot_too_low = f"You didn't bet enough money, the minimum buy in is {{amount}} {MONEY}"
    money_pot_too_high = f"You bet too much {MONEY}, the maximum buy in is {{amount}} {MONEY}"
    money_pot_ok = f"You bet {{amount}} {MONEY}, the game can begin."
    invalid_bet = "Invalid bet, try again."
    start_hands_minigame = "A mysterious stranger approaches you, he asks if you want to play 'Hands'. You say yes."
    start_fate_minigame = "A Pilgrim approaches you, making you understand he wants to play Pilgrim's fate. You accept."
    hands_minigame_bet = "What value are you betting? (3 - 18, 10 & 5 excluded)."
    fate_minigame_lose = f"The Pilgrim walks away with your {MONEY}, not making a sound."
    fate_minigame_win = "The Pilgrim just walks away, not making a sound."
    you_win = "You win."
    you_lose = "You lose."
    minigame_played_too_recently = "You played this minigame too recently, wait {seconds} seconds and try again."

    # explain
    invalid_minigame_name = "Minigame name is not valid."

    # spells
    not_enough_power = "You don't have enough stored power to cast this spell."

    # errors
    no_character_yet = "You haven't made a character yet!"
    named_object_not_exist = "{obj} with name {name} does not exist."
    name_object_already_exists = "{obj} with name {name} already exists, give your {obj} a different name (names are case sensitive)"
    __must_not_contain = "must not contain new lines & the following characters: \\_, \\*, \\`, \\[, ], ~"
    player_name_validation_error = "Player names must only be 4 to 20 characters long, must not contain spaces and " + __must_not_contain
    guild_name_validation_error = "Guild names must only be 2 to 30 characters long, must not contain spaces and " + __must_not_contain
    description_validation_error = "Descriptions must only be 10 to 300 characters long and " + __must_not_contain
    zone_number_error = "Zone number must be a positive integer number."
    zone_does_not_exist = "The zone does not exist!"
    yes_no_error = "You must send only either 'y' (yes) or 'n' (no)!"
