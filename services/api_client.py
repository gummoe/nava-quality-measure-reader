import requests
import json

MEASURES_ENDPOINT = 'https://2swdepm0wa.execute-api.us-east-1.amazonaws.com/prod/NavaInterview/measures'


class APIClient:

    @classmethod
    def post_measures_record(cls, record):
        data = json.dumps(record.to_dict())
        response = requests.post(MEASURES_ENDPOINT, data=data)

        # Just print the response status for now
        print(response.status_code)

