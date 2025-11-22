# Setting up

## Enviroment

Linux/MacOS :
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows :
```cmd
python -m venv .venv
".venv/Scripts/activate.bat"
pip install -r requirements.txt
```

## Program's settings
Expected fields in `global_settings.py`:

- `LOGGER_BYDIRECT_LOGS_TO_STDOUT`  
`True` or `False`. Determines if logging text is also sent to stdout. 

- `TELEGRAM_TOKEN`  
String with bot's telegram token.

- `TELEGRAM_ADMIN`  
Number with admin's (controller's) telegram id.

- `TELEGRAM_MAX_TIME_SHIFT`  
The maximum time shift in seconds of message's sent time relative to current, exceeding which message is ignored.

- `MAIN_AFTERLOAD_SCRIPT`  
String with path to script to execute line by line after setting everything up or `None` if no script needed.
