# import requests
# import json
# import jsonpath
# import openpyxl
#
#
# def test_add_multiple_data():
#     API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
#     f = open('D:/Develop/Python_source/10Clouds_task/CommonModule/addNew_student.json')
#     json_request = json.loads(f.read())
#
#     # Excel Code
#     wb = openpyxl.load_workbook('D:/Develop/Python_source/10Clouds_task/CommonModule/data_xl_multiple.xlsx')
#     sh = wb['Sheet1']
#     rows = sh.max_row
#     for i in range(2, rows + 1):
#         cell_first_name = sh.cell(row=i, column=1)
#         cell_mid_name = sh.cell(row=i, column=2)
#         cell_last_name = sh.cell(row=i, column=3)
#         cell_dob = sh.cell(row=i, column=4)
#
#         # read data from the cell
#         json_request['first_name'] = cell_first_name.value
#         json_request['middle_name'] = cell_mid_name.value
#         json_request['last_name'] = cell_last_name.value
#         json_request['date_of_birth'] = cell_dob.value
#
#         response = requests.post(API_URL, json_request)
#         print(response.status_code)
#         print('response - ', response.text)
#         assert response.status_code == 201
