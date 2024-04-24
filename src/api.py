import requests
from src.services import WORD_ENDPOINT

def collect_word()->str:
    response = requests.get(WORD_ENDPOINT)
    response = response.content.decode("utf-8")
    return response[2:-2]
