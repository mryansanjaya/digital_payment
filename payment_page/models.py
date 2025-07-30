from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'payment_page'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Untuk acakan ronde dan final payment
    final_payment = models.IntegerField(initial=0)
    uang_kehadiran = models.IntegerField(initial=0)
    selected_round = models.IntegerField(initial=0)
    kode_peserta = models.StringField()


