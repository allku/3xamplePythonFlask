# -*- coding: utf-8 -*-
import json
import pytest
from app import app


@pytest.mark.run(order=1)
def test_post_beer():
    response = app.test_client().post('/example/rest/v1/beer',
            json={'name': 'Veneno',
                  'brand': 'Mi cervezeria clandestina',
                  'dateReleased': '1803-10-11T13:44:02',
                  'locationId': 4,
                  'ingredients': [{'name': 'Agua contaminada'}]})
    res = json.loads(response.data.decode('utf-8'))
    assert res['name'] == 'Veneno'
    assert response.status_code == 200


@pytest.mark.run(order=2)
def test_get_beer_by_id():
    response = app.test_client().get('/example/rest/v1/beer/1')
    res = json.loads(response.data.decode('utf-8'))
    print(res)
    assert res['id'] == 1
    assert res['name'] == 'Calenturienta'
    assert res['brand'] == 'Cerveceria de Mi Hogar'
    assert response.status_code == 200


@pytest.mark.run(order=3)
def test_get_all_beers():
    response = app.test_client().get('/example/rest/v1/beers')
    res = json.loads(response.data.decode('utf-8'))
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['name'] == 'Calenturienta'
    # assert res[1]['name'] == 'Krombacher'
    assert response.status_code == 200
    assert type(res) is list

