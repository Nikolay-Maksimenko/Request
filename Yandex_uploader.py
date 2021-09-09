import requests
from pathlib import Path

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {'Authorization': 'OAuth ' + self.token}

    def upload(self, path_to_file):
        """Метод загруджает файлы по списку file_list на яндекс диск"""

        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        params = {'path': '/Upload_file/' + path_to_file.name}
        # получаем url для загрузки:
        get_upload_url = requests.get(url, headers=self.headers, params=params)
        if not str(get_upload_url.status_code).startswith('2'):
            print(get_upload_url.json().get('message'))
        else:
            upload_url = get_upload_url.json().get('href')
            with open(path_to_file, 'rb') as file:
                # загружаем файл по полученному url:
                upload_file = requests.put(upload_url, file, headers=self.headers)
                if not str(upload_file.status_code).startswith('2'):
                    print(upload_file.json().get('message'))
                else:
                    print(f'файл был успешно загружен')
        return

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = Path('/home/nikolay/Документы/project.py')
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)