from otree.api import *
import random
import json
import datetime

doc = """
Digital Payment Experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'digital_payment_practice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # Daftar produk pasar
    PRODUK_TRADISIONAL = [
        {"nama": "Tepung Terigu", "harga": 10000, "deskripsi": "Tepung Terigu per Kg", "satuan": "kg",
         "gambar": "tepung.jpg"},
        {"nama": "Bawang Putih", "harga": 34000, "deskripsi": "Bawang Putih per Kg", "satuan": "kg",
         "gambar": "bawangputih.jpg"},
        {"nama": "Cabe Merah", "harga": 60000, "deskripsi": "Cabe Merah segar per Kg", "satuan": "kg",
         "gambar": "cabemerah.jpg"},
        {"nama": "Santan Kelapa", "harga": 15000, "deskripsi": "Santan Kelapa segar per Kg", "satuan": "bungkus",
         "gambar": "santan.png"},
        {"nama": "Garam Halus", "harga": 5000, "deskripsi": "Garam Halus per bungkus 500gr", "satuan": "bungkus",
         "gambar": "garam.jpg"},
        {"nama": "Tahu", "harga": 7000, "deskripsi": "Tahu Putih per potong", "satuan": "potong", "gambar": "tahu.jpg"},
        {"nama": "Tempe", "harga": 8000, "deskripsi": "Tempe per papan", "satuan": "papan", "gambar": "tempe.jpg"},
        {"nama": "Beras Medium", "harga": 14000, "deskripsi": "Beras Medium per Kg", "satuan": "kg",
         "gambar": "beras.jpg"},
        {"nama": "Telur Ayam Ras", "harga": 28000, "deskripsi": "Telur Ayam Ras per Kg", "satuan": "kg",
         "gambar": "telur.jpg"},
        {"nama": "Ayam Potong", "harga": 42000, "deskripsi": "Ayam Potong segar per Kg", "satuan": "kg",
         "gambar": "ayam.png"},
        {"nama": "Kentang", "harga": 15000, "deskripsi": "Kentang per Kg", "satuan": "kg", "gambar": "kentang.jpg"},
        {"nama": "Minyak Goreng Curah", "harga": 18000, "deskripsi": "Minyak Goreng Curah per Liter", "satuan": "liter",
         "gambar": "minyak.jpg"},
        {"nama": "Kerudung/Jilbab Polos", "harga": 20000, "deskripsi": "Kerudung/Jilbab Polos", "satuan": "pcs",
         "gambar": "kerudung.jpg"},
        {"nama": "Kemeja Kerja", "harga": 75000, "deskripsi": "Kemeja kerja per pcs", "satuan": "pcs",
         "gambar": "kemeja.jpg"},
        {"nama": "Kaos T-Shirt", "harga": 50000, "deskripsi": "Kaos T-Shirt per pcs", "satuan": "pcs",
         "gambar": "kaos.jpg"},
    ]

    PRODUK_DIGITAL = [
        {"nama": "Case HP", "harga": 12500, "deskripsi": "Case HP menarik & fungsional", "satuan": "pcs",
         "gambar": "Case HP-Digital-12500.jpg"},
        {"nama": "Celana Jeans Pria", "harga": 75000, "deskripsi": "Celana Jeans pilihan cocok untuk pria", "satuan":
            "pcs", "gambar": "Celana Jins Pria-Digital-75000.jpeg"},
        {"nama": "Cincin Safir", "harga": 55000, "deskripsi": "Cincin Safir dibuat dari bahan berkualitas tinggi",
         "satuan": "pcs", "gambar": "Cincin Safir-Digital-55000.jpg"},
        {"nama": "Dompet Pria", "harga": 45000, "deskripsi": "Dompet elegan untuk pria", "satuan": "pcs",
         "gambar": "Dompet Pria-Digital-45000.jpeg"},
        {"nama": "Dompet Wanita", "harga": 30000, "deskripsi": "Dompet elegan untuk wanita", "satuan": "pcs",
         "gambar": "Dompet Wanita-Digital-30000.jpeg"},
        {"nama": "Jaket ", "harga": 65000, "deskripsi": "Tampil stylish dengan Jaket berbahan kualitas tinggi",
         "satuan": "pcs", "gambar": "jaket-Digital-65000.jpg"},
        {"nama": "Jam Tangan Unisex", "harga": 60000, "deskripsi": "Jam Tangan elegan dapat dipakai pria maupun wanita",
         "satuan": "pcs", "gambar": "Jam Tangan Unisex-Digital-60000.jpeg"},
        {"nama": "Kacamata Hitam", "harga": 45000, "deskripsi": "Kacamata Hitam tampil menawan", "satuan": "pcs",
         "gambar": "Kacamata Hitam-Digital-45000.jpeg"},
        {"nama": "Paket Skin Care", "harga": 60000, "deskripsi": "All in One Skin Care", "satuan": "pcs",
         "gambar": "Paket Skin Care-Digital-60000.jpeg"},
        {"nama": "Parfum 35ml", "harga": 30000, "deskripsi": "Parfum wangi tahan lama", "satuan": "pcs",
         "gambar": "Parfum 35ml-Digital-30000.jpeg"},
        {"nama": "Pashmina", "harga": 20000, "deskripsi": "Tampil menawan dengan Pashmina", "satuan": "pcs",
         "gambar": "Pashmina-Digital-20000.jpeg"},
        {"nama": "Sepatu Lari", "harga": 70000, "deskripsi": "Sepatu berkualitas terbaik", "satuan": "pcs",
         "gambar": "Sepatu Lari-Digital-70000.jpeg"},
        {"nama": "Sepatu Slip Wanita", "harga": 52000, "deskripsi": "Sepatu Slip terbaik untuk wanita", "satuan": "pcs",
         "gambar": "Sepatu Slip Wanita-Digital-52000.jpeg"},
        {"nama": "Tas Ransel", "harga": 40000, "deskripsi": "Tas Ransel murah", "satuan": "pcs",
         "gambar": "Tas Ransel-Digital-40000.jpeg"},
        {"nama": "Tas Selempang Pria", "harga": 55000, "deskripsi": "Tas Selempang murah untuk pria", "satuan": "pcs",
         "gambar": "Tas Selempang Pria-Digital-55000.jpg"},
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
    uang_kehadiran = models.IntegerField(initial=125000)
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
        self.endowment = random.randint(15, 50) * 1000
        acakan = random.randrange(70, 90, 1)
        self.konsumsi_dasar = acakan * round(self.endowment / 100)

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

            peluang = random.random()
            if peluang <= 0.5:
                hasil = int(round(jumlah * 1.25))
                status = 'untung'
                player.total_untung_lowinvest += (hasil - int(jumlah))
            else:
                hasil = int(round(jumlah * 0.75))
                status = 'rugi'
                player.total_rugi_lowinvest += (int(jumlah) - hasil)

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
                    saldo_digital=player.saldo_digital
                )
            }

        elif jenis == "investasi_tinggi":
            jumlah = float(data.get("jumlah", 0))
            menang = data.get("menang", False)

            if menang:
                hasil = int(round(jumlah * 2))
                status = 'untung'
                player.total_untung_highinvest += int(hasil - round(jumlah))
            else:
                hasil = 0
                status = 'rugi'
                player.total_rugi_highinvest += (int(jumlah) - hasil)

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
