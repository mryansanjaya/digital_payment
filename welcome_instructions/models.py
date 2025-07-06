from otree.api import *

doc = """
Welcome to Digital Payment Experiment 
"""


class Constants(BaseConstants):
    name_in_url = 'welcome_instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
