import os
import functools
from datetime import datetime as dt
# ction FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:29:17
# Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:33:18
# Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:39:57
# Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:44:18


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            result = func(path)
            with open(log_file_path, 'a') as f:
                f.write('Action {} executed on {} on {} \n'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            return result
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', r'C:/temp/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', r'C:/temp/delete_file .txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')








