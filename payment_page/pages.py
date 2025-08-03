from otree.api import *
from .models import C, Player
import random


class PaymentIntro(Page):
    def before_next_page(self):
        player = self.player
        participant = player.participant

        player.final_payment = participant.vars.get('final_payment')
        player.uang_kehadiran = participant.vars.get('uang_kehadiran')
        player.selected_round = participant.vars.get('selected_round')


class PaymentSelection(Page):
    form_model = 'player'
    form_fields = ['kode_peserta']

    def vars_for_template(self):
        return {
            'formatted_final_payment': "Rp. {:,}".format(self.player.final_payment).replace(",", "."),
            'formatted_uang_kehadiran': "Rp. {:,}".format(self.player.uang_kehadiran).replace(",", "."),
            'total_pembayaran':
                "Rp. {:,}".format(self.player.final_payment + self.player.uang_kehadiran).replace(",", ".")
        }

    def before_next_page(self):
        player = self.player
        player.payoff = player.final_payment + player.uang_kehadiran


class PaymentThanks(Page):
    def vars_for_template(self):
        return {
            'formatted_final_payment': "Rp. {:,}".format(self.player.final_payment).replace(",", "."),
            'formatted_uang_kehadiran': "Rp. {:,}".format(self.player.uang_kehadiran).replace(",", "."),
            'total_pembayaran':
                "Rp. {:,}".format(self.player.final_payment + self.player.uang_kehadiran).replace(",", ".")
        }


page_sequence = [
    PaymentIntro,
    PaymentSelection,
    PaymentThanks,
]
