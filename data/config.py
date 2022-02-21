#-*- coding: utf-8 -*-

from environs import Env 

env = Env()
env.read_env()


BOTS_SETTINGS = [
    {
        'token': env.str("BOT_1"),
        'bot': 'ReactionsClicker',
        'id': 945248403657478164,
        'prefix': '!',
    },
    {
        'token': env.str("BOT_1"),
        'bot': 'ReactionsClicker',
        'id': 945248403657478164,
        'prefix': '!',
    }
]
