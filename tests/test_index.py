# -*- coding: utf-8 -*-
import json

from app import app


def test_index_route():
    response = app.test_client().get('/')
    res = json.loads(response.data.decode('utf-8'))
    assert res['success'] == True
    assert res['application']['name'] == '3xamplePythonFlask'
    assert response.status_code == 200

