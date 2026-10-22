import pytest
from pydantic import ValidationError

from models.travel_model import TravelInfoRequest, TravelInfoResponse

# TODO: Add tests for TravelInfoRequest and TravelInfoResponse

def test_travel_info_request_requires_all_fields():
    with pytest.raises(ValidationError):
        TravelInfoRequest(country_from="France")

def test_travel_info_request_valid():
    request = TravelInfoRequest(
        country_from="France",
        country_to="Japan",
        is_capital=True,
        is_weather=False,
        is_currency=True,
    )
    assert request.country_from == "France"
    assert request.country_to == "Japan"
    assert request.is_capital is True
    assert request.is_weather is False
    assert request.is_currency is True


def test_travel_info_response_defaults():
    response = TravelInfoResponse(
        country_from="France",
        country_to="Japan",
    )
    assert response.country_from == "France"
    assert response.country_to == "Japan"
    assert response.capital_to is None
    assert response.weather is None
    assert response.currency_code_from is None
    assert response.currency_code_to is None
    assert response.currency_name_from is None
    assert response.currency_name_to is None
    assert response.exchange_rate is None


def test_travel_info_response_valid_with_all_fields():
    response = TravelInfoResponse(
        country_from="France",
        country_to="Japan",
        capital_to="Tokyo",
        weather="Sunny",
        currency_code_from="EUR",
        currency_code_to="JPY",
        currency_name_from="Euro",
        currency_name_to="Japanese Yen",
        exchange_rate=160.5,
    )
    assert response.capital_to == "Tokyo"
    assert response.currency_code_from == "EUR"
    assert response.currency_code_to == "JPY"
    assert response.exchange_rate == 160.5