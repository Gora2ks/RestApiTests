# import jsonpath
# import requests
#
#
# def test_with_token_authentication():
#     # response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('Gora2ks', 'kosiv78600'))
#     # response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('testingworld'))
#     token_url = 'http://thetestingworldapi/Token'
#     data = {'grant_type': 'password', 'username': 'admin', 'password': 'gogodz'}
#     response = requests.get(token_url, data)
#     token_value = jsonpath.jsonpath(response.json(), 'access_token')
#
#     o_auth = {'Autorization': 'Bearer ' + token_value[0]}
#     API_URL = 'https://thetestingworldapi.com/api/StDetails/1104'
#     response = requests.get(API_URL, headers=o_auth )
#     print(response.text)
#
