from otree.api import *
import random
import json

doc = """
Digital Payment Experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'digital_payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3

# Daftar produk pasar
    PRODUK_TRADISIONAL = [
        {"nama": "Beras", "harga": 12000, "deskripsi": "Beras medium per kg", "satuan": "kg"},
        {"nama": "Cabe Merah", "harga": 40000, "deskripsi": "Cabe merah segar per kg", "satuan": "kg"},
        {"nama": "Telur Ayam", "harga": 25000, "deskripsi": "1 kg telur ayam ras", "satuan": "kg"},
        {"nama": "Ikan Lele", "harga": 30000, "deskripsi": "1 kg ikan lele segar", "satuan": "kg"},
        {"nama": "Sayur Bayam", "harga": 5000, "deskripsi": "1 ikat bayam segar", "satuan": "ikat"},
        {"nama": "Bawang Merah", "harga": 28000, "deskripsi": "1 kg bawang merah", "satuan": "kg"},
        {"nama": "Bawang Putih", "harga": 27000, "deskripsi": "1 kg bawang putih", "satuan": "kg"},
        {"nama": "Minyak Goreng Curah", "harga": 16000, "deskripsi": "1 liter", "satuan": "liter"},
        {"nama": "Gula Pasir", "harga": 14000, "deskripsi": "1 kg", "satuan": "kg"},
        {"nama": "Kacang Hijau", "harga": 18000, "deskripsi": "1 kg", "satuan": "kg"},
        {"nama": "Tempe", "harga": 4000, "deskripsi": "1 papan tempe", "satuan": "papan"},
        {"nama": "Tahu", "harga": 3000, "deskripsi": "1 potong tahu putih", "satuan": "potong"},
        {"nama": "Ayam Potong", "harga": 35000, "deskripsi": "1 kg ayam segar", "satuan": "kg"},
        {"nama": "Ikan Bandeng", "harga": 38000, "deskripsi": "1 kg bandeng", "satuan": "kg"},
        {"nama": "Daging Sapi", "harga": 110000, "deskripsi": "1 kg daging sapi segar", "satuan": "kg"},
        {"nama": "Santan Kelapa", "harga": 7000, "deskripsi": "1 bungkus santan segar", "satuan": "bungkus"},
        {"nama": "Lombok Rawit", "harga": 45000, "deskripsi": "1 kg", "satuan": "kg"},
        {"nama": "Kangkung", "harga": 4000, "deskripsi": "1 ikat kangkung segar", "satuan": "ikat"},
        {"nama": "Tomat", "harga": 8000, "deskripsi": "1 kg tomat merah", "satuan": "kg"},
        {"nama": "Wortel", "harga": 10000, "deskripsi": "1 kg wortel", "satuan": "kg"},
        {"nama": "Kentang", "harga": 11000, "deskripsi": "1 kg kentang", "satuan": "kg"},
        {"nama": "Timun", "harga": 7000, "deskripsi": "1 kg timun", "satuan": "kg"},
        {"nama": "Kubis", "harga": 6000, "deskripsi": "1 kepala kubis", "satuan": "kepala"},
        {"nama": "Terong", "harga": 9000, "deskripsi": "1 kg terong", "satuan": "kg"},
        {"nama": "Pepaya", "harga": 10000, "deskripsi": "1 buah pepaya sedang", "satuan": "buah"},
        {"nama": "Pisang Raja", "harga": 15000, "deskripsi": "1 sisir pisang", "satuan": "sisir"},
        {"nama": "Jeruk", "harga": 20000, "deskripsi": "1 kg jeruk manis", "satuan": "kg"},
        {"nama": "Apel Lokal", "harga": 25000, "deskripsi": "1 kg apel", "satuan": "kg"},
        {"nama": "Mangga", "harga": 22000, "deskripsi": "1 kg mangga harum manis", "satuan": "kg"},
        {"nama": "Jambu Merah", "harga": 18000, "deskripsi": "1 kg jambu biji", "satuan": "kg"},
        {"nama": "Daun Bawang", "harga": 3000, "deskripsi": "1 ikat kecil", "satuan": "ikat"},
        {"nama": "Seledri", "harga": 3000, "deskripsi": "1 ikat kecil", "satuan": "ikat"},
        {"nama": "Kelapa Parut", "harga": 7000, "deskripsi": "1 butir diparut", "satuan": "butir"},
        {"nama": "Tepung Terigu", "harga": 9000, "deskripsi": "1 kg", "satuan": "kg"},
        {"nama": "Tepung Beras", "harga": 8500, "deskripsi": "1 kg", "satuan": "kg"},
        {"nama": "Daun Pisang", "harga": 3000, "deskripsi": "1 lembar besar", "satuan": "lembar"},
        {"nama": "Ikan Asin", "harga": 15000, "deskripsi": "1 ikat ikan asin", "satuan": "ikat"},
        {"nama": "Kerupuk Udang", "harga": 12000, "deskripsi": "1 bungkus kerupuk mentah", "satuan": "bungkus"},
        {"nama": "Garam Halus", "harga": 3000, "deskripsi": "1 bungkus 500g", "satuan": "bungkus"},
        {"nama": "Kecap Manis Lokal", "harga": 7000, "deskripsi": "Isi 150ml", "satuan": "botol"},
    ]

    PRODUK_DIGITAL = [
        {"nama": "Pulpen Gel Murah", "harga": 2500, "deskripsi": "Pulpen warna-warni isi ulang", "satuan": "pcs"},
        {"nama": "Notebook A5", "harga": 3500, "deskripsi": "Buku catatan 60 lembar", "satuan": "pcs"},
        {"nama": "Headset Kabel Murah", "harga": 12000, "deskripsi": "Headset stereo universal", "satuan": "pcs"},
        {"nama": "Casing HP Silikon", "harga": 8000, "deskripsi": "Softcase universal berbagai tipe", "satuan": "pcs"},
        {"nama": "Charger HP 1A", "harga": 15000, "deskripsi": "Adaptor charger fast charge palsu", "satuan": "pcs"},
        {"nama": "Stiker Dekorasi 50pcs", "harga": 9500, "deskripsi": "Stiker lucu waterproof", "satuan": "pak"},
        {"nama": "Kabel Data Micro USB", "harga": 7000, "deskripsi": "Kabel 1 meter", "satuan": "pcs"},
        {"nama": "Masker Kain 3 Lapis", "harga": 3000, "deskripsi": "Masker kain washable", "satuan": "pcs"},
        {"nama": "Tempered Glass", "harga": 10000, "deskripsi": "Pelindung layar HP", "satuan": "pcs"},
        {"nama": "Mouse Pad Mini", "harga": 5000, "deskripsi": "Mousepad polos kecil", "satuan": "pcs"},
        {"nama": "Dompet Koin Kecil", "harga": 7000, "deskripsi": "Dompet receh travel", "satuan": "pcs"},
        {"nama": "Gunting Mini", "harga": 6000, "deskripsi": "Gunting kecil lipat", "satuan": "pcs"},
        {"nama": "Pulpen 6-in-1", "harga": 8500, "deskripsi": "Pulpen multifungsi warna-warni", "satuan": "pcs"},
        {"nama": "Lampu LED USB", "harga": 5000, "deskripsi": "Lampu belajar portabel", "satuan": "pcs"},
        {"nama": "Kipas Mini USB", "harga": 10000, "deskripsi": "Kipas meja colok USB", "satuan": "pcs"},
        {"nama": "Notebook Spiral", "harga": 6000, "deskripsi": "Buku catatan ekonomis", "satuan": "pcs"},
        {"nama": "Sticky Notes", "harga": 3500, "deskripsi": "Kertas memo warna", "satuan": "pak"},
        {"nama": "Gantungan Kunci Akrilik", "harga": 3000, "deskripsi": "Model karakter lucu", "satuan": "pcs"},
        {"nama": "Cermin Mini Lipat", "harga": 7000, "deskripsi": "Cermin saku portable", "satuan": "pcs"},
        {"nama": "Sisir Lipat", "harga": 4000, "deskripsi": "Sisir lipat travel", "satuan": "pcs"},
        {"nama": "Tas Belanja Lipat", "harga": 10000, "deskripsi": "Eco bag serut praktis", "satuan": "pcs"},
        {"nama": "Botol Minum 350ml", "harga": 12000, "deskripsi": "Botol plastik BPA-free", "satuan": "pcs"},
        {"nama": "Tali Sepatu Warna", "harga": 4500, "deskripsi": "1 pasang tali sepatu unik", "satuan": "pasang"},
        {"nama": "Sabun Cuci Muka Sachet", "harga": 2500, "deskripsi": "Isi 10gr", "satuan": "sachet"},
        {"nama": "Penjepit Kertas", "harga": 3000, "deskripsi": "Isi 10 penjepit kecil", "satuan": "pak"},
        {"nama": "Tali Gantungan HP", "harga": 5000, "deskripsi": "Strap lucu untuk handphone", "satuan": "pcs"},
        {"nama": "Kabel Charger iPhone KW", "harga": 15000, "deskripsi": "KW fast charging", "satuan": "pcs"},
        {"nama": "Sendok Lipat Camping", "harga": 8000, "deskripsi": "Sendok portable logam", "satuan": "pcs"},
        {"nama": "Jam Tangan Anak", "harga": 17000, "deskripsi": "Digital murah waterproof", "satuan": "pcs"},
        {"nama": "Tas Selempang Mini", "harga": 17000, "deskripsi": "Tas kecil 1 kompartemen", "satuan": "pcs"},
        {"nama": "Alat Pembersih Kaca HP", "harga": 4000, "deskripsi": "Kain & cairan kecil", "satuan": "pak"},
        {"nama": "Mini Tripod HP", "harga": 14000, "deskripsi": "Tripod kecil lipat", "satuan": "pcs"},
        {"nama": "Tattoo Sticker Temporary", "harga": 3000, "deskripsi": "Tahan air, anak-anak", "satuan": "pcs"},
        {"nama": "Earphone Organizer", "harga": 7000, "deskripsi": "Kotak gulung kabel", "satuan": "pcs"},
        {"nama": "Tempat Pensil Lucu", "harga": 8000, "deskripsi": "Desain karakter kartun", "satuan": "pcs"},
        {"nama": "Kabel Roll Panjang", "harga": 16000, "deskripsi": "Kabel listrik mini roll", "satuan": "pcs"},
        {"nama": "Cermin Meja Kecil", "harga": 9500, "deskripsi": "Kaca meja minimalis", "satuan": "pcs"},
        {"nama": "Kunci Gembok Kecil", "harga": 6000, "deskripsi": "Gembok koper/tas", "satuan": "pcs"},
        {"nama": "Tempat Sabun Portable", "harga": 5000, "deskripsi": "Kotak sabun plastik", "satuan": "pcs"},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_products_produk_riil = models.LongStringField(blank=True)
    total_belanja_riil = models.CurrencyField(blank=True, initial=None)

    selected_products_produk_digital = models.LongStringField(blank=True)
    total_belanja_digital = models.CurrencyField(blank=True, initial=None)

    # Investasi Risiko Rendah
    lowinvest = models.CurrencyField(blank=True, initial=None)
    hasil_akhir_lowinvest = models.CurrencyField(blank=True, initial=None)
    untungrugi_lowinvest = models.StringField(blank=True)  # UNTUNG atau RUGI

    # History Aktivitas Beli & Investasi
    history_riil = models.LongStringField(blank=True, initial='[]')
    history_digital = models.LongStringField(blank=True, initial='[]')
    history_lowinvest = models.LongStringField(blank=True, initial='[]')

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