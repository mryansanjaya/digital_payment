from otree.api import *
import random

doc = """
Platform Digital
"""


class C(BaseConstants):
    NAME_IN_URL = 'platform_digital'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

# Daftar produk pasar
    PRODUK_LIST = [
        {"nama": "Pulpen Standard", "harga": 2500, "deskripsi": "Pulpen tinta hitam, murah dan lancar"},
        {"nama": "Buku Tulis Sidu 38 Lembar", "harga": 3500, "deskripsi": "Buku tulis pelajar ukuran A5"},
        {"nama": "Masker Kain 3 Lapis", "harga": 3000, "deskripsi": "Masker kain bisa dicuci, warna acak"},
        {"nama": "Kabel Data Micro USB 1m", "harga": 7000, "deskripsi": "Kabel data charger universal"},
        {"nama": "Headset Stereo Murah", "harga": 12000, "deskripsi": "Headset kabel untuk HP & laptop"},
        {"nama": "Charger HP 1A KW", "harga": 15000, "deskripsi": "Adaptor charger murah universal"},
        {"nama": "Casing HP Silikon", "harga": 8000, "deskripsi": "Softcase silikon berbagai tipe HP"},
        {"nama": "Gunting Kecil Serbaguna", "harga": 6000, "deskripsi": "Gunting plastik mini untuk rumah"},
        {"nama": "Korek Api Gas", "harga": 2000, "deskripsi": "Korek api isi ulang, warna acak"},
        {"nama": "Stiker Lucu Paket 50pcs", "harga": 9500, "deskripsi": "Stiker waterproof berbagai desain"},
        {"nama": "Lampu LED 5W Putih", "harga": 9000, "deskripsi": "Lampu LED hemat energi"},
        {"nama": "Kaos Oblong Polos", "harga": 17000, "deskripsi": "Kaos polos pria wanita, warna random"},
        {"nama": "Sendok Garpu Stainless", "harga": 8000, "deskripsi": "Set sendok + garpu ekonomis"},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_products = models.LongStringField(blank=True)
    total_belanja = models.CurrencyField(initial=0)


class PlatformDigital(Page):
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


# page_sequence = [Welcome, Instruction1, Instruction2, Instruction3, Illustration]
page_sequence = [PlatformDigital]

