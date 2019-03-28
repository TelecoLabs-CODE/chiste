import logging
import os
import urllib.parse
import requests


def get_content(path):
    """
    Read the file from the passed path or URL.
    Args:
        path:    URL or filepath.
    Returns: A string representing contents of the file.
    Raises:
        UnexpectedResponse if path is an URL which can't be reached.
        IOError or OSError if path is a filepath that can't be read.
    """
    try:
        response = requests.get(path)

        if response.status_code == 200:
            return response.content.decode()

        raise UnexpectedResponse('Unexpected response {} from {} !'.format(
            response.status_code, path
        ))
    except requests.RequestException:
        logging.debug('File path `%s` detected.', path)

    with open(path, 'r') as opened_file:
        return opened_file.read()

