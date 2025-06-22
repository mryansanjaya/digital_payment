from otree.api import *
import random

doc = """
Platform Investasi Risiko Rendah
"""


class C(BaseConstants):
    NAME_IN_URL = 'low_risk_investment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MODAL_AWAL = 100000  # modal tetap


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    investasi = models.CurrencyField(label="Berapa rupiah yang ingin Anda investasikan?", min=0)
    hasil_akhir = models.CurrencyField()
    status = models.StringField()  # UNTUNG atau RUGI


class Investment(Page):
    form_model = 'player'
    form_fields = ['investasi']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        investasi = player.investasi

        # Simulasi hasil acak: 70% untung, 30% rugi
        is_untung = random.random() < 0.7
        if is_untung:
            hasil = investasi * 1.2  # naik 20%
            player.status = "UNTUNG"
        else:
            hasil = investasi * 0.8  # turun 20%
            player.status = "RUGI"

        player.hasil_akhir = hasil


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            status=player.status,
            hasil=int(player.hasil_akhir)
        )


page_sequence = [Investment, Results]
