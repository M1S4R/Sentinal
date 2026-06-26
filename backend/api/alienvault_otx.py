import requests
from config import ALIENVAULT_API_KEY

def check_otx(domain):

    endpoint = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/general"

    headers = {
        "X-OTX-API-KEY": ALIENVAULT_API_KEY
    }

    response = requests.get(
        endpoint,
        headers=headers
    )

    if response.status_code == 200:

        data = response.json()

        pulse_count = data["pulse_info"]["count"]

        return pulse_count

    return 0