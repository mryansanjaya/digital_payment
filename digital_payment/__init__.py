from otree.api import *
import random, json

doc = """
Digital Payment Experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'digital_payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

# Daftar produk pasar
    PRODUK_TRADISIONAL = [
        {"nama": "Beras", "harga": 12000, "deskripsi": "Beras medium per kg"},
        {"nama": "Cabe Merah", "harga": 40000, "deskripsi": "Cabe merah segar per kg"},
        {"nama": "Telur Ayam", "harga": 25000, "deskripsi": "1 kg telur ayam ras"},
        {"nama": "Ikan Lele", "harga": 30000, "deskripsi": "1 kg ikan lele segar"},
        {"nama": "Sayur Bayam", "harga": 5000, "deskripsi": "1 ikat bayam segar"},
        {"nama": "Bawang Merah", "harga": 28000, "deskripsi": "1 kg bawang merah"},
        {"nama": "Bawang Putih", "harga": 27000, "deskripsi": "1 kg bawang putih"},
        {"nama": "Minyak Goreng Curah", "harga": 16000, "deskripsi": "1 liter"},
        {"nama": "Gula Pasir", "harga": 14000, "deskripsi": "1 kg"},
        {"nama": "Kacang Hijau", "harga": 18000, "deskripsi": "1 kg"},
        {"nama": "Tempe", "harga": 4000, "deskripsi": "1 papan tempe"},
        {"nama": "Tahu", "harga": 5000, "deskripsi": "8 potong tahu putih"},
        {"nama": "Ayam Potong", "harga": 35000, "deskripsi": "1 kg ayam segar"},
        {"nama": "Ikan Bandeng", "harga": 38000, "deskripsi": "1 kg bandeng"},
        {"nama": "Daging Sapi", "harga": 110000, "deskripsi": "1 kg daging sapi segar"},
        {"nama": "Santan Kelapa", "harga": 7000, "deskripsi": "1 bungkus santan segar"},
        {"nama": "Lombok Rawit", "harga": 45000, "deskripsi": "1 kg"},
        {"nama": "Kangkung", "harga": 4000, "deskripsi": "1 ikat kangkung segar"},
        {"nama": "Tomat", "harga": 8000, "deskripsi": "1 kg tomat merah"},
        {"nama": "Wortel", "harga": 10000, "deskripsi": "1 kg wortel"},
        {"nama": "Kentang", "harga": 11000, "deskripsi": "1 kg kentang"},
        {"nama": "Timun", "harga": 7000, "deskripsi": "1 kg timun"},
        {"nama": "Kubis", "harga": 6000, "deskripsi": "1 kepala kubis"},
        {"nama": "Terong", "harga": 9000, "deskripsi": "1 kg terong"},
        {"nama": "Pepaya", "harga": 10000, "deskripsi": "1 buah pepaya sedang"},
        {"nama": "Pisang Raja", "harga": 15000, "deskripsi": "1 sisir pisang"},
        {"nama": "Jeruk", "harga": 20000, "deskripsi": "1 kg jeruk manis"},
        {"nama": "Apel Lokal", "harga": 25000, "deskripsi": "1 kg apel"},
        {"nama": "Mangga", "harga": 22000, "deskripsi": "1 kg mangga harum manis"},
        {"nama": "Jambu Merah", "harga": 18000, "deskripsi": "1 kg jambu biji"},
        {"nama": "Daun Bawang", "harga": 3000, "deskripsi": "1 ikat kecil"},
        {"nama": "Seledri", "harga": 3000, "deskripsi": "1 ikat kecil"},
        {"nama": "Kelapa Parut", "harga": 7000, "deskripsi": "1 butir diparut"},
        {"nama": "Tepung Terigu", "harga": 9000, "deskripsi": "1 kg"},
        {"nama": "Tepung Beras", "harga": 8500, "deskripsi": "1 kg"},
        {"nama": "Daun Pisang", "harga": 3000, "deskripsi": "1 lembar besar"},
        {"nama": "Ikan Asin", "harga": 15000, "deskripsi": "1 ikat ikan asin"},
        {"nama": "Kerupuk Udang", "harga": 12000, "deskripsi": "1 bungkus kerupuk mentah"},
        {"nama": "Garam Halus", "harga": 3000, "deskripsi": "1 bungkus 500g"},
        {"nama": "Kecap Manis Lokal", "harga": 7000, "deskripsi": "Isi 150ml"},
    ]

    PRODUK_DIGITAL = [
        {"nama": "Pulpen Gel Murah", "harga": 2500, "deskripsi": "Pulpen warna-warni isi ulang"},
        {"nama": "Notebook A5", "harga": 3500, "deskripsi": "Buku catatan 60 lembar"},
        {"nama": "Headset Kabel Murah", "harga": 12000, "deskripsi": "Headset stereo universal"},
        {"nama": "Casing HP Silikon", "harga": 8000, "deskripsi": "Softcase universal berbagai tipe"},
        {"nama": "Charger HP 1A", "harga": 15000, "deskripsi": "Adaptor charger fast charge palsu"},
        {"nama": "Stiker Dekorasi 50pcs", "harga": 9500, "deskripsi": "Stiker lucu waterproof"},
        {"nama": "Kabel Data Micro USB", "harga": 7000, "deskripsi": "Kabel 1 meter"},
        {"nama": "Masker Kain 3 Lapis", "harga": 3000, "deskripsi": "Masker kain washable"},
        {"nama": "Tempered Glass", "harga": 10000, "deskripsi": "Pelindung layar HP"},
        {"nama": "Mouse Pad Mini", "harga": 5000, "deskripsi": "Mousepad polos kecil"},
        {"nama": "Dompet Koin Kecil", "harga": 7000, "deskripsi": "Dompet receh travel"},
        {"nama": "Gunting Mini", "harga": 6000, "deskripsi": "Gunting kecil lipat"},
        {"nama": "Pulpen 6-in-1", "harga": 8500, "deskripsi": "Pulpen multifungsi warna-warni"},
        {"nama": "Lampu LED USB", "harga": 5000, "deskripsi": "Lampu belajar portabel"},
        {"nama": "Kipas Mini USB", "harga": 10000, "deskripsi": "Kipas meja colok USB"},
        {"nama": "Notebook Spiral", "harga": 6000, "deskripsi": "Buku catatan ekonomis"},
        {"nama": "Sticky Notes", "harga": 3500, "deskripsi": "Kertas memo warna"},
        {"nama": "Gantungan Kunci Akrilik", "harga": 3000, "deskripsi": "Model karakter lucu"},
        {"nama": "Cermin Mini Lipat", "harga": 7000, "deskripsi": "Cermin saku portable"},
        {"nama": "Sisir Lipat", "harga": 4000, "deskripsi": "Sisir lipat travel"},
        {"nama": "Tas Belanja Lipat", "harga": 10000, "deskripsi": "Eco bag serut praktis"},
        {"nama": "Botol Minum 350ml", "harga": 12000, "deskripsi": "Botol plastik BPA-free"},
        {"nama": "Tali Sepatu Warna", "harga": 4500, "deskripsi": "1 pasang tali sepatu unik"},
        {"nama": "Sabun Cuci Muka Sachet", "harga": 2500, "deskripsi": "Isi 10gr"},
        {"nama": "Penjepit Kertas", "harga": 3000, "deskripsi": "Isi 10 penjepit kecil"},
        {"nama": "Tali Gantungan HP", "harga": 5000, "deskripsi": "Strap lucu untuk handphone"},
        {"nama": "Kabel Charger iPhone KW", "harga": 15000, "deskripsi": "KW fast charging"},
        {"nama": "Sendok Lipat Camping", "harga": 8000, "deskripsi": "Sendok portable logam"},
        {"nama": "Jam Tangan Anak", "harga": 17000, "deskripsi": "Digital murah waterproof"},
        {"nama": "Tas Selempang Mini", "harga": 17000, "deskripsi": "Tas kecil 1 kompartemen"},
        {"nama": "Alat Pembersih Kaca HP", "harga": 4000, "deskripsi": "Kain & cairan kecil"},
        {"nama": "Mini Tripod HP", "harga": 14000, "deskripsi": "Tripod kecil lipat"},
        {"nama": "Tattoo Sticker Temporary", "harga": 3000, "deskripsi": "Tahan air, anak-anak"},
        {"nama": "Earphone Organizer", "harga": 7000, "deskripsi": "Kotak gulung kabel"},
        {"nama": "Tempat Pensil Lucu", "harga": 8000, "deskripsi": "Desain karakter kartun"},
        {"nama": "Kabel Roll Panjang", "harga": 16000, "deskripsi": "Kabel listrik mini roll"},
        {"nama": "Cermin Meja Kecil", "harga": 9500, "deskripsi": "Kaca meja minimalis"},
        {"nama": "Kunci Gembok Kecil", "harga": 6000, "deskripsi": "Gembok koper/tas"},
        {"nama": "Tempat Sabun Portable", "harga": 5000, "deskripsi": "Kotak sabun plastik"},
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_products_produk_riil = models.LongStringField(blank=True)
    selected_products_produk_digital = models.LongStringField(blank=True)
    total_belanja_pasar_riil = models.CurrencyField(initial=0)
    total_belanja_pasar_digital = models.CurrencyField(initial=0)

    # Investasi Risiko Rendah
    lowinvest = models.CurrencyField(label="Berapa rupiah yang ingin Anda investasikan?", min=0)
    hasil_akhir_lowinvest = models.CurrencyField()
    untungrugi_lowinvest = models.StringField()  # UNTUNG atau RUGI


class PlatformRiil(Page):
    form_model = 'player'
    form_fields = ['selected_products_produk_riil']

    @staticmethod
    def vars_for_template(player: Player):
        produk_acak = random.sample(C.PRODUK_TRADISIONAL, 25)
        player.participant.vars['produk_riil_acak'] = produk_acak
        return dict(produk_list=produk_acak)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        selected_indexes = json.loads(player.selected_products_produk_riil or "[]")
        produk_acak = player.participant.vars.get('produk_riil_acak', [])
        total = sum(produk_acak[i]['harga'] for i in selected_indexes)
        player.total_belanja_pasar_riil = total


class PlatformDigital(Page):
    form_model = 'player'
    form_fields = ['selected_products_produk_digital']

    @staticmethod
    def vars_for_template(player: Player):
        produk_acak = random.sample(C.PRODUK_DIGITAL, 25)
        player.participant.vars['produk_digital_acak'] = produk_acak
        return dict(produk_list=json.dumps(produk_acak))  # agar bisa di JS

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        selected = json.loads(player.selected_products_produk_digital or "[]")
        total = sum(C.PRODUK_DIGITAL[i]["harga"] for i in selected)
        player.total_belanja_pasar_digital = total


class LowInvestment(Page):
    form_model = 'player'
    form_fields = ['lowinvest']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        investasi = player.lowinvest

        # Simulasi hasil acak: 70% untung, 30% rugi
        is_untung = random.random() < 0.7
        if is_untung:
            hasil = investasi * 1.2  # naik 20%
            player.untungrugi_lowinvest = "UNTUNG"
        else:
            hasil = investasi * 0.8  # turun 20%
            player.untungrugi_lowinvest = "RUGI"

        player.hasil_akhir_lowinvest = hasil


class LowResults(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            status=player.untungrugi_lowinvest,
            hasil=int(player.hasil_akhir_lowinvest)
        )


page_sequence = [PlatformRiil, PlatformDigital, LowInvestment, LowResults]
