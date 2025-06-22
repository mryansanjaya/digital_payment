from otree.api import *

doc = """
Welcome Page
"""


class C(BaseConstants):
    NAME_IN_URL = 'welcome_page'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# Welcome & Instruction Page
class Welcome(Page):
    pass


class Instruction1(Page):
    pass


class Instruction2(Page):
    pass


class Instruction3(Page):
    pass


class Illustration(Page):
    pass


page_sequence = [Welcome, Instruction1, Instruction2, Instruction3, Illustration]
