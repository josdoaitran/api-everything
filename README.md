# API-AutomationTesting-Python
API-AutomationTesting-Python


## 1. Basic API testing

API testing: to perform api testing we should use API client: Postman, SoapUI, cURL in command line, ...

### Install and set up

Python 3

- Install request package:

```pip install requests```
- Install json package

```pip install json```
- Install jsonpath package

```pip install jsonpath```


API document site: https://restful-booker.herokuapp.com/apidoc/index.html

## 2. Get method

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

## 3. Post method


```

```


Testing Practice Websites:

1. https://restful-booker.herokuapp.com
2. https://reqres.in/
