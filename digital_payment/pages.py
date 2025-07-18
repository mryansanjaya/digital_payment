from otree.api import *
from .models import C, Player
import random
import json


class InfoPage(Page):
    pass


class DynamicPage(Page):
    live_method = 'live_handle'

    def vars_for_template(player: Player):
        produk_riil_list = random.sample(C.PRODUK_TRADISIONAL, 38)
        produk_digital_list = random.sample(C.PRODUK_DIGITAL, 38)
        return {
            'produk_riil_list': produk_riil_list,
            'produk_digital_list': produk_digital_list,
        }


class AfterRound(Page):
    def vars_for_template(player):
        return dict(
            next_round_number=player.round_number + 1
        )


page_sequence = [InfoPage, DynamicPage, AfterRound]
