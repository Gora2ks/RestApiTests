import requests
import json
import jsonpath
import openpyxl
from DataDrivenTesting import Library


def test_add_multiple_data():
    API_URL = 'http://thetestingworldapi.com/api/studentsDetails'
    f = open('D:/Develop/Python_source/10Clouds_task/CommonModule/addNew_student.json')
    json_request = json.loads(f.read())

    obj = Library.Common('D:/Develop/Python_source/10Clouds_task/CommonModule/data_xl_multiple.xlsx', 'Sheet1')
    column = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_name()

    # Excel Code
    for i in range(2, row + 1):
        update_json_request = obj.update_request_with_date(i, json_request, keylist)
        response = requests.post(API_URL, update_json_request)
        print(response)
