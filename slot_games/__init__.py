from otree.api import *
import random

doc = """
Permainan Slot Machine sederhana: Pemain memutar slot dan mendapatkan skor jika tiga simbol sama.
"""


class C(BaseConstants):
    NAME_IN_URL = 'slot_games'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5
    SLOT_SYMBOLS = ['🍒', '🍋', '🔔', '⭐', '💎']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    slot1 = models.StringField()
    slot2 = models.StringField()
    slot3 = models.StringField()
    slot4 = models.StringField()
    slot5 = models.StringField()
    win = models.BooleanField(initial=False)


# PAGE 1: Slot Machine Game
class Coba(Page):
    def vars_for_template(player: Player):
        symbols = C.SLOT_SYMBOLS
        player.slot1 = random.choice(symbols)
        player.slot2 = random.choice(symbols)
        player.slot3 = random.choice(symbols)
        player.slot4 = random.choice(symbols)
        player.slot5 = random.choice(symbols)

        # Menang jika tiga simbol sama
        if player.slot1 == player.slot2 == player.slot3 == player.slot4 == player.slot5:
            player.win = True
            player.payoff = 100
        else:
            player.win = False
            player.payoff = 0

        return {
            'slot1': player.slot1,
            'slot2': player.slot2,
            'slot3': player.slot3,
            'slot4': player.slot4,
            'slot5': player.slot5,
            'win': player.win
        }

    def is_displayed(player):
        return True

    def before_next_page(player, timeout_happened):
        if player.round_number > 1:
            player.payoff += player.in_round(player.round_number - 1).payoff


# PAGE 2: Final Results
class Results(Page):
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS

    def vars_for_template(player):
        total = sum([p.payoff for p in player.in_all_rounds()])
        return {'total': total}


page_sequence = [Coba, Results]
