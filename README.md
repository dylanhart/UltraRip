# UltraRip

A Slack app backend to generate customized gravestones via `/rip [message]`.

## Running Locally

### Dependencies
* Python 3 w/ pip

### Setup
* `pip3 install -r requirements.txt` to fetch python dependencies
* `python3 rip.py` to run the app
* ???
* [Profit](http://localhost:5000/gen_img?text=Hey%20it%20works)

## Deployment

The application is hosted on Heroku at [ultra-rip.herokuapp.com](ultra-rip.herokuapp.com).
Pushes to the `master` branch will automatically deploy.

The discord bot requires a `DISCORD_TOKEN` environment variable to be set to a valid bot
token. The bot needs permission to send messages and attach files.

