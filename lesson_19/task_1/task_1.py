import requests
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
response = requests.get(url=url, params=params)
data = response.json()

photos = []
for ind, el in enumerate(data['photos']):
    for k in el:
        if k == 'img_src':
            photos.append(data['photos'][ind]['img_src'])

if photos:
    len_photos = len(photos)
    for num in range(len_photos):
        img = requests.get(photos[num])
        with open(f'nasa_photo_{num+1}.jpg', 'wb') as img_file:
            img_file.write(img.content)
