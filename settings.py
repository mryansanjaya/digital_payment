from os import environ


SESSION_CONFIGS = [
    {
        'name': 'digital_payment',
        'display_name': "Digital Payment Experiment",
        'num_demo_participants': 1,
        'app_sequence': ['welcome_instructions', 'digital_payment_practice', 'digital_payment', 'payment_page'],
    }
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'selected_round',
    'final_payment',
    'uang_kehadiran',
]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='tengah',
        display_name='Semarang Tengah',
        participant_label_file='_rooms/tengah.txt',
    ),
    dict(
        name='utara',
        display_name='Semarang Utara',
        participant_label_file='_rooms/utara.txt',
    ),
    dict(
        name='selatan',
        display_name='Semarang Selatan',
        participant_label_file='_rooms/selatan.txt',
    ),
    dict(
        name='timur',
        display_name='Semarang Timur',
        participant_label_file='_rooms/timur.txt',
    ),
]

USE_LIVE_RELOAD = True
DEBUG = False
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '5099442996514'

INSTALLED_APPS = ['otree']
