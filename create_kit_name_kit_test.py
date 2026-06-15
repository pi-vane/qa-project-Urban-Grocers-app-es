import sender_stand_request
import data


def get_user_here():
    user_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()

def auth_token():
    token = get_user_here()
    return token.json()['authToken']

def positive_assert_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))

    assert new_kit_name == kit_response.json()["name"]
    assert kit_response.status_code == 201

def test_1_character_kit_name_get_success_response():
    positive_assert_kit_name("a")

def positive_assert_511_character_count_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))
    name_str_count = len(kit_response.json()["name"])

    assert name_str_count == 511
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == new_kit_name

def test_511_kit_name_less_than_a_get_success_response():
    positive_assert_511_character_count_kit_name(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def negative_assert_empty_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))

    assert kit_response.json()["name"] == new_kit_name
    assert kit_response.status_code == 400

def test_empty_kit_name_get_400_failure_response():
    negative_assert_empty_kit_name("")

def negative_assert_512_character_count_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))
    name_str_count = len(kit_response.json()["name"])

    assert name_str_count == 512
    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == new_kit_name

def test_512_character_kit_name_get_failure_response():
    negative_assert_512_character_count_kit_name(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def positive_assert_symbol_in_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == new_kit_name

def test_symbol_in_kit_name_get_success_response():
    positive_assert_symbol_in_kit_name("\"№%@\",")

def test_space_in_kit_name_get_success_response():
    positive_assert_kit_name("A Aaa")

def positive_assert_number_string_in_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))
    assert kit_response.json()["name"] == new_kit_name
    assert kit_response.status_code == 201

def test_number_string_in_kit_name_get_success_response():
    positive_assert_number_string_in_kit_name("123")

def negative_assert_no_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))
    assert kit_response.json()["name"] == new_kit_name
    assert kit_response.status_code == 400

def test_no_kit_name_get_fail_response():
    new_kit = data.kit_body.copy()
    new_kit.pop('name')
    negative_assert_no_kit_name(new_kit)

def negative_assert_inter_number_reaches_kit_name(new_kit_name):
    current_kit_name = data.kit_body.copy()
    current_kit_name["name"] = new_kit_name
    kit_response = (sender_stand_request.post_new_client_kit(current_kit_name, auth_token))
    assert kit_response.json()["name"] == new_kit_name
    assert kit_response.status_code == 400

def test_inter_number_in_kit_name_get_fail_response():
    negative_assert_inter_number_reaches_kit_name(123)
