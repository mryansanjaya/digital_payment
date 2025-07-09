from otree.api import *
from .models import C, Player
import random
import json


class DynamicPage(Page):
    live_method = 'live_handle'

    def vars_for_template(player: Player):
        produk_riil_list = random.sample(C.PRODUK_TRADISIONAL, 38)
        produk_digital_list = random.sample(C.PRODUK_DIGITAL, 38)
        return {
            'produk_riil_list': produk_riil_list,
            'produk_digital_list': produk_digital_list,
        }

    def live_handle(player: Player, data):
        jenis = data.get("jenis")

        if jenis == "belanja_riil":
            produk_riil = data.get("produk_terpilih", [])
            total = data.get("total_belanja", 0)

            if total > 100000:
                return {player.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            player.selected_products_produk_riil = json.dumps(produk_riil)
            player.total_belanja_riil = total

            return {player.id_in_group: dict(status="success", message="Belanja pasar riil berhasil disimpan.")}

        elif jenis == "belanja_digital":
            produk_digital = data.get("produk_terpilih", [])
            total = data.get("total_belanja", 0)

            if total > 100000:
                return {player.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            player.selected_products_produk_digital = json.dumps(produk_digital)
            player.total_belanja_digital = total

            return {player.id_in_group: dict(status="success", message="Belanja pasar riil berhasil disimpan.")}


page_sequence = [DynamicPage]