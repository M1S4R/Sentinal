import requests
from config import ABUSEIPDB_API_KEY

def check_abuseipdb(ip):

    endpoint = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    response = requests.get(
        endpoint,
        headers=headers,
        params=params
    )

    if response.status_code == 200:

        data = response.json()

        score = data["data"]["abuseConfidenceScore"]

        return score

    return 0