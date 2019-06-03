import requests


def booking_request(booking_id):
    return requests.get('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id))


def get_booking_request(booking_name):
    return requests.get('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id))


response = booking_request(10)

print('content of response')

print(response.content)

print('Header of response')

print(response.headers)

print('Status Code of response')

print(response.status_code)
