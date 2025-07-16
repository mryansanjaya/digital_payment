from otree.api import *
from .models import C, Player
import random
import json


class InfoPage(Page):
    pass


class DynamicPage(Page):
    live_method = 'live_handle'

    def vars_for_template(player: Player):
        produk_riil_list = random.sample(C.PRODUK_TRADISIONAL, 38)
        produk_digital_list = random.sample(C.PRODUK_DIGITAL, 38)
        return {
            'produk_riil_list': produk_riil_list,
            'produk_digital_list': produk_digital_list,
        }

    def live_handle(player, data):
        jenis = data.get("jenis")

        if jenis == "belanja_riil":
            produk_riil = data.get("produk_terpilih", [])
            total = data.get("total_belanja", 0)

            if total > 100000:
                return {player.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            history = json.loads(player.history_riil or "[]")
            history.append({
                "produk": produk_riil,
                "total": total,
                "round_number": player.round_number
            })
            player.history_riil = json.dumps(history)

            return {player.id_in_group: dict(status="success", message="Belanja pasar riil berhasil disimpan.")}

        elif jenis == "belanja_digital":
            produk_digital = data.get("produk_terpilih", [])
            total = data.get("total_belanja", 0)
            if total > 100000:
                return {player.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            history = json.loads(player.history_digital or "[]")
            history.append({
                "produk": produk_digital,
                "total": total,
                "round_number": player.round_number
            })

            player.history_digital = json.dumps(history)
            return {player.id_in_group: dict(status="success", message="Belanja pasar digital berhasil disimpan.")}

        elif jenis == "investasi_rendah":
            jumlah = float(data.get("jumlah", 0))

            if jumlah <= 0:
                return {player.id_in_group: dict(status="error", message="Jumlah tidak valid")}

            peluang = random.random()
            if peluang <= 0.75:
                hasil = round(jumlah * 1.25)
                status = 'untung'
            else:
                hasil = round(jumlah * 0.75)
                status = 'rugi'

            history = json.loads(player.history_lowinvest or "[]")
            history.append({
                "jumlah": jumlah,
                "hasil": hasil,
                "status": status,
                "round_number": player.round_number
            })
            player.history_lowinvest = json.dumps(history)

            return {
                player.id_in_group: {
                    "status": status,
                    "hasil": hasil
                }
            }

        elif data.get("jenis") == "minta_rekap":
            return {
                player.id_in_group: {
                    "selected_products_produk_riil": player.field_maybe_none("selected_products_produk_riil"),
                    "total_belanja_riil": player.field_maybe_none("total_belanja_riil"),
                    "selected_products_produk_digital": player.field_maybe_none("selected_products_produk_digital"),
                    "total_belanja_digital": player.field_maybe_none("total_belanja_digital"),
                    "lowinvest": player.field_maybe_none("lowinvest"),
                    "hasil_akhir_lowinvest": player.field_maybe_none("hasil_akhir_lowinvest"),
                    "untungrugi_lowinvest": player.field_maybe_none("untungrugi_lowinvest"),
                    "history_riil": player.history_riil,
                    "history_digital": player.history_digital,
                    "history_lowinvest": player.history_lowinvest
                }
            }


page_sequence = [InfoPage, DynamicPage]
