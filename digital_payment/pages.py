from otree.api import *
from .models import C, Player
import random
import json


class DynamicPage(Page):
    live_method = 'live_handle'

    def vars_for_template(player):
        produk_riil_list = random.sample(C.PRODUK_TRADISIONAL, 38)
        produk_digital_list = random.sample(C.PRODUK_DIGITAL, 38)
        return {
            'produk_riil_list': produk_riil_list,
            'produk_digital_list': produk_digital_list,
        }

    def live_handle(self, data):
        player = self.player
        jenis = data.get("jenis")

        if jenis == "belanja_riil":
            produk = data.get("produk_terpilih", [])
            total = data.get("total_belanja", 0)

            if total > 100000:
                return {player.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            player.selected_products_produk_riil = json.dumps(produk)
            player.total_belanja_riil = total

            return {player.id_in_group: dict(status="success", message="Belanja pasar riil berhasil disimpan.")}

        elif jenis == "digital":
            produk_index = data.get("produk_terpilih", [])
            total = data.get("total", 0)

            if total > 100000:
                return {player.id_in_group: dict(status="error", message="Total belanja digital melebihi saldo.")}

            selected_names = [C.PRODUK_DIGITAL[i]['nama'] for i in produk_index]
            player.selected_products_produk_digital = json.dumps(selected_names)
            player.total_harga_digital = total

            return {player.id_in_group: dict(status="success", message="Belanja digital berhasil disimpan.")}


page_sequence = [DynamicPage]