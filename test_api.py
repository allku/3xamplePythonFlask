# -*- coding: utf-8 -*-
import json

from app import app


def test_index_route():
    response = app.test_client().get('/')
    res = json.loads(response.data.decode('utf-8'))
    # assert response.data.decode('utf-8') == ''
    assert res['success'] == True
    assert res['application']['name'] == '3xamplePythonFlask'
    assert response.status_code == 200


def test_get_beer_by_id():
    response = app.test_client().get('/example/rest/v1/beer/1')
    res = json.loads(response.data.decode('utf-8'))
    print(res)
    assert res['id'] == 1
    assert res['name'] == 'Calenturienta'
    assert res['brand'] == 'Cerveceria de Mi Hogar'
    assert response.status_code == 200


def test_get_all_beers():
    response = app.test_client().get('/example/rest/v1/beers')
    res = json.loads(response.data.decode('utf-8'))
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['name'] == 'Calenturienta'
    assert res[1]['name'] == 'Krombacher'
    assert response.status_code == 200
    assert type(res) is list

