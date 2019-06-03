- We can use this command to make get request to API

```
import requests

def booking_request(booking_id):

    return requests.get(‘https://restful-booker.herokuapp.com/booking/{:d}/‘.format(booking_id))

response = booking_request(10)

```
- To display response and print the response content to screen.

``` print(booking_request(10).content)```

or 

``` print(response.content)```

- To get header of response
``` print(response.headers)```

- To get status code of response
``` print(response.status_code)```