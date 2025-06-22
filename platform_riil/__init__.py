from otree.api import *
import random

doc = """
Platform Riil
"""


class C(BaseConstants):
    NAME_IN_URL = 'platform_riil'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

# Daftar produk pasar
    PRODUK_LIST = [
        {"nama": "Beras", "harga": 12000, "deskripsi": "Beras medium per kg"},
        {"nama": "Cabe Merah", "harga": 40000, "deskripsi": "Cabe merah segar per kg"},
        {"nama": "Telur Ayam", "harga": 25000, "deskripsi": "1 kg telur ayam ras"},
        {"nama": "Ikan Lele", "harga": 30000, "deskripsi": "1 kg ikan lele segar"},
        {"nama": "Sayur Bayam", "harga": 5000, "deskripsi": "1 ikat bayam segar"},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_products = models.LongStringField(blank=True)
    total_belanja = models.CurrencyField(initial=0)


class PlatformRiil(Page):
    form_model = 'player'
    form_fields = ['selected_products']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(produk_list=C.PRODUK_LIST)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        selected_indexes = player.selected_products
        total = 0
        for i in selected_indexes:
            total += C.PRODUK_LIST[i]['harga']
        player.total_belanja = total


page_sequence = [PlatformRiil]
