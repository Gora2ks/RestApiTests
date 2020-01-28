# import requests
# import jsonpath
# import json
#
#
# def test_Add_New_student():
#     global id
#     url = 'http://thetestingworldapi.com/api/studentsDetails/'
#     f = open('C:/Users/gora2/PycharmProjects/10Clouds_task/CommonModule/Request_3.json', 'r')
#     requests_json = json.loads(f.read())
#     response = requests.post(url, requests_json)
#     id = jsonpath.jsonpath(response.json(), 'id')
#     print('add new student = ', id[0])
#     print('response - ', response.text)
#
#
# def test_get_details():
#     url = 'http://thetestingworldapi.com/api/studentsDetails/' + str(id[0])
#     response = requests.get(url)
#     print('response - ', response.text)
