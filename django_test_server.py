import base64

import requests


# def test_basic_auth():
#     username = 'admin'
#     password = '540812'

#     # via auth param
#     response = requests.get('http://localhost:8000/api/lessons/', auth=(username, password))
#     print(response.status_code)
#     print(response.text)

#     credentials_string = f'{username}:{password}'
#     print(f"credentials_string: {credentials_string}")
#     encoded_credentials = credentials_string.encode('utf-8')
#     print(f"encoded_credentials bytes: {encoded_credentials}")

#     base64_credentials = base64.b64encode(encoded_credentials)
#     print(f"base64_credentials bytes: {base64_credentials}")

#     decoded_base64_credentials = base64_credentials.decode()
#     print(f"decoded_base64_credentials string: {decoded_base64_credentials}")

#     headers = {
#         'Authorization': f'Basic {decoded_base64_credentials}'
#     }
#     response = requests.get('http://localhost:8000/api/lessons/', headers=headers)
#     print(response.status_code)
#     print(response.text)
    
    
def test_token_auth():
    username = 'admin'
    password = '540812'

    response = requests.post('http://localhost:8000/api-token-auth/', json={'username': username, 'password': password})
    print(response.status_code)
    print(response.text)
    token = response.json()['token']

    headers = {
        'Authorization': f'Token {token}'
    }
    response = requests.get('http://localhost:8000/api/orders/', headers=headers)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    test_token_auth()