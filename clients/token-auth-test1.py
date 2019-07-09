import requests

def client():
    # credentials = {'username': 'admin', 'password': 'admin'}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                               data=credentials)

    token_h = "Token 4c6b4637d305380d047d7b99b90e5ab71752a732"
    
    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print('Status Code: ', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()