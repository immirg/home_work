import os
import requests

# python app.py
url = 'http://127.0.0.1:8080'


def download_image_from_url(image_name, image_url, headers):
    response = requests.get(image_url, headers=headers)
    if response.status_code == 200:
        with open(image_name, 'wb') as f:
            f.write(response.content)
            print(f'Изображение скачено с интернета и сохранено локально успешно. Статус код {response.status_code}')
            return True
    else:
        print(f'Ошбика загрузки изображения с интернета. Статус код {response.status_code}')
        return False


def upload_image_to_server(image_name='image.jpg'):
    with open(image_name, 'rb') as f:
        files = {'image': f}
        r = requests.post(url=f'{url}/upload', files=files)
        if r.status_code == 201:
            print(f'Файл загружен на сервер успешно. Статус код {r.status_code}')
            return True
        else:
            print(f'Ошбика загрузки фото на сервер. Статус код {r.status_code}')
            return False


def fetch_image_from_server(image_name='image.jpg'):
    img_url = f'{url}/image/{image_name}'
    headers_img = {'Content-Type': 'image'}
    response_jpg = requests.get(img_url, headers=headers_img)
    if response_jpg.status_code == 200:
        print(f'Изображение успешно загружено с сервера. Статус код {response_jpg.status_code}')
        return True
    else:
        print(f'Изображение не было загружено с сервера. Статус код {response_jpg.status_code}')
        return False


def delete_image_from_server(image_name='image.jpg'):
    del_img = f'{url}/delete/{image_name}'
    resource_del = requests.delete(del_img)
    if resource_del.status_code == 200:
        print(f'Изображение было успешно удалено с сервера. Статус код {resource_del.status_code}')
        return True
    else:
        print(f'Ошибка изображение не было удалено с сервера. Статус код {resource_del.status_code}')
        return False


def main():
    image_url = 'https://web-shturman.com.ua/wp-content/uploads/2023/12/sho-take-kosmos.jpg'
    image_name = 'image.jpg'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    print("1. Скачивание изображения из интернета...")
    if not download_image_from_url(image_name, image_url, headers):
        return

    print("2. Загрузка изображения на сервер...")
    if not upload_image_to_server(image_name=image_name):
        return

    print("3. Получение изображения с сервера...")
    if not fetch_image_from_server(image_name=image_name):
        return

    print("4. Удаление изображения с сервера...")
    if not delete_image_from_server(image_name=image_name):
        return False
    else:
        return True


all_operations = main()
if all_operations:
    print("5. Удаление изображения с сохраненного локально...")
    os.remove(os.path.abspath('image.jpg'))
    print("Изображение сохраненное локально было удалено")

