import requests

def booking_request(booking_id):

    return requests.get('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id))

def get_booking_request(booking_name):

    return requests.get('https://restful-booker.herokuapp.com/booking/{:d}/'.format(booking_id))

print (booking_request(10).content)

