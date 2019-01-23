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

* create a ``local_settings.py`` file with your django ``SECRET_KEY`` and telegram ``BOT_TOKEN`` in ``main`` folder

* set a webhook with telegram api (replace {data} with your own)

```bash
curl https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}
```

### Start server

* enter virtual environment

```bash
source venv/bin/activate
```

* start django server

```bash
python manage.py runserver
```
