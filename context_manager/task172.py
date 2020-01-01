import os
import zipfile
import requests


class UnzipFileFromWeb:
    def __init__(self, url, temp_path):
        self.url = url
        self.temp_path = temp_path
        self.save_path = os.path.join(self.temp_path, self.url.split('/')[-1])

    def __enter__(self):
        r = requests.get(self.url)
        with open(self.save_path, 'wb') as f:
            f.write(r.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.save_path)

    def unzip(self):
        with zipfile.ZipFile(self.save_path, 'r') as zip_ref:
            zip_ref.extractall(path=self.temp_path)


with UnzipFileFromWeb(r'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', r'c:/temp') as f:
    f.unzip()