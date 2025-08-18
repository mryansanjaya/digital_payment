from otree.api import *
import random
import json
import datetime
import math

doc = """
Digital Payment Experiment - Practice Session
"""


class C(BaseConstants):
    NAME_IN_URL = 'digital_payment_practice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Daftar produk pasar
    PRODUK_TRADISIONAL = [
        {"nama": "Bon Cabe Lv 15", "harga": 12000, "deskripsi": "Bon Cabe 45 gr level kepedasan 15", "satuan": "pcs",
         "gambar": "Bon Cabe 45 gr Lv 15 - 12000.jpg"},
        {"nama": "Bumbu Pecel", "harga": 10000, "deskripsi": "Bumbu Pecel berat 100 gr", "satuan": "pcs",
         "gambar": "Bumbu Pecel 100gr - 10000.jpg"},
        {"nama": "Deterjen Bubuk", "harga": 9000, "deskripsi": "Deterjen Bubuk 470 gr untuk cuci baju",
         "satuan": "pack", "gambar": "Deterjen Bubuk 470 gr - 9000.jpg"},
        {"nama": "Ikan Kembung Banjar", "harga": 20000, "deskripsi": "Ikan Kembung Banjar segar 500 gr per ekor",
         "satuan": "ekor", "gambar": "Ikan Kembung Banjar 500gr - 20000.jpeg"},
        {"nama": "Kaos Oblong", "harga": 20000, "deskripsi": "Kaos Oblong kualitas terbaik", "satuan": "pcs",
         "gambar": "kaos Oblong - 20000.jpg"},
        {"nama": "Minyak Goreng Minyakita", "harga": 15000, "deskripsi": "Minyak Goreng Minyakita per Liter",
         "satuan": "liter", "gambar": "Minyak Goreng Minyakita - 15000.jpg"},
        {"nama": "Pasta Gigi", "harga": 13000, "deskripsi": "Pasta Gigi 190 gr", "satuan": "pcs",
         "gambar": "Pasta Gigi 190 gr - 13000.jpg"},
        {"nama": "Roti Krim Mocha", "harga": 5000, "deskripsi": "Roti Krim 49 gr rasa Mocha", "satuan": "pcs",
         "gambar": "Roti Krim 49 gr - 5000.jpg"},
        {"nama": "Sabun Cuci Piring", "harga": 9000, "deskripsi": "Sabun Cuci Piring 650 ml", "satuan": "pcs",
         "gambar": "Sabun Cuci Piring 650 ml - 9000.jpg"},
        {"nama": "Sabun Mandi Batang", "harga": 5000, "deskripsi": "Sabun Batang 80 gr untuk keperluan mandi",
         "satuan": "pcs", "gambar": "Sabun Mandi Batang 80 gr - 5000.jpg"},
        {"nama": "Santan Kelapa", "harga": 7000, "deskripsi": "Santan Kelapa 65 ml untuk memasak", "satuan": "pcs",
         "gambar": "Santan Kelapa 65 ml - 7000.jpg"},
        {"nama": "Sarden Extra Pedas", "harga": 11000, "deskripsi": "Sarden Extra Pedas 155 gr makanan cepat saji",
         "satuan": "kaleng", "gambar": "Sarden Extra Pedas 155gr - 11000.jpg"},
        {"nama": "Lifebouy Shampoo", "harga": 14000, "deskripsi": "Shampoo Lifebouy 70 ml", "satuan": "botol",
         "gambar": "Shampoo 70 ml - 14000.jpg"},
        {"nama": "Tepung Bumbu Racik", "harga": 6500, "deskripsi": "Tepung Bumbu Racik Serba Guna 210 gr",
         "satuan": "pcs", "gambar": "tepung Bumbu Serba Guna 210 gr - 6500.jpg"},
        {"nama": "Tisu Gulung", "harga": 2500, "deskripsi": "Tisu Gulung Satuan", "satuan": "pcs",
         "gambar": "Tisu Gulung satuan - 2500.jpg"},
    ]

    PRODUK_DIGITAL = [
        {"nama": "Bluetooth Earphone", "harga": 25000, "deskripsi": "Earphone bluetooth TWS", "satuan": "pcs",
         "gambar": "Bluetooth Earphone-Digital-25000.jpeg"},
        {"nama": "Case HP", "harga": 12500, "deskripsi": "Case HP menarik & fungsional", "satuan": "pcs",
         "gambar": "Case HP-Digital-12500.jpg"},
        {"nama": "Celana Pendek Chino", "harga": 18000, "deskripsi": "Celana Chino pilihan cocok untuk pria", "satuan":
            "pcs", "gambar": "Celana Pendek Chino-Digital-18000.jpg"},
        {"nama": "Dompet Pria", "harga": 15000, "deskripsi": "Dompet elegan untuk pria", "satuan": "pcs",
         "gambar": "Dompet Pria Polos-Digital-15000.jpg"},
        {"nama": "Dompet Wanita", "harga": 17500, "deskripsi": "Dompet elegan untuk wanita", "satuan": "pcs",
         "gambar": "Dompet Wanita Croco-Digital-17500.jpeg"},
        {"nama": "Gelang Giok", "harga": 11000, "deskripsi": "gelang Giok dibuat dari bahan berkualitas tinggi",
         "satuan": "pcs", "gambar": "Gelang Giok-Digital-11000.jpeg"},
        {"nama": "Jilbab Kerudung Segiempat", "harga": 8500, "deskripsi": "Tampil stylish dengan Jilbab Kerudung"
                                                                          "berbahan kualitas tinggi",
         "satuan": "pcs", "gambar": "Jilbab Kerudung Segiempat-Digital-8500.jpeg"},
        {"nama": "Kaos Oblong Wanita", "harga": 18500, "deskripsi": "Kaos Oblong untuk wanita", "satuan": "pcs",
         "gambar": "Kaos Oblong Wanita-Digital-18500.jpeg"},
        {"nama": "Mini Figure Naruto", "harga": 24500, "deskripsi": "Mini Figure Naruto terbuat dari bahan Resin"
                                                                    "kualitas tinggi", "satuan": "pcs",
         "gambar": "Mini Figure Naruto-Digital-24500.jpeg"},
        {"nama": "Parfum Pria", "harga": 15000, "deskripsi": "Parfum 30 ml untuk pria wangi tahan lama",
         "satuan": "pcs", "gambar": "Parfum Pria 30ml-Digital-15000.jpeg"},
        {"nama": "Pashmina", "harga": 20000, "deskripsi": "Tampil menawan dengan Pashmina", "satuan": "pcs",
         "gambar": "Pashmina-Digital-20000.jpeg"},
        {"nama": "Sandal Gunung", "harga": 13000, "deskripsi": "Sandal Gunung berkualitas terbaik", "satuan": "pcs",
         "gambar": "Sandal Gunung-Digital-13000.jpeg"},
        {"nama": "Skin Care Moisturizer", "harga": 18000, "deskripsi": "Skin Care Mosturizer 50 gr untuk mencerahkan"
                                                                       "kulit", "satuan": "pcs",
         "gambar": "Skin Care Moisturizer 50gr-Digital-18000.jpg"},
        {"nama": "Tas Pinggang Pria", "harga": 16000, "deskripsi": "Tas Pinggang murah untuk pria", "satuan": "pcs",
         "gambar": "Tas Pinggang Pria-Digital-16000.jpeg"},
        {"nama": "Topi Sport Klasik", "harga": 16000, "deskripsi": "Olahraga semakin nyaman dengan Topi Sport Klasik",
         "satuan": "pcs", "gambar": "Topi Sport Klasik-Digital-16000.jpeg"},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_payment = models.IntegerField(initial=0, blank=True)
    sisa_uang = models.IntegerField(initial=0, blank=True)
    endowment = models.IntegerField(initial=0)
    saldo_tunai = models.IntegerField(initial=0)
    saldo_digital = models.IntegerField(initial=0)
    bantuan = models.IntegerField(initial=25000)
    saluran_bantuan = models.StringField()
    konsumsi_dasar = models.IntegerField(initial=0)
    denda_penalty = models.IntegerField(initial=0)
    uang_kehadiran = models.IntegerField(initial=0)
    invest_count_total = models.IntegerField(initial=0)
    total_pasar_all = models.IntegerField(initial=0)
    total_invest_all = models.IntegerField(initial=0)

    # Total masing-masing platform
    total_belanja_riil = models.CurrencyField(blank=True, initial=0)
    total_belanja_digital = models.CurrencyField(blank=True, initial=0)
    total_untung_lowinvest = models.CurrencyField(blank=True, initial=0)
    total_rugi_lowinvest = models.CurrencyField(blank=True, initial=0)
    total_untung_highinvest = models.CurrencyField(blank=True, initial=0)
    total_rugi_highinvest = models.CurrencyField(blank=True, initial=0)

    # History Aktivitas Beli & Investasi
    history_riil = models.LongStringField(blank=True, initial='[]')
    history_digital = models.LongStringField(blank=True, initial='[]')
    history_lowinvest = models.LongStringField(blank=True, initial='[]')
    history_highinvest = models.LongStringField(blank=True, initial='[]')
    history_tukar_uang = models.LongStringField(blank=True, initial='[]')

    # Investasi Risiko Rendah
    lowinvest = models.IntegerField(blank=True, initial=None)
    hasil_akhir_lowinvest = models.IntegerField(blank=True, initial=None)
    untungrugi_lowinvest = models.StringField(blank=True)  # UNTUNG atau RUGI

    # Investasi Risiko Rendah
    highinvest = models.CurrencyField(blank=True, initial=None)
    hasil_akhir_highinvest = models.CurrencyField(blank=True, initial=None)
    untungrugi_highinvest = models.StringField(blank=True)  # UNTUNG atau RUGI

    selected_products_produk_riil = models.LongStringField(blank=True)
    selected_products_produk_digital = models.LongStringField(blank=True)

    def set_saldo_awal(self):
        # 1. Acakan Endowment dengan kelipatan 1.000
        acakan_angka_endowment = random.randrange(75, 125, 1) / 100
        hasil_acakan_angka_endowment = acakan_angka_endowment * 50000
        self.endowment = math.ceil(hasil_acakan_angka_endowment / 100) * 100
        acakan_konsumsi_dasar = random.randrange(70, 85, 1) / 100
        hasil_acakan_konsumsi_dasar = acakan_konsumsi_dasar * self.endowment
        self.konsumsi_dasar = math.ceil(hasil_acakan_konsumsi_dasar / 100) * 100

        self.saldo_tunai = self.endowment
        self.saldo_digital = 0

        # 2. Bantuan masuk ke saldo tunai ATAU saldo digital (acak)
        if random.choice(['tunai', 'digital']) == 'tunai':
            self.saldo_tunai += self.bantuan
            self.saluran_bantuan = "tunai"
        else:
            self.saldo_digital += self.bantuan
            self.saluran_bantuan = "digital"

    def final_saldo_awal(self):
        self.endowment
        self.saldo_tunai
        self.saldo_digital
        self.konsumsi_dasar

    def hitung_utilitas(self):
        # Hitung total belanja pasar tradisional
        try:
            history_riil = json.loads(self.history_riil or "[]")
            total_riil = sum(item.get("total", 0) for item in history_riil)
        except Exception:
            total_riil = 0

        # Hitung total belanja pasar digital
        try:
            history_digital = json.loads(self.history_digital or "[]")
            total_digital = sum(item.get("total", 0) for item in history_digital)
        except Exception:
            total_digital = 0

        # Simpan ke field oTree
        self.total_belanja_riil = total_riil
        self.total_belanja_digital = total_digital
        self.total_pasar_all = total_riil + total_digital

        # Hitung total investasi
        history_low = json.loads(self.history_lowinvest or "[]")
        history_high = json.loads(self.history_highinvest or "[]")
        total_low = sum(item.get("jumlah", 0) for item in history_low)
        total_high = sum(item.get("jumlah", 0) for item in history_high)
        self.total_invest_all = total_low + total_high

        # Hitung utilitas konsumsi dasar (selalu 1x)
        utilitas_konsumsi = self.konsumsi_dasar

        # Hitung utilitas belanja: 90% dikali 1, 10% dikali 1.05
        acakan_utilitas = random.randrange(90, 10, -10)
        if acakan_utilitas <= 90:
            utilitas_belanja = self.total_pasar_all
        elif acakan_utilitas <= 10:
            utilitas_belanja = self.total_pasar_all * 1.05

        # Sisa uang = saldo tunai + saldo digital
        self.sisa_uang = (self.saldo_tunai + self.saldo_digital)

        # Denda / Penalty jika Subjek tidak mampu membayar Konsumsi Dasar
        if self.sisa_uang < utilitas_konsumsi:
            self.denda_penalty = self.sisa_uang - utilitas_konsumsi

        # Final Payment adalah total utilitas
        if self.total_pasar_all == 0 and self.total_invest_all == 0:
            self.final_payment = int(self.sisa_uang)
        elif self.total_invest_all == 0:
            self.final_payment = int(self.sisa_uang + utilitas_belanja)
        elif self.total_pasar_all == 0:
            self.final_payment = int(self.sisa_uang + (self.total_untung_lowinvest + self.total_untung_highinvest) -
                                     (self.total_rugi_lowinvest + self.total_rugi_highinvest))
        else:
            self.final_payment = int(self.sisa_uang + (self.total_pasar_all * 1.05) +
                                     (self.total_untung_lowinvest + self.total_untung_highinvest) -
                                     (self.total_rugi_lowinvest + self.total_rugi_highinvest))

    def live_handle(player, data):
        jenis = data.get("jenis")

        if jenis == "belanja_riil":
            produk_riil = data.get("produk_terpilih", [])
            total = data.get("total_belanja", 0)

            if total > player.saldo_tunai:
                return {player.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            player.saldo_tunai -= total

            history = json.loads(player.history_riil or "[]")
            history.append({
                "produk": produk_riil,
                "total": total,
                "round_number": player.round_number
            })
            player.history_riil = json.dumps(history)

            # Hitung dulu utilitas agar semua nilai terisi
            player.hitung_utilitas()

            return {
                player.id_in_group: dict(
                    status="success",
                    message="Pembelian Belanja Berhasil.",
                    saldo_tunai=player.saldo_tunai,
                )
            }

        elif jenis == "belanja_digital":
            produk_digital = data.get("produk_terpilih", [])
            total = data.get("total_belanja", 0)

            if total > player.saldo_digital:
                return {player.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            player.saldo_digital -= total

            history = json.loads(player.history_digital or "[]")
            history.append({
                "produk": produk_digital,
                "total": total,
                "round_number": player.round_number
            })

            player.history_digital = json.dumps(history)

            # Hitung dulu utilitas agar semua nilai terisi
            player.hitung_utilitas()

            return {
                player.id_in_group: dict(
                    status="success",
                    message="Pembelian Belanja Berhasil",
                    saldo_digital=player.saldo_digital,
                )
            }

        elif jenis == "investasi_rendah":
            jumlah = float(data.get("jumlah", 0))

            if jumlah <= 0:
                return {player.id_in_group: dict(status="error", message="Jumlah tidak valid.")}

            if jumlah > player.saldo_digital:
                return {player.id_in_group: dict(status="error", message="Saldo digital tidak cukup.")}

            # 🚀 Tambahan logika: jika sudah >= 15 kali, hentikan
            if player.invest_count_total >= 20:
                return {
                    player.id_in_group: dict(
                        status="kecanduan",
                        message="Anda sudah terlalu sering bermain investasi. "
                                "Sistem menghentikan investasi supaya Anda tidak kecanduan",
                    )
                }

            peluang = random.random()
            if peluang <= 0.5:
                hasil = int(round(jumlah * 1.25))
                status = 'untung'
                player.total_untung_lowinvest += (hasil - int(jumlah))
                player.invest_count_total += 1
            else:
                hasil = int(round(jumlah * 0.75))
                status = 'rugi'
                player.total_rugi_lowinvest += (int(jumlah) - hasil)
                player.invest_count_total += 1

            history = json.loads(player.history_lowinvest or "[]")
            history.append({
                "jumlah": int(jumlah),
                "hasil": hasil,
                "status": status,
                "round_number": player.round_number
            })

            player.history_lowinvest = json.dumps(history)

            # Update saldo digital
            if status == 'untung':
                player.saldo_digital += (hasil - int(jumlah))

            else:
                player.saldo_digital -= (int(jumlah) - hasil)

            # Hitung dulu utilitas agar semua nilai terisi
            player.hitung_utilitas()

            return {
                player.id_in_group: dict(
                    status=status,
                    hasil=hasil,
                    count_invest=player.invest_count_total,
                    saldo_digital=player.saldo_digital
                )
            }

        elif jenis == "investasi_tinggi":
            jumlah = float(data.get("jumlah", 0))
            menang = data.get("menang", False)

            # 🚀 Tambahan logika: jika sudah >= 15 kali, hentikan
            if player.invest_count_total >= 20:
                return {
                    player.id_in_group: dict(
                        status="kecanduan",
                        message="Anda sudah terlalu sering bermain investasi. "
                                "Sistem menghentikan investasi supaya Anda tidak kecanduan",
                    )
                }

            elif menang:
                hasil = int(round(jumlah * 2))
                status = 'untung'
                player.total_untung_highinvest += int(hasil - round(jumlah))
                player.invest_count_total += 1

            else:
                hasil = 0
                status = 'rugi'
                player.total_rugi_highinvest += (int(jumlah) - hasil)
                player.invest_count_total += 1

            # Simpan ke history
            history = json.loads(player.history_highinvest or "[]")
            history.append({
                "jumlah": int(jumlah),
                "hasil": hasil,
                "status": status,
                "round_number": player.round_number

            })

            player.history_highinvest = json.dumps(history)

            # Update saldo digital
            if status == 'untung':
                player.saldo_digital += int(hasil)
            else:
                player.saldo_digital -= int(jumlah)

            player.hitung_utilitas()
            return {
                player.id_in_group: dict(
                    status=status,
                    hasil=hasil,
                    jumlah=jumlah,
                    saldo_digital=player.saldo_digital
                )
            }

        elif jenis == "minta_rekap":
            # Hitung dulu utilitas agar semua nilai terisi
            player.hitung_utilitas()

            return {
                player.id_in_group: {
                    "selected_products_produk_riil": player.field_maybe_none("selected_products_produk_riil"),
                    "total_belanja_riil": player.field_maybe_none("total_belanja_riil"),
                    "selected_products_produk_digital": player.field_maybe_none("selected_products_produk_digital"),
                    "total_belanja_digital": player.field_maybe_none("total_belanja_digital"),

                    "lowinvest": player.field_maybe_none("lowinvest"),
                    "hasil_akhir_lowinvest": player.field_maybe_none("hasil_akhir_lowinvest"),
                    "untungrugi_lowinvest": player.field_maybe_none("untungrugi_lowinvest"),
                    "total_untung_investasi_rendah": player.total_untung_lowinvest,
                    "total_rugi_investasi_rendah": player.total_rugi_highinvest,
                    "total_untung_investasi_tinggi": player.total_untung_highinvest,
                    "total_rugi_investasi_tinggi": player.total_rugi_highinvest,

                    "saldo_tunai": player.field_maybe_none("saldo_tunai"),
                    "saldo_digital": player.field_maybe_none("saldo_digital"),

                    "history_riil": player.history_riil,
                    "history_digital": player.history_digital,
                    "history_lowinvest": player.history_lowinvest,
                    "history_highinvest": player.history_highinvest,
                    "history_tukar_uang": player.history_tukar_uang,

                    # Tambahan variabel utilitas
                    "endowment": player.endowment,
                    "bantuan": player.bantuan,
                    "konsumsi_dasar": player.konsumsi_dasar,
                    "total_pasar_all": player.total_pasar_all,
                    "total_invest_all": player.total_invest_all,
                    "sisa_uang": player.field_maybe_none("sisa_uang"),
                    "final_payment": player.field_maybe_none("final_payment"),
                }
            }

        elif jenis == "tukar_uang":
            # Hitung dulu utilitas agar semua nilai terisi
            player.hitung_utilitas()

            arah = data.get("arah")
            jumlah = int(data.get("jumlah", 0))
            biaya_admin = 1000

            if jumlah <= 0:
                return {player.id_in_group: dict(status="gagal", message="Jumlah tidak valid")}

            history = json.loads(player.history_tukar_uang or "[]")

            if arah == "tunai_ke_digital":
                if player.saldo_tunai < jumlah + biaya_admin:
                    return {player.id_in_group: dict(status="gagal", message="Saldo tunai tidak mencukupi")}
                player.saldo_tunai -= jumlah + biaya_admin
                player.saldo_digital += jumlah

            elif arah == "digital_ke_tunai":
                if player.saldo_digital < jumlah + biaya_admin:
                    return {player.id_in_group: dict(status="gagal", message="Saldo digital tidak mencukupi")}
                player.saldo_digital -= jumlah + biaya_admin
                player.saldo_tunai += jumlah

            else:
                return {player.id_in_group: dict(status="gagal", message="Arah pertukaran tidak valid")}

            history.append({
                "waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "jumlah": jumlah,
                "admin": biaya_admin,
                "arah": arah,
            })
            player.history_tukar_uang = json.dumps(history)

            return {
                player.id_in_group: {
                    "status": "sukses",
                    "history": history,
                    "saldo_tunai": player.saldo_tunai,
                    "saldo_digital": player.saldo_digital
                }
            }
