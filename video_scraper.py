import requests
import os
import glob


# 1.下載m3u8檔案
response = requests.get(
    'https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/ef3d1a91-f65b-306c-a42b-6c665425a61a/2022-06-24/03-58-35/4956d0df-986a-5af0-9376-6bf131ec2d5f/stream_960x540x1035_v2.m3u8')

if not os.path.exists('video'):
    os.mkdir('video')

with open('video\\trailer.m3u8', 'wb') as file:
    file.write(response.content)

# 2.下載ts檔案
ts_url_list = []
with open('video\\trailer.m3u8', 'r', encoding='utf-8') as file:
    contents = file.readlines()
    base_url = 'https://edgecast-cf-prod.yahoo.net/cp-video-transcode/production/ef3d1a91-f65b-306c-a42b-6c665425a61a/2022-06-24/03-58-35/4956d0df-986a-5af0-9376-6bf131ec2d5f/'

    for content in contents:
        if content.endswith('ts\n'):
            ts_url = base_url + content.replace('\n', '')
            ts_url_list.append(ts_url)

for index, url in enumerate(ts_url_list):
    ts_response = requests.get(url)

    with open(f'video\\{index+1}.ts', 'wb') as file:
        file.write(ts_response.content)

# 3.合併ts檔案
ts_files = glob.glob('video\\*.ts')

with open('video\\trailer.mp4', 'wb') as file:
    for ts_file in ts_files:
        file.write(open(ts_file, 'rb').read())
