import csv
import json

import requests

from hired_score import logger


def get_csv_data(request_url):
    with requests.Session() as s:
        download = s.get(request_url)

    decoded_content = download.content.decode('utf-8')

    csv_data = csv.DictReader(decoded_content.splitlines(), delimiter=',')
    csv_data = list(csv_data)
    return csv_data


def get_candidates_info(request_url):
    logger.debug("Calling candidates API")
    try:
        candidates_api_response = {}
        response = requests.get(request_url)
        if response.status_code == 200:
            candidates_api_response = json.loads(response.text)
            logger.debug(f"Received candidates {len(candidates_api_response)} from  API")
        return candidates_api_response
    except Exception as e:
        raise f"Sorry there was an exception getting candidates data. Error is {e}"
