# Function to get odds data from API:

import requests

def get_odds_data(api_key, sport):
    initial_url = 'https://api.the-odds-api.com/v4/sports?apiKey=' + api_key + '&all=true'
    response = requests.get(initial_url)

    data = response.json()

    for sport_data in data:
        if sport_data['sport_key'] == sport:
            key = sport_data['key']
            break
        
        second_url = 'https://api.the-odds-api.com/v4/sports/' + key + '/odds?apiKey=' + api_key + '&regions=eu,us,us2,uk,au&markets=h2h,spreads,totals&dateFormat=iso&oddsFormat=american'
        response = requests.get(second_url)
        
        data = response.json()

    return data


# Option 2
import requests
import json

def get_odds_data(api_key, league_key):
    url = f"https://api.the-odds-api.com/v4/sports/{league_key}/odds"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    params = {
        'regions': 'eu,us,us2,uk,au',
        'markets': 'h2h,spreads,totals',
        'dateFormat': 'iso',
        'oddsFormat': 'american'
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text)
    return data

# Option 3?

# Function to get odds data from API:

import requests

def get_odds_data(api_key, sport):
    initial_url = 'https://api.the-odds-api.com/v4/sports?apiKey=' + api_key + '&all=true'
    response = requests.get(initial_url)

    data = response.json()

    for sport_data in data:
        if sport_data['sport_key'] == sport:
            key = sport_data['key']
            break
        
        second_url = 'https://api.the-odds-api.com/v4/sports/' + key + '/odds?apiKey=' + api_key + '&regions=eu,us,us2,uk,au&markets=h2h,spreads,totals&dateFormat=iso&oddsFormat=american'
        response = requests.get(second_url)
        
        data = response.json()

    return data