from urllib.parse import urlparse
import socket

from api.virustotal import check_virustotal
from api.abusedb import check_abuseipdb
from api.alienvault_otx import check_otx

from processor.risk_score import calculate_risk


def analyze_url(url):

    domain = urlparse(url).netloc

    try:
        ip = socket.gethostbyname(domain)
    except:
        ip = "0.0.0.0"

    vt_detections = check_virustotal(url)

    abuse_score = 0

    if ip != "0.0.0.0":
        abuse_score = check_abuseipdb(ip)

    otx_score = check_otx(domain)

    final_score = calculate_risk(
        vt_detections,
        abuse_score,
        otx_score
    )

    print("\n========== THREAT REPORT ==========")
    print("URL:", url)
    print("IP:", ip)
    print("VirusTotal:", vt_detections)
    print("AbuseIPDB:", abuse_score)
    print("OTX:", otx_score)
    print("Risk Score:", final_score)
    print("===================================\n")

    return {
    "url": url,
    "ip": ip,
    "virustotal": vt_detections,
    "abuseipdb_score": abuse_score,
    "otx_pulses": otx_score,
    "risk_score": final_score
    }