import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)


def delete_file_if_exist(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


try:
    delete_file_if_exist(tmpfile_path)
    save_url_to_file(url, tmpfile_path)
    shutil.copy(tmpfile_path, file_path)
except requests.exceptions.ConnectionError:
    print('Error downloading the file. The URL {} is incorrect'.format(url))

except FileNotFoundError:
    print('File cannot be found: {}'.format(tmpfile_path))

except PermissionError:
    print('Problem accessing a file: {}'.format(file_path))

except Exception as e:
    print('General Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))
else:
    print('success')
finally:
    delete_file_if_exist(tmpfile_path)
