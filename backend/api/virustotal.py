import requests
import base64
from config import VIRUSTOTAL_API_KEY


def check_virustotal(url):

    try:

        url_id = base64.urlsafe_b64encode(
            url.encode()
        ).decode().strip("=")

        endpoint = (
            f"https://www.virustotal.com/api/v3/urls/{url_id}"
        )

        headers = {
            "x-apikey": VIRUSTOTAL_API_KEY
        }

        response = requests.get(
            endpoint,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:

            data = response.json()

            stats = data["data"]["attributes"][
                "last_analysis_stats"
            ]

            malicious = stats["malicious"]
            suspicious = stats["suspicious"]

            return malicious + suspicious

    except Exception as e:

        print("VirusTotal Error:", e)

    return 0