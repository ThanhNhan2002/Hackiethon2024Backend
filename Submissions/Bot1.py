# bot code goes here
from Game.Skills import *
from Game.projectiles import *
from ScriptingHelp.usefulFunctions import *
from Game.playerActions import defense_actions, attack_actions, projectile_actions
from Game.gameSettings import HP, LEFTBORDER, RIGHTBORDER, LEFTSTART, RIGHTSTART, PARRYSTUN
import random

# PRIMARY CAN BE: Teleport, Meditate, Dash Attack, Uppercut, One Punch
# SECONDARY CAN BE : Hadoken, Grenade, Boomerang, Bear Trap, Super Saiyan,

# TODO FOR PARTICIPANT: Set primary and secondary skill here
PRIMARY_SKILL = Meditate
SECONDARY_SKILL = Hadoken

#constants, for easier move return
#movements
JUMP = ("move", (0,1))
FORWARD = ("move", (1,0))
BACK = ("move", (-1,0))
JUMP_FORWARD = ("move", (1,1))
JUMP_BACKWARD = ("move", (-1, 1))

# attacks and block
LIGHT = ("light",)
HEAVY = ("heavy",)
BLOCK = ("block",)

PRIMARY = get_skill(PRIMARY_SKILL)
SECONDARY = get_skill(SECONDARY_SKILL)
CANCEL = ("skill_cancel", )

# no move, aka no input
NOMOVE = "NoMove"
# for testing
moves = SECONDARY,
moves_iter = iter(moves)

# TODO FOR PARTICIPANT: WRITE YOUR WINNING BOT
class Script:
    def __init__(self):
        self.primary = PRIMARY_SKILL
        self.secondary = SECONDARY_SKILL
        
    # DO NOT TOUCH
    def init_player_skills(self):
        return self.primary, self.secondary
    
    # MAIN FUNCTION that returns a single move to the game manager
    def get_move(self, player, enemy, player_projectiles, enemy_projectiles):
        action_list = [JUMP, FORWARD, BACK, JUMP_BACKWARD, JUMP_FORWARD, LIGHT, HEAVY, BLOCK, PRIMARY, SECONDARY, CANCEL]
        #print(get_last_move(player))
        distance = abs((get_pos(player)[0] - get_pos(enemy)[0]))
        # print(distance)
        # if distance > 4:
        #     return FORWARD 
        # print(get_last_move(player), get_past_move(player, 1), get_past_move(player, 2))

        # return JUMP


        if not get_secondary_cooldown(player):
            return SECONDARY
        
        # return PRIMARY     
        # if distance > 5:
        #     return FORWARD
        # else:ss
        #     if not get_primary_cooldown(player) and not get_secondary_cooldown(player):
        #         return SECONDARY
        #     elif get_last_move(player)[0] == 'super_saiyan':
        #         return PRIMARY

        
