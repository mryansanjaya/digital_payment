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
    aktivitas_utama = models.StringField()
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
    anak_sekolah = models.IntegerField()
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
    no_rekening = models.StringField()

