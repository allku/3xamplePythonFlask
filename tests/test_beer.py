# -*- coding: utf-8 -*-
import json
import pytest
from app import app
import colorama
from colorama import Fore


# Value to share between test functions
class Values:
    id = None


@pytest.mark.order(1)
def test_post_beer():
    url = '/example/rest/v1/beer'
    response = app.test_client().post(url,
            json={'name': 'Venenoza',
                  'brand': 'Mi cervezeria clandestina',
                  'dateReleased': '1803-10-11T13:44:02',
                  'locationId': 4,
                  'ingredients': [{'name': 'Agua contaminada'}]})
    res = json.loads(response.data.decode('utf-8'))
    print(Fore.GREEN + 'URL {0}'.format(url))
    print(Fore.BLUE + 'Json POST result {0} '.format(res))
    Values.id = res['id']
    assert res['name'] == 'Venenoza'
    assert response.status_code == 200


@pytest.mark.order(4)
def test_put_beer():
    url = '/example/rest/v1/beer/{0}'.format(Values.id)
    response = app.test_client().put(url,
            json={'name': 'Venenoza 100%',
                  'brand': 'Mi cervezeria clausurada',
                  'dateReleased': '1903-10-11T13:44:02',
                  'locationId': 5})
    res = json.loads(response.data.decode('utf-8'))
    print(Fore.GREEN + 'URL {0}'.format(url))
    print(Fore.BLUE + 'Json PUT result {0} '.format(res))
    assert res['name'] == 'Venenoza 100%'
    assert response.status_code == 200


@pytest.mark.order(2)
def test_get_beer_by_id():
    url = '/example/rest/v1/beer/{0}'.format(Values.id)
    response = app.test_client().get(url)
    res = json.loads(response.data.decode('utf-8'))
    print(Fore.GREEN + 'URL {0}'.format(url))
    print(Fore.BLUE + 'Json GET result {0} '.format(res))
    assert res['id'] == Values.id
    assert res['name'] == 'Venenoza'
    assert res['brand'] == 'Mi cervezeria clandestina'
    assert response.status_code == 200


#@pytest.mark.skip(reason=None)
@pytest.mark.order(3)
def test_get_all_beers():
    url = '/example/rest/v1/beers'
    response = app.test_client().get(url)
    res = json.loads(response.data.decode('utf-8'))
    print(Fore.GREEN + 'URL {0}'.format(url))
    print(Fore.BLUE + 'Json GET result {0} '.format(res))
    #assert type(res[0]) is dict
    #assert type(res[1]) is dict
    #assert res[0]['name'] == 'Calenturienta'
    #assert res[1]['name'] == 'Krombacher'
    assert response.status_code == 200
    assert type(res) is list


@pytest.mark.order(5)
def test_delete_beer():
    url = '/example/rest/v1/beer/{0}'.format(Values.id)
    response = app.test_client().delete(url)
    res = json.loads(response.data.decode('utf-8'))
    print(Fore.GREEN + 'URL {0}'.format(url))
    print(Fore.BLUE + 'Json DELETE result {0} '.format(res))
    assert res['name'] == 'Venenoza 100%'
    assert response.status_code == 200
