import requests

# Exemplo de requisição GET
def get_request():
    url = "http://sua-api.com/get-endpoint"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

# Exemplo de requisição POST
def post_request():
    url = "http://sua-api.com/post-endpoint"
    data = {
        "key1": "valor1",
        "key2": "valor2"
    }
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

if __name__ == "__main__":
    get_request()
    post_request()
