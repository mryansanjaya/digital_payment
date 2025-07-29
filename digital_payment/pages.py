from otree.api import *
from .models import C, Player
import random
import json


class InfoPage(Page):
    def vars_for_template(self):
        self.player.set_saldo_awal()
        return dict(
            formatted_endowment="Rp. {:,}".format(self.player.endowment).replace(",", "."),
            formatted_saldo_tunai="Rp. {:,}".format(self.player.saldo_tunai).replace(",", "."),
            formatted_saldo_digital="Rp. {:,}".format(self.player.saldo_digital).replace(",", "."),
            formatted_uang_kehadiran="Rp. {:,}".format(self.player.uang_kehadiran).replace(",", "."),
            formatted_bantuan="Rp. {:,}".format(self.player.bantuan).replace(",", "."),
            formatted_konsumsi_dasar="Rp. {:,}".format(self.player.konsumsi_dasar).replace(",", "."),
            info_bansos="Dompet Tunai" if self.player.saluran_bantuan == "tunai" else "Dompet Digital"
        )

    def before_next_page(self):
        self.player.final_saldo_awal()


class DynamicPage(Page):
    live_method = 'live_handle'

    def vars_for_template(self):
        produk_riil_list = random.sample(C.PRODUK_TRADISIONAL, 38)
        produk_digital_list = random.sample(C.PRODUK_DIGITAL, 38)
        player = self.player

        return {
            'produk_riil_list': produk_riil_list,
            'produk_digital_list': produk_digital_list,
            'formatted_endowment': "Rp. {:,}".format(player.endowment).replace(",", "."),
            'formatted_saldo_tunai': "Rp. {:,}".format(player.saldo_tunai).replace(",", "."),
            'formatted_saldo_digital': "Rp. {:,}".format(player.saldo_digital).replace(",", "."),
            'formatted_uang_kehadiran': "Rp. {:,}".format(player.uang_kehadiran).replace(",", "."),
            'formatted_bantuan': "Rp. {:,}".format(player.bantuan).replace(",", "."),
            'formatted_konsumsi_dasar': "Rp. {:,}".format(player.konsumsi_dasar).replace(",", "."),
        }


class AfterRound(Page):
    def vars_for_template(player):
        return dict(
            next_round_number=player.round_number + 1
        )


page_sequence = [InfoPage, DynamicPage, AfterRound]
