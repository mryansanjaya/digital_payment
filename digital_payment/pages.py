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

        # Kalau ini ronde pertama, set uang kehadiran awal
        if self.round_number == 1:
            self.player.participant.vars['uang_kehadiran'] = 125000  # contoh nilai awal
            self.player.uang_kehadiran = self.player.participant.vars['uang_kehadiran']
        else:
            # Kalau bukan ronde pertama, ambil dari ronde sebelumnya
            self.player.participant.vars['uang_kehadiran'] = self.player.in_round(self.round_number - 1).uang_kehadiran
            self.player.uang_kehadiran = self.player.participant.vars['uang_kehadiran']

        # Simpan juga ke player supaya bisa ditampilkan di HTML
        self.player.uang_kehadiran = self.player.participant.vars['uang_kehadiran']

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
            'formatted_sisa_uang': "Rp. {:,}".format(self.player.sisa_uang).replace(",", "."),
            'formatted_final_payment': "Rp. {:,}".format(self.player.final_payment).replace(",", ".")
        }

    def before_next_page(self):
        if self.player.sisa_uang < self.player.konsumsi_dasar:
            self.player.denda_penalty = self.player.sisa_uang - self.player.konsumsi_dasar
            self.player.sisa_uang = 0
            self.player.uang_kehadiran += self.player.denda_penalty
        else:
            self.player.denda_penalty = 0
            self.player.sisa_uang -= self.player.konsumsi_dasar

        player = self.player
        participant = player.participant

        if player.round_number == C.NUM_ROUNDS:
            selected_round = random.randint(1, C.NUM_ROUNDS)
            player_in_selected_round = player.in_round(selected_round)

            participant.vars['selected_round'] = selected_round
            participant.vars['final_payment'] = player_in_selected_round.final_payment


class AfterRound(Page):
    def vars_for_template(self):
        return {
            'next_round_number': self.player.round_number + 1,
            'formatted_endowment': "Rp. {:,}".format(self.player.endowment).replace(",", "."),
            'formatted_saldo_tunai': "Rp. {:,}".format(self.player.saldo_tunai).replace(",", "."),
            'formatted_saldo_digital': "Rp. {:,}".format(self.player.saldo_digital).replace(",", "."),
            'formatted_bantuan': "Rp. {:,}".format(self.player.bantuan).replace(",", "."),
            'formatted_konsumsi_dasar': "Rp. {:,}".format(self.player.konsumsi_dasar).replace(",", "."),
            'formatted_total_pasar_riil': "Rp. {:,}".format(self.player.total_belanja_riil).replace(
                ",", "."),
            'formatted_total_pasar_digital': "Rp. {:,}".format(self.player.total_belanja_digital).replace(
                ",", "."),
            'formatted_total_untung_investasi_rendah': "Rp. {:,}".format(self.player.total_untung_lowinvest).replace(
                ",", "."),
            'formatted_total_rugi_investasi_rendah': "Rp. {:,}".format(self.player.total_rugi_lowinvest).replace(
                ",", "."),
            'formatted_total_untung_investasi_tinggi': "Rp. {:,}".format(self.player.total_untung_highinvest).replace(
                ",", "."),
            'formatted_total_rugi_investasi_tinggi': "Rp. {:,}".format(self.player.total_rugi_highinvest).replace(
                ",", "."),
            'formatted_sisa_uang': "Rp. {:,}".format(self.player.sisa_uang).replace(",", "."),
            'formatted_final_payment': "Rp. {:,}".format(self.player.final_payment).replace(",", "."),
            'formatted_denda': "Rp. {:,}".format(self.player.denda_penalty).replace(",", ".")
        }


class AfterExperiment(Page):
    def is_displayed(self):
        return self.player.round_number == C.NUM_ROUNDS

    def before_next_page(self):
        # Ambil uang kehadiran dari ronde terakhir
        last_round = self.player.in_round(C.NUM_ROUNDS)
        self.participant.vars["uang_kehadiran"] = last_round.uang_kehadiran


page_sequence = [BeforeRealExperiment, InfoPage, DynamicPage, AfterRound, AfterExperiment]
