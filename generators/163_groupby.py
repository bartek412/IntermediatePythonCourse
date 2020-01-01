import os
import itertools as it


def scantree(path):
    with os.scandir(path) as itr:
        for entry in itr:
            if entry.is_dir():
                yield entry
                yield from scantree(entry.path)
            else:
                yield entry


listing = scantree('c:/temp')

# for item in listing:
#     print('Dir ' if item.is_dir() else 'File ', item.path)

listing = sorted(listing, key=lambda x: x.is_dir())

for key, values in it.groupby(listing, lambda x: x.is_dir()):
    print('Dirs:' if key else 'Files:', len(list(values)))
