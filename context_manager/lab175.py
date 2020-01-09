import os
import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        # download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == KeyError or exc_type == FileNotFoundError:
            print('error {} - {}'.format(exc_type, exc_val))
            return True
        return False


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/tempa')
        z.extract(a_file, '.', None)