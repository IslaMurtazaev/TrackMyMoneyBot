# TrackMyMoneyBot
Simple bot that uses a Telegram API to track financial spendings

### Set up

* create a virtual environment inside a root folder

```bash
virtualenv --no-site-packages --distribute -p /usr/bin/python3 venv
```

* enter virtual environment

```bash
source venv/bin/activate
```

* install dependencies

```bash
pip install -r requirements.txt
```

* run migrations

```bash
python manage.py migrate
```

* create a ``local_settings.py`` file with your django ``SECRET_KEY``, telegram ``BOT_TOKEN`` and ``APP_URL`` in ``main`` folder.

To generate ``BOT_TOKEN`` you should [create a new bot](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token).

Expample:
```bash
SECRET_KEY = "my_secret_key"
BOT_TOKEN = "my_bot_token"
APP_URL = "https://my_domain.com"
```
 
Using this information, after you start the server, bot will automatically set webhook.

### Start server

* enter virtual environment

```bash
source venv/bin/activate
```

* start django server

```bash
python manage.py runserver
```
