from otree.api import *
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
    total_belanja_riil = models.CurrencyField(initial=0)

    selected_products_produk_digital = models.LongStringField(blank=True)
    total_harga_digital = models.CurrencyField(initial=0)

    # Investasi Risiko Rendah
    lowinvest = models.CurrencyField(label="Berapa rupiah yang ingin Anda investasikan?", min=0)
    hasil_akhir_lowinvest = models.CurrencyField()
    untungrugi_lowinvest = models.StringField()  # UNTUNG atau RUGI

    def live_handle(self, data):
        jenis = data.get('jenis')

        if data.get('jenis') == 'belanja_riil':
            total = data['total_belanja']
            if total > 100000:
                return {self.id_in_group: dict(status="error", message="Total belanja melebihi saldo.")}

            self.selected_products_produk_riil = json.dumps(data['produk_terpilih'])
            self.total_belanja_riil = total

            return {self.id_in_group: dict(status="success", message="Belanja riil berhasil disimpan.")}

        elif jenis == "digital":
            produk_terpilih = data.get("produk_terpilih", [])
            total = data.get("total", 0)

            if total > 100000:
                return {self.id_in_group: dict(status="error", message="Total belanja digital melebihi saldo.")}

            self.selected_products_produk_digital = json.dumps(produk_terpilih)
            self.total_harga_digital = total

            return {self.id_in_group: dict(status="success", message="Belanja digital berhasil disimpan.")}

        return {self.id_in_group: dict(error="Jenis data tidak dikenali.")}

