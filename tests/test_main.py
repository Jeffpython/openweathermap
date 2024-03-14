import pytest
from app.main import get_city_data, get_weather_data

@pytest.fixture()
def api_key():
    return 'ed03406521a9e4a91d46056b0aa6237c'


@pytest.fixture()
def city():
    return 'Moscow'


@pytest.fixture()
def lat():
    return 55.7504461


@pytest.fixture()
def lon():
    return 37.6174943


def test__get_city_data__return_correct_data(city, api_key, lat, lon):
    assert get_city_data(city, api_key) == (lat, lon)


def test__get_city_data__return_exception_for_non_existent_city(api_key):
    with pytest.raises(IndexError):
        assert get_city_data('abcde', api_key)


def test__get_city_data__return_exception_for_empty_city(api_key):
    with pytest.raises(KeyError):
        assert get_city_data('', api_key)


def test__get_city_data__return_exception_for_empty_api_key(city, api_key):
    with pytest.raises(KeyError):
        assert get_city_data(city, '')


def test__get_weather_data__return_correct_data(lat, lon, api_key):
    assert get_weather_data(lat, lon, api_key)['cod'] == 200


def test__get_weather_data__return_cod_401_for_empty_api_key(lat, lon, api_key):
    assert get_weather_data(lat, lon, '')['cod'] == 401
