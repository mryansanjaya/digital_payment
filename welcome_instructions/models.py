from otree.api import *

doc = """
Welcome to Digital Payment Experiment 
"""


class Constants(BaseConstants):
    name_in_url = 'welcome_instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    usia = models.IntegerField()
    jenis_kelamin = models.IntegerField(
        choices=[
            [1, 'Laki-Laki'],
            [2, 'Perempuan']
        ],
        widget=widgets.RadioSelect
    )
    pendidikan = models.IntegerField(
        choices=[
            [1, 'SD'],
            [2, 'SMP'],
            [3, 'SMA'],
            [4, 'Sarjana/Diploma'],
            [5, 'Lainnya']
        ],
        widget=widgets.RadioSelect
    )
    status_pekerjaan = models.IntegerField(
        choices=[
            [1, 'Bekerja/Berusaha'],
            [2, 'Mencari Pekerjaan'],
            [3, 'Sekolah'],
            [4, 'Mengurus Rumah Tangga'],
            [5, 'Tidak Bekerja'],
            [6, 'Lainnya']
        ],
        widget=widgets.RadioSelect
    )
    aktivitas_utama = models.StringField(
        choices=[
            ['bertani', 'Bertani'],
            ['berdagang ritel', 'Berdagang Ritel (Kelontong, Los di pasar, E-commerce, dsb)'],
            ['transportasi/ojek', 'Transportasi/Ojek'],
            ['usaha jasa', 'Usaha Jasa (Wedding, Rias/Salon, Katering, Print, dsb)'],
            ['usaha makanan', 'Usaha Makanan (Warung, Kafe, Rumahan, dsb)'],
            ['produksi seni kriya', 'Produksi Karya Seni-Kriya'],
            ['usaha fashion', 'Usaha Fashion (Jahit, Dropshipping, dsb)'],
            ['lainnya', 'Lainnya'],
        ],
    )
    aktivitas_untuk_seseorang = models.IntegerField(
        choices=[
            [1, 'Ya'],
            [2, 'Tidak']
        ],
        widget=widgets.RadioSelect
    )
    rata_pengeluaran = models.IntegerField(
        choices=[
            [1, 'Di bawah Rp. 500.000'],
            [2, 'Rp. 500.001 s.d. Rp. 1.000.000'],
            [3, 'Rp. 1.000.001 s.d. 1.500.000'],
            [4, 'Rp. 1.500.001 s.d. Rp. 2.000.000'],
            [5, 'Rp. 2.000.001 s.d. Rp. 2.500.000'],
            [6, 'Di atas Rp. 2.500.000'],
        ],
        widget=widgets.RadioSelect
    )
    status_perkawinan = models.IntegerField(
        choices=[
            [1, 'Kawin'],
            [2, 'Belum Kawin'],
            [3, 'Cerai Mati'],
            [4, 'Cerai Hidup']
        ],
        widget=widgets.RadioSelect
    )
    jumlah_anak = models.IntegerField()
    jumlah_anak_sekolah = models.IntegerField()
    jenis_rekening = models.StringField(
        choices=[
            ['bca', 'BCA'],
            ['bni', 'BNI'],
            ['bri', 'BRI'],
            ['mandiri', 'Mandiri'],
            ['dana', 'DANA'],
            ['ovo', 'OVO'],
            ['gopay', 'GoPay']
        ],
    )
    no_rekening = models.IntegerField()