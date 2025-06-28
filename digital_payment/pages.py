from otree.api import *
from .models import C, Player
import random
import json


class DynamicPage(Page):
    form_model = 'player'
    form_fields = ['selected_products_produk_riil', 'selected_products_produk_digital']

    def vars_for_template(player: Player):
        # Hanya acak jika belum ada
        if 'produk_riil_acak' not in player.participant.vars:
            player.participant.vars['produk_riil_acak'] = random.sample(C.PRODUK_TRADISIONAL, 25)

        if 'produk_digital_acak' not in player.participant.vars:
            player.participant.vars['produk_digital_acak'] = random.sample(C.PRODUK_DIGITAL, 25)

        produk_riil = player.participant.vars['produk_riil_acak']
        produk_digital = player.participant.vars['produk_digital_acak']

        return dict(
            produk_riil_list=produk_riil,
            produk_digital_list=produk_digital,
            produk_riil_json=json.dumps(produk_riil),
            produk_digital_json=json.dumps(produk_digital),
        )

    # def before_next_page(player: Player, timeout_happened):
    #     # Pasar Riil
    #     try:
    #         selected_riil = json.loads(player.selected_products_produk_riil or "[]")
    #     except json.JSONDecodeError:
    #         selected_riil = []
    #
    #     produk_riil = player.participant.vars.get('produk_riil_acak', [])
    #     total_riil = sum(produk_riil[i]['harga'] for i in selected_riil if 0 <= i < len(produk_riil))
    #     player.total_belanja_pasar_riil = total_riil
    #
    #     # Pasar Digital
    #     try:
    #         selected_digital = json.loads(player.selected_products_produk_digital or "[]")
    #     except json.JSONDecodeError:
    #         selected_digital = []
    #
    #     produk_digital = player.participant.vars.get('produk_digital_acak', [])
    #     total_digital = sum(produk_digital[i]['harga'] for i in selected_digital if 0 <= i < len(produk_digital))
    #     player.total_belanja_pasar_digital = total_digital


# class PlatformDigital(Page):
#     form_model = 'player'
#     form_fields = ['selected_products_produk_digital', 'back_to_menu']
#
#     def is_displayed(player):
#         return player.participant.vars.get('menu_choice') == 'pasar_digital'
#
#     @staticmethod
#     def vars_for_template(player: Player):
#         produk_acak = random.sample(C.PRODUK_DIGITAL, 25)
#         player.participant.vars['produk_digital_acak'] = produk_acak
#         return dict(produk_list=json.dumps(produk_acak))
#
#     @staticmethod
#     def before_next_page(player: Player, timeout_happened):
#         # ambil dari form langsung
#         is_back = player.back_to_menu
#         if is_back:
#             player.participant.vars['back_to_menu'] = True
#         else:
#             player.participant.vars['back_to_menu'] = False
#
#         # proses belanja kalau bukan kembali
#         if not is_back:
#             selected = json.loads(player.selected_products_produk_digital or "[]")
#             total = sum(C.PRODUK_DIGITAL[i]["harga"] for i in selected)
#             player.total_belanja_pasar_digital = total
#
#
# class LowInvestment(Page):
#     form_model = 'player'
#     form_fields = ['lowinvest', 'back_to_menu']
#
#     def is_displayed(player):
#         return player.participant.vars.get('menu_choice') == 'investasi'
#
#     @staticmethod
#     def before_next_page(player: Player, timeout_happened):
#         # ambil dari form langsung
#         is_back = player.back_to_menu
#         if is_back:
#             player.participant.vars['back_to_menu'] = True
#         else:
#             player.participant.vars['back_to_menu'] = False
#
#         # proses investasi kalau bukan kembali
#         if not is_back:
#             investasi = player.lowinvest
#
#             # Simulasi hasil acak: 70% untung, 30% rugi
#             is_untung = random.random() < 0.7
#             if is_untung:
#                 hasil = investasi * 1.2  # naik 20%
#                 player.untungrugi_lowinvest = "UNTUNG"
#             else:
#                 hasil = investasi * 0.8  # turun 20%
#                 player.untungrugi_lowinvest = "RUGI"
#
#             player.hasil_akhir_lowinvest = hasil
#
#
# class LowResults(Page):
#     def is_displayed(player):
#         return player.participant.vars.get('menu_choice') == 'investasi'
#
#     @staticmethod
#     def vars_for_template(player: Player):
#         return dict(
#             status=player.untungrugi_lowinvest,
#             hasil=int(player.hasil_akhir_lowinvest)
#         )


page_sequence = [DynamicPage]
