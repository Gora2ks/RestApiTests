# import requests
# import jsonpath
# import json
#
#
# def test_Add_New_data():
#     url = 'http://thetestingworldapi.com/api/studentsDetails/'
#     f = open('C:/Users/gora2/PycharmProjects/10Clouds_task/CommonModule/Request_3.json', 'r')
#     requests_json = json.loads(f.read())
#     response = requests.post(url, requests_json)
#     id = jsonpath.jsonpath(response.json(), 'id')
#     print('add new student = ', id[0])
#     print('response add new data - ', response.text )
#
#     tech_api_url = 'http://thetestingworldapi.com/api/technicalskills'
#     f = open('C:/Users/gora2/PycharmProjects/10Clouds_task/CommonModule/TechDetails.json', 'r')
#     requests_json = json.loads(f.read())
#     requests_json['id'] = int(id[0])
#     requests_json['st_id'] = id[0]
#     response = requests.post(tech_api_url, requests_json)
#     print('techDetails - ', response.text)
#
#     address_api_url = 'http://thetestingworldapi.com/api/addresses'
#     f = open('C:/Users/gora2/PycharmProjects/10Clouds_task/CommonModule/address.json', 'r')
#     requests_json = json.loads(f.read())
#     requests_json['stId'] = id[0]
#     response = requests.post(address_api_url, requests_json)
#     print('address - ', response)
#
#     final_details = 'http://thetestingworldapi.com/api/FinalStudentDetails/' + str(id[0])
#     response = requests.get(final_details)
#     print('final_details - ', response.text)
