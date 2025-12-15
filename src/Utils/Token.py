# takes a short lived token and retrieves the long lived token

import requests 
import datetime 

def get_long_lived_token(config: dict) -> str:
    APP_ID = config["authentication"]["APP_ID"]
    APP_SECRET= config["authentication"]["APP_SECRET"]
    SHORT_LIVED_TOKEN = config["authentication"]["SHORT_LIVED_TOKEN"]
    URL = config["authentication"]["URL"]
    
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": APP_ID,
        "client_secret": APP_SECRET,
        "fb_exchange_token": SHORT_LIVED_TOKEN,
    }
    
    try: 
        r = requests.get(URL, params=params)
        r.raise_for_status()
        data = r.json()
        return data["access_token"]
    except requests.RequestException as e:
        raise RuntimeError(f"{e}\nShort lived token is not valid.") from e
    except (KeyError, ValueError) as e:
        raise RuntimeError(f"Bad response: {data if 'data' in locals() else ''}") from e


def validate(config: dict, TOKEN) -> bool:
    # vars:
    APP_ID = config["authentication"]["APP_ID"]
    APP_SECRET= config["authentication"]["APP_SECRET"]
    URL = config["authentication"]["URL"]
    
    app_access_token = f"{APP_ID}|{APP_SECRET}"
    params = {
        'input_token': TOKEN,
        'access_token': app_access_token
    }
    
    try:
        r = requests.get('https://graph.facebook.com/debug_token', params=params)
        r.raise_for_status()
        data = r.json()
        if data['data']['is_valid']:
            expires = datetime.datetime.fromtimestamp(data['data'].get('expires_at')).strftime("%A, %B %d, %Y at %H:%M")
            print(f"Token is valid. Expires {expires}")
            return True
        else: 
            return False
    except: 
        return False
        