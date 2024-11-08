from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CMC_TOKEN_API: str = str()
    CMC_BASE_URL: str = 'https://pro-api.coinmarketcap.com'

settings = Settings(_env_file='.env')