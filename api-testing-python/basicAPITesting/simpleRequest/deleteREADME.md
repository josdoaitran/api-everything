```
import requests

url = "https://reqres.in/api/users/{:d}"

def delete_booking(booking_id):

    return requests.delete(url.format(booking_id))

response = delete_booking(3)

print(response.content)
print(response.status_code)
```