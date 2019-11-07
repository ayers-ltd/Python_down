import requests
import pprint
song_id = '221393810'
headerss = {
	'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
media_url = 'https://www.ximalaya.com/revision/play/v1/audio?id=' + song_id + '&ptype=1'
heads = {}
heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
response = requests.get(media_url , headers=heads)
#print(response.text)
data = response.json()
#print(data)
#pprint.pprint(data['data'])
pprint.pprint(data['data']['src'])
mp3_url = (data['data']['src'])
mp3_data = requests.get(mp3_url)
with open('b.m4a', 'wb') as f:
    f.write(mp3_data.content)
