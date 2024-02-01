to Json:

```
json_response = json.loads(response.text)

print('As Json text: ')
print(json_response)
print(json_response[0])
```