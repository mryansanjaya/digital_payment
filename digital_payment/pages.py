from otree.api import *
from .models import C, Player
import random
import json


class BeforeRealExperiment(Page):
    def is_displayed(self):
        return self.player.round_number == 1


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

    # def js_vars(self):
    #     # Acak hasil 5 kolom × 3 baris
    #
    #     result = [[random.choice(C.SLOT_ITEMS) for _ in range(3)] for _ in range(5)]
    #     # Tentukan menang (30% peluang)
    #     is_win = random.randint(1, 100) <= 80
    #     if is_win:
    #         win_symbol = random.choice(C.SLOT_ITEMS)
    #         for i in range(2):  # Kolom 0, 1, 2 — baris tengah
    #             result[i][1] = win_symbol
    #
    #     return dict(
    #         result=result,
    #         is_win=is_win
    #     )

    def vars_for_template(self):
        produk_riil_list = random.sample(C.PRODUK_TRADISIONAL, 15)
        produk_digital_list = random.sample(C.PRODUK_DIGITAL, 15)
        player = self.player

        self.player.hitung_utilitas()

        return {
            'produk_riil_list': produk_riil_list,
            'produk_digital_list': produk_digital_list,
            'formatted_endowment': "Rp. {:,}".format(player.endowment).replace(",", "."),
            'formatted_saldo_tunai': "Rp. {:,}".format(player.saldo_tunai).replace(",", "."),
            'formatted_saldo_digital': "Rp. {:,}".format(player.saldo_digital).replace(",", "."),
            'formatted_bantuan': "Rp. {:,}".format(self.player.bantuan).replace(",", "."),
            'formatted_konsumsi_dasar': "Rp. {:,}".format(self.player.konsumsi_dasar).replace(",", "."),
            'formatted_total_pasar': "Rp. {:,}".format(self.player.total_pasar_all).replace(",", "."),
            'formatted_total_investasi': "Rp. {:,}".format(self.player.total_invest_all).replace(",", "."),
            'formatted_utilitas_belanja': "Rp. {:,}".format(self.player.utilitas_belanja).replace(",", "."),
            'formatted_sisa_uang': "Rp. {:,}".format(self.player.sisa_uang).replace(",", "."),
            'formatted_final_payment': "Rp. {:,}".format(self.player.final_payment).replace(",", ".")
        }

    def before_next_page(self):
        player = self.player
        participant = player.participant

        if player.round_number == C.NUM_ROUNDS:
            selected_round = random.randint(1, C.NUM_ROUNDS)
            player_in_selected_round = player.in_round(selected_round)

            participant.vars['selected_round'] = selected_round
            participant.vars['final_payment'] = player_in_selected_round.final_payment
            participant.vars['uang_kehadiran'] = player_in_selected_round.uang_kehadiran


class AfterRound(Page):
    def vars_for_template(self):
        return {
            'next_round_number': self.player.round_number + 1,
            'formatted_endowment': "Rp. {:,}".format(self.player.endowment).replace(",", "."),
            'formatted_saldo_tunai': "Rp. {:,}".format(self.player.saldo_tunai).replace(",", "."),
            'formatted_saldo_digital': "Rp. {:,}".format(self.player.saldo_digital).replace(",", "."),
            'formatted_bantuan': "Rp. {:,}".format(self.player.bantuan).replace(",", "."),
            'formatted_konsumsi_dasar': "Rp. {:,}".format(self.player.konsumsi_dasar).replace(",", "."),
            'formatted_total_pasar': "Rp. {:,}".format(self.player.total_pasar_all).replace(",", "."),
            'formatted_total_investasi': "Rp. {:,}".format(self.player.total_invest_all).replace(",", "."),
            'formatted_utilitas_belanja': "Rp. {:,}".format(self.player.utilitas_belanja).replace(",", "."),
            'formatted_sisa_uang': "Rp. {:,}".format(self.player.sisa_uang).replace(",", "."),
            'formatted_final_payment': "Rp. {:,}".format(self.player.final_payment).replace(",", ".")
        }


class AfterExperiment(Page):
    def is_displayed(self):
        return self.player.round_number == C.NUM_ROUNDS


page_sequence = [BeforeRealExperiment, InfoPage, DynamicPage, AfterRound, AfterExperiment]
