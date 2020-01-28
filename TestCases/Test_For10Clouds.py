# import pytest
# import requests
# import json
# import jsonpath
# # from assertpy import assert_that
#
# """
# author   : Igor Koshak
# customer :
# svn      :
# git      :
# version  : 1.0
# """
#
#
# # For Run test ans create report in allure:
# #      pytest Test_For10Clouds.py -s
# #      pytest --alluredir C:\Users\gora2\PycharmProjects\10Clouds_task\Reports
# #      allure generate --clean C:\Users\gora2\PycharmProjects\10Clouds_task\Reports
#
#
# @pytest.fixture(scope="module")
# def precondition():
#     print("Run test")
#
#
# @pytest.mark.GET
# def test_1_get_post_13_(precondition):
#     # API_URL
#     url = 'https://jsonplaceholder.typicode.com/posts/1/'
#     response = requests.get(url)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#
#
# @pytest.mark.GET
# def test_1_1_get_exact_comments_from_post_13_(precondition):
#     # API_URL
#     url = 'https://jsonplaceholder.typicode.com/posts/13/comments/'
#     payload = {'postId': 13, 'id': 61}
#     response = requests.get(url, params=payload)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#     # assert_that(response.ok, 'HTTP Request OK').is_true()
#
#     # Part two - dump mode
#     # API_URL
#     url = 'https://jsonplaceholder.typicode.com/usersposts/13/comments/'
#     r = requests.get(url)
#     packages_json = r.json()
#     packages_json = json.dumps(packages_json[60], indent=2)
#     print(packages_json)
#     print(r.status_code)
#     print(len(packages_json))
#     if response.status_code != 200:
#         print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
#         exit()
#     assert packages_json != 0
#     assert len(packages_json) == 313
#     assert response.status_code == 200
#
#
# @pytest.mark.GET_REQRES
# def test_2_get_exact_first_name_from_post_reqres(precondition):
#     # url = 'https://jsonplaceholder.typicode.com/posts/1/'
#     url = 'http://reqres.in/api/users?page=2'
#     response = requests.get(url)
#     json_response = json.loads(response.text)
#     data = jsonpath.jsonpath(json_response, 'data[0].first_name')
#     print(data[0])
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#     if response:
#         print('Response OK')
#     else:
#         print('Response Failed')
#
#
# @pytest.mark.POST
# def test_3_add_post(precondition):
#     url = 'https://jsonplaceholder.typicode.com/posts/1/comments/'
#     # url = 'http://thetestingworldapi.com/api/studentsDetails/3034'
#     f = open('C://Users//gora2//PycharmProjects//10Clouds_task//CommonModule//Request_.json', 'r')
#     json_request = json.loads(f.read())
#     response = requests.post(url, json_request)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     response_json = json.loads(response.text)
#     email = jsonpath.jsonpath(response_json, 'email')
#     print(email[0])
#     assert response_code == 201
#
#
# def test_3_1_get_new_created_post_(precondition):
#     # API_URL
#     url = 'https://jsonplaceholder.typicode.com/usersposts/13/comments/'
#     r = requests.get(url)
#     packages_json = r.json()
#     packages_json = json.dumps(packages_json[12], indent=2)
#     print(packages_json)
#     print(r.status_code)
#     print(len(packages_json))
#     assert packages_json != 0
#     assert len(packages_json) == 291
#
#
# @pytest.mark.POST_REQRES
# def test_4_add_post_reqres(precondition):
#     # url = 'https://jsonplaceholder.typicode.com/posts/1/comments/'
#     url = 'http://reqres.in/api/users'
#     f = open('C://Users//gora2//PycharmProjects//10Clouds_task//CommonModule//Request_5.json', 'r')
#     json_input = f.read()
#     requests_json = json.loads(json_input)
#     response = requests.post(url, requests_json)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#
#
# @pytest.mark.PUT
# def test_5_update_post(precondition):
#     url = 'https://jsonplaceholder.typicode.com/posts/1/'
#     # url = 'http://thetestingWorldapi.com/api/studentsDetails/3034'
#     f = open('C://Users//gora2//PycharmProjects//10Clouds_task//CommonModule//Request_1.json', 'r')
#     json_request = json.loads(f.read())
#     response = requests.put(url, json_request)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#
#
# @pytest.mark.PUT_REQRES
# def test_6_update_post_reqres(precondition):
#     # url = 'https://jsonplaceholder.typicode.com/posts/1/'
#     # url = 'http://thetestingWorldapi.com/api/studentsDetails/3034'
#     url = 'http://reqres.in/api/users/2'
#     f = open('C://Users//gora2//PycharmProjects//10Clouds_task//CommonModule//Request_6.json', 'r')
#     json_request = json.loads(f.read())
#     response = requests.put(url, json_request)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#
#     # Parse response Content
#     response_json = json.loads(response.text)
#     update_comm = jsonpath.jsonpath(response_json, 'updatedAt')
#     assert (update_comm[0])
#     print(update_comm)
#
#
# @pytest.mark.DELETE
# def test_7_delete_object(precondition):
#     # url = 'https://jsonplaceholder.typicode.com/posts/1/'
#     url = 'https://jsonplaceholder.typicode.com/posts/1'
#     response = requests.delete(url)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 204
#
#
# @pytest.mark.GET_DELETE_OBJECT
# def test_7_1_get_deleted_object(precondition):
#     url = 'https://jsonplaceholder.typicode.com/posts/1'
#     response = requests.get(url)
#     json_response = response.text
#     print(json_response)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#
#
# @pytest.mark.DELETE_REQRES
# def test_8_delete_object_reqres(precondition):
#     # url = 'https://jsonplaceholder.typicode.com/posts/1/'
#     url = 'http://reqres.in/api/users/2'
#     response = requests.delete(url)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
#
#
# @pytest.mark.DELETE_REQRES
# def test_9_delete_object_reqres___(precondition):
#     url = 'https://jsonplaceholder.typicode.com/posts/1/'
#     # url = 'http://reqres.in/api/users/2'
#     response = requests.delete(url)
#     print(response.text)
#     response_code = response.status_code
#     print(response_code)
#     assert response_code == 200
