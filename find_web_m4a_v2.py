import requests
import re
"""import pprint is json.print"""

"""webclient.headers"""
heads = {}
heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

"""song_name,song_id down ok"""
def download_madia(song_id, song_name):
    media_url = 'https://www.ximalaya.com/revision/play/v1/audio?id=' + song_id + '&ptype=1'
    response = requests.get(media_url, headers=heads)
    data = response.json()
    mp3_url = data['data']['src']
    response_copy = requests.get(mp3_url)
    with open(song_name + '.m4a', 'wb') as f:
        f.write(response_copy.content)
    print(song_name,' download is ok')

"""list down """
for range_num in range(1, 9):
    response_html = requests.get('https://www.ximalaya.com/xiangsheng/6355825/p' + str(range_num) + '/',  headers=heads)
    html_ml = re.findall('<div class="text _c2"><a title="(.*?)" href="/xiangsheng/6355825/(.*?)">', response_html.text)
    for filename in html_ml:
        print(filename[0])
    """start '#' is down list """
        #download_madia(filename[1],filename[0])