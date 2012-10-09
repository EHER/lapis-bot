#Lapis Bot
A IRC Bot that can search by places using the [Apontador API](http://api.apontador.com.br/).

##Install
```
git clone git://github.com/EHER/lapis-bot.git
virtualenv lapis-bot
cd lapis-bot
source bin/activate
pip install -r deps.txt
```

##Configure
```
vim bot.py
```
Put your [consumer key and secret](http://www.apontador.com.br/accounts/apps.html) of Apontador API.

```
APONTADOR_CONSUMER_KEY = ''
APONTADOR_CONSUMER_SECRET = ''
```

##Run
```
python bot.py
```



