import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ.get("QUOTEBOT_API_URL", "https://api.exchangerate.host")


class RateClient:
    def __init__(self, base_url=BASE_URL, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def latest(self, base="USD"):
        response = requests.get(
            "{}/latest".format(self.base_url),
            params={"base": base},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.json()["rates"]

    def convert(self, amount, base, to):
        rates = self.latest(base)
        if to not in rates:
            raise KeyError("unknown currency: {}".format(to))
        return round(amount * rates[to], 4)
