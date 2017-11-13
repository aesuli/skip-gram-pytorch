import os
import urllib.request


def download_file(url, local_file, force=False):
    """
    Helper function to download a file and store it locally
    """
    if not os.path.exists(local_file) or force:
        print('Downloading')
        with urllib.request.urlopen(url) as opener, \
                open(local_file, mode='wb') as outfile:
            outfile.write(opener.read())
    else:
        print('Already downloaded')
