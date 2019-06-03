import requests
import json


def booking_request(booking_id):
    return requests.get('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id))


def get_booking_request(booking_name):
    return requests.get('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_name))


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

