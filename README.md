# Discord Bot Init Project ( Python )

This is a init project for Discord Bot development.

## Tech stack

- Python
- Discord.py

## Prerequisites

- [Python](https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe) 3.13.0 or higher
- [Discord bot](https://discord.com/developers/applications/)

## Configuration

### 1. clone the repository:

```
https://github.com/acmicpc0614/Discord-Bot-init-Python.git
```

### 2. Go to the project directory:

```
cd Discord-Bot-init-Python
```

### 3. Set local virtual environments named .venv:
- windows:
```
python -m venv .venv
```
- linux:
```
python3 -m venv .venv
```

### 4. Activate the virtual environment:
- windows:
```
.venv\Scripts\activate
```
- linux:
```
source .venv/bin/activate
```
### 5. Deactivate the virtual environment:
- windows:
```
deactivate
```
- linux:
```
deactivate
```
### 6. Install the required packages:

```
pip install -r requirements.txt
```

### 7. Set the Discord bot token in the .env file:

```
DISCORD_TOKEN=
```

- You can use the [Discord bot](https://discord.com/developers/applications/) to get the token.
- Create a Discord bot, invite it to your server.
- Get token from the Discord bot.

### 8. Run the script:

```
python main.py
```

### 9. Logging to development server:
```
from logger import logger
...

logger.info("Hello, World!")
```

### 10. How to fix audioop module err in python for Discord bot development?
```
pip install audioop-lts
```

### 11. Enjoy!


## Contact

- [Telegram](https://t.me/plzbugmenot)
