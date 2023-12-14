import data
import sender_stand_request


def get_token():
    res = sender_stand_request.post_new_user()
    if res.ok:
        return res.json()['authToken']
    else:
        return ''


def test_kits_name_1():
    token = get_token()
    kit_name = 'a'
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name


def test_kits_name_511():
    token = get_token()
    kit_name = 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC'
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name


def test_kits_name_0():
    token = get_token()
    kit_name = ''
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 400


def test_kits_name_512():
    token = get_token()
    kit_name = 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD'
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 400


def test_kits_name_eng():
    token = get_token()
    kit_name = 'QWErty'
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name


def test_kits_name_rus():
    token = get_token()
    kit_name = 'Мария'
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name


def test_kits_name_special():
    token = get_token()
    kit_name = '"№%@",'
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name


def test_kits_name_space():
    token = get_token()
    kit_name = ' Человек и КО '
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name


def test_kits_name_numberstr():
    token = get_token()
    kit_name = '123'
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 201
    assert res.json()['name'] == kit_name


def test_kits_name_no_parameter():
    token = get_token()
    user_kit = data.my_kit.copy()
    user_kit.pop('name')
    res = sender_stand_request.post_new_client_kit(token, user_kit)
    assert res.status_code == 400


def test_kits_name_number():
    token = get_token()
    kit_name = 123
    res = sender_stand_request.post_new_client_kit(token, kit_name)
    assert res.status_code == 400