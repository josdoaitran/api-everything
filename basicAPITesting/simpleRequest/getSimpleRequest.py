import requests
import json
import jsonpath


def booking_request(booking_id):
    return requests.get('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id))


response = booking_request(10)

print('Content of response: ')

print(response.content)

print('Header of response: ')

print(response.headers)

print('Status Code of response: ')

print(response.status_code)

# parse to Json

json_response = json.loads(response.text)

print('As Json text: ')
print(json_response)

totalprice = jsonpath.jsonpath(json_response,'totalprice')

print(totalprice)
print(totalprice[0])