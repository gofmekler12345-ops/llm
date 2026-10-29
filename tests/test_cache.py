from cache import set_last_pair, get_last_pair, clear_last_pair

def setup_function(function):
    clear_last_pair()

def test_set_and_get_last_pair():
    set_last_pair("country_from", "country_to")
    assert get_last_pair() == ("country_from", "country_to")

def test_clear_last_pair():
    set_last_pair("country_from", "country_to")
    clear_last_pair()
    assert get_last_pair() is None