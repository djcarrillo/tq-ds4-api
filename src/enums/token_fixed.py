

def Polygon(endpoint):

    dirs = {
           'available_companies': '/v3/reference/tickers'

    }

    return 'https://api.polygon.io'+dirs[endpoint]