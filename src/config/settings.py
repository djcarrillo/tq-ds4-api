import os

path_base = os.path.dirname(os.path.realpath(__file__))


class Setting:
    VERSION = "1.0.0"
    ENVIRONMENT = "DEV" if os.getenv("MACHINE", 'DEV') == "DEV" else "PROD"
    ROOT_PATH = "" if ENVIRONMENT == "DEV" else "/ds4_bootcamp"
    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS", "['*']")
    ALLOW_CREDENTIALS = os.getenv("ALLOW_CREDENTIALS", True)
    ALLOW_METHODS = os.getenv("ALLOW_METHODS", "['*']")
    ALLOW_HEADERS = os.getenv("ALLOW_HEADERS", "['*']")

    USER_AWS = os.getenv("user")
    ACCESS_KEY_ID_AWS = os.getenv("access_key_id")
    SECRET_ACCESS_KEY_AWS = os.getenv("secret_access_key")
    PASSWORD_AWS = os.getenv("password")

    x_auth_login_token = os.getenv("jwt", 'xx')

    DATA_RANDOM_FOREST = f'{path_base}/../enums/random_forest/data_training/bd_random_forest.csv'
    MODEL_RANDOM_FOREST = f'{path_base}/../enums/random_forest/model/random_forest.pkl'
    MODEL_LOGIT = f'{path_base}/../enums/logit/model/logit.pkl'
