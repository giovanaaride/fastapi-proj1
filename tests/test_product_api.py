import requests

def test_should_get_list_of_products():
    r = requests.get('http://127.0.0.1:8000/products')
    response = r.json()
    print(response)

test_should_get_list_of_products()



    #python tests/test_product_api.py 