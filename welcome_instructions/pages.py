from otree.api import *


class Welcome_Experiment(Page):
    pass


class Instruction_Page(Page):
    form_model = 'player'
    form_fields = ['usia', 'jenis_kelamin', 'pendidikan', 'status_pekerjaan', 'aktivitas_utama',
                   'aktivitas_untuk_seseorang', 'rata_pengeluaran', 'status_perkawinan',
                   'jumlah_anak', 'jumlah_anak_sekolah', 'jenis_rekening', 'no_rekening']


class BeforeInfo(Page):
    pass


class DemoPractice(Page):
    pass


page_sequence = [Welcome_Experiment, Instruction_Page, BeforeInfo, DemoPractice]
