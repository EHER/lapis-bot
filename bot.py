# -*- coding: UTF-8 -*-
from irctk import Bot
import requests
from requests.auth import HTTPBasicAuth
import json
import random


class Config:
    SERVER = 'irc.freenode.net'
    PORT = 6667
    SSL = False
    TIMEOUT = 300
    NICK = 'LapisBot'
    REALNAME = 'Apontador Bot'
    CHANNELS = ['#apontador']
    APONTADOR_BASE_URL = 'http://api.apontador.com.br/v1'
    APONTADOR_KEY = ''
    APONTADOR_SECRET = ''

bot = Bot()
bot.config.from_object(Config)


@bot.command('search')
def search(context):
    query = context.args

    search_url = bot.config['APONTADOR_BASE_URL'] + '/search/places'
    r = requests.get(
            search_url,
            params=dict(type='json', q=query),
            auth=HTTPBasicAuth(
                bot.config['APONTADOR_KEY'],
                bot.config['APONTADOR_SECRET']
                )
            )
    data = json.loads(r.content)

    if not data['search'] or data['search']['result_count'] == '0':
        return u'não achei nada... :('

    search_result_rows = len(data['search']['places'])
    random_index = random.randrange(1, search_result_rows) - 1
    place = data['search']['places'][random_index]['place']

    return place['name'] + ' ' + place['main_url']

if __name__ == '__main__':
    bot.run()
