import pytest
import responses

from quotebot.client import RateClient

PAYLOAD = {"base": "USD", "rates": {"EUR": 0.92, "GBP": 0.79, "JPY": 148.5}}


@responses.activate
def test_latest_returns_rates():
    responses.add(
        responses.GET,
        "https://api.exchangerate.host/latest",
        json=PAYLOAD,
        status=200,
    )
    assert RateClient().latest("USD")["EUR"] == 0.92


@responses.activate
def test_convert_multiplies_rate():
    responses.add(
        responses.GET,
        "https://api.exchangerate.host/latest",
        json=PAYLOAD,
        status=200,
    )
    assert RateClient().convert(10, "USD", "EUR") == 9.2


@responses.activate
def test_unknown_currency_raises():
    responses.add(
        responses.GET,
        "https://api.exchangerate.host/latest",
        json=PAYLOAD,
        status=200,
    )
    with pytest.raises(KeyError):
        RateClient().convert(10, "USD", "XYZ")


def test_base_url_is_normalized():
    assert RateClient(base_url="https://example.com/").base_url == "https://example.com"
