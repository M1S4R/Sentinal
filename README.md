# Sentinel AI - Live Threat Intelligence Browser Extension

Sentinel AI is a real-time threat intelligence browser extension that analyzes websites using multiple threat intelligence sources and calculates a risk score to help users identify malicious or suspicious websites before interacting with them.

---

## Features

- Real-time website scanning
- VirusTotal integration
- AbuseIPDB integration
- AlienVault OTX integration
- Risk score calculation
- Automatic website monitoring
- MySQL database logging
- Grafana dashboard visualization
- Browser notifications
- Protection ON/OFF toggle
- Scan history

---

## Architecture

```
Chrome Extension
        │
        ▼
    Flask Backend
        │
 ┌──────┼────────┐
 │      │        │
 ▼      ▼        ▼
VirusTotal AbuseIPDB AlienVault OTX
        │
        ▼
 Risk Score Engine
        │
        ▼
   MySQL Database
        │
        ▼
 Grafana Dashboard
```

---

## Project Structure

```
Live-Threat-Intelligence-Extension/

│
├── backend/
│   ├── api/
│   │   ├── virustotal.py
│   │   ├── abusedb.py
│   │   └── alienvault_otx.py
│   │
│   ├── processor/
│   │   ├── threat_aggregator.py
│   │   └── risk_score.py
│   │
│   ├── database/
│   │   └── threat_intel.db
│   │
│   ├── config.py
│   └── app.py
│
├── extension/
│   ├── background/
│   ├── popup/
│   ├── content/
│   ├── icons/
│   └── manifest.json
│
├── dashboard/
│
└── README.md
```

---

## Technologies Used

- Python
- Flask
- JavaScript
- HTML5
- CSS3
- MySQL
- Grafana
- Chrome Extension Manifest V3
- REST APIs

---

## Threat Intelligence Sources

### VirusTotal
Checks URLs against multiple antivirus engines.

### AbuseIPDB
Retrieves IP reputation and abuse confidence scores.

### AlienVault OTX
Collects threat intelligence pulses and indicators of compromise.

---

## Risk Score

The overall risk score is calculated using data from all integrated threat intelligence sources.

| Source | Weight |
|---------|--------|
| VirusTotal | 50 |
| AbuseIPDB | 30 |
| AlienVault OTX | 20 |

Final Risk Score ranges from **0–100**.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/M1S4R/Live-Threat-Intelligence-Extension.git

cd Live-Threat-Intelligence-Extension
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

Linux

```bash
source venv/bin/activate
```

Windows

```cmd
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Keys

Edit:

```
backend/config.py
```

```python
VIRUSTOTAL_API_KEY = "YOUR_API_KEY"

ABUSEIPDB_API_KEY = "YOUR_API_KEY"

ALIENVAULT_API_KEY = "YOUR_API_KEY"
```

### Start Backend

```bash
cd backend

python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

### Load the Extension

1. Open Chrome
2. Navigate to:

```
chrome://extensions
```

3. Enable **Developer Mode**
4. Click **Load Unpacked**
5. Select the `extension/` folder

---

## Grafana Dashboard

Start Grafana:

```bash
sudo systemctl start grafana-server
```

Open:

```
http://localhost:3000
```

Configure the MySQL data source and create dashboards for:

- Total Websites Scanned
- Risk Score Distribution
- High Risk Websites
- Most Frequently Visited Domains
- Threat Timeline

---

## Example Response

```json
{
    "url": "https://chatgpt.com",
    "ip": "172.64.155.209",
    "virustotal": 0,
    "abuseipdb_score": 0,
    "otx_pulses": 50,
    "risk_score": 20,
    "message": "Website appears safe"
}
```

---


----

## Author

Mohammed Misfar

GitHub: https://github.com/M1S4R
