import requests
response = requests.get('https://fdfs.xmcdn.com/group67/M07/52/52/wKgMbV2sajqAc0f4AE0iSMqgYQs051.m4a')
print(response)
with open('a.m4a', 'wb') as f:
    f.write(response.content)
