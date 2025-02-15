# -*- coding: utf-8 -*-
"""

@author: nickb
"""

from constants import ACTION_FORWARD, ACTION_SUCK, ACTION_TURN_LEFT, ACTION_TURN_RIGHT
from constants import ACTION_STOP
from constants import WALL, DIRT, CLEAN
from constants import FORWARD

from agents.vacuumagent import VacuumAgent
from random import choice
from agents.agentworldmodel import AgentWorldModel

class BestWorldModelAgent(VacuumAgent):
    def __init__(self, log):
        self.version = "BestWorldModelAgent"
        super().__init__(self.version, log, self.execute)
        self.world_model = AgentWorldModel()
    
    def prep(self, report):
        self.world_model.tell_recon(report)
        
    def execute(self, percept):
        self.pre_update(percept) 
        self.world_model.tell_percepts(percept)
        action = self.choose_action(percept)
        self.world_model.tell_action(action)
        self.post_update(action)
        return action
   
    def choose_action(self, percept):
        action = None
        if self.battery_depleted():
            self.log(f"Battery depleted, score is {self.score()}")
            action = ACTION_STOP          
        else:
            if self.world_model.ask_state_here() == DIRT:
                action = ACTION_SUCK

            elif self.world_model.ask_state_in_direction(FORWARD) != WALL:
                action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT, ACTION_FORWARD, ACTION_FORWARD, ACTION_FORWARD])
                if self.world_model.ask_state_in_direction(FORWARD) == WALL:
                    action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT]) 
                else:
                    action = ACTION_FORWARD  
                    if self.world_model.ask_last_action == ACTION_FORWARD:
                        action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT]) 
                    else:
                        action = ACTION_FORWARD  
           
# SHIT I'M ADDING IN...
            elif self.world_model.ask_state_in_direction(FORWARD) == WALL:
                action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT]) 
                #action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT]) 
#                action = ACTION_FORWARD       
#                action = ACTION_TURN_RIGHT
#                action = ACTION_FORWARD   
#            elif self.world_model.ask_state_here() == CLEAN:
#                action = ACTION_FORWARD  

                #action = ACTION_TURN_LEFT
            elif self.world_model.ask_last_action == ACTION_TURN_RIGHT:
                action = ACTION_FORWARD
                
#            elif self.world_model.ask_state_in_direction(FORWARD) != WALL:
#                action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT, ACTION_FORWARD, ACTION_FORWARD, ACTION_FORWARD])
            elif self.world_model.ask_last_action == ACTION_FORWARD:   
                action = ACTION_TURN_LEFT
            elif self.world_model.ask_last_action == ACTION_TURN_LEFT:
                action = ACTION_TURN_RIGHT
            elif self.world_model.ask_last_action == ACTION_TURN_RIGHT:
                action = ACTION_TURN_LEFT
            else:
                action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT])              
        return action

#####################################################

class BestReactiveAgent(VacuumAgent):
    def __init__(self, log):
        self.version = "BestReactiveAgent"
        super().__init__(self.version, log, self.execute)
    
    def prep(self, report):
        pass
        
    def execute(self, percept):
        self.pre_update(percept) 
        action = self.choose_action(percept)
        self.post_update(action)
        return action
   
    def choose_action(self, percept):
        action = None
        if self.battery_depleted():
            self.log(f"Battery depleted, score is {self.score()}")
            action = ACTION_STOP          
        else:
            dirt_here = percept.attributes['dirt']
            if dirt_here:
                action = ACTION_SUCK
            else:
                bump_here = percept.attributes['bump']
                if bump_here:
                    action = choice([ACTION_TURN_LEFT, ACTION_TURN_RIGHT])
                else:
                    action = ACTION_FORWARD
        return action