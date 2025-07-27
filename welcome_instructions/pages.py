from otree.api import *


class Welcome_Experiment(Page):
    pass


class Instruction_Page(Page):
    form_model = 'player'
    form_fields = ['usia', 'jenis_kelamin', 'aktivitas_utama', 'status_perkawinan', 'jumlah_anak', 'anak_sekolah']


page_sequence = [Welcome_Experiment, Instruction_Page]
