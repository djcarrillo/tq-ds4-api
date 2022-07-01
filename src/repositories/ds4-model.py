import ast
import json

import requests
from requests_oauthlib import OAuth1
from src.config.settings import Setting
from src.enums.token_fixed import Polygon


def available_companies():
    url = Polygon('available_companies')
    url_auth = f'{url}?apiKey={Setting.polygon_auth}'
    info_companies = requests.get(url_auth)
    symbols = []

    companies = json.loads(info_companies.content)['results']

    if info_companies.status_code == 200:
        for company in companies:
            company_tracker = company.get('ticker', False)
            if company_tracker:
                symbols.append(company_tracker)
        return symbols
    else:
        return "Intente nuevamente"


