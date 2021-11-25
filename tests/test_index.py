# -*- coding: utf-8 -*-
import json

from app import app
from colorama import Fore


def test_index_route():
    url = '/'
    response = app.test_client().get(url)
    res = json.loads(response.data.decode('utf-8'))
    print(Fore.GREEN + 'URL {0}'.format(url))
    print(Fore.YELLOW + 'Json GET result {0} '.format(res))
    assert res['success'] == True
    assert res['application']['name'] == '3xamplePythonFlask'
    assert response.status_code == 200

