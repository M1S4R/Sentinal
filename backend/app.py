from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

from processor.threat_aggregator import analyze_url

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "database",
    "threat_intel.db"
)


@app.route("/")
def home():
    return "Threat Intelligence Backend Running"


@app.route("/check", methods=["POST"])
def check_website():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No JSON data received"
            }), 400

        url = data.get("url")

        if not url:
            return jsonify({
                "error": "URL is required"
            }), 400

        print("\n" + "=" * 50)
        print("Scanning URL:", url)
        print("=" * 50)

        result = analyze_url(url)

        print("Analysis Result:")
        print(result)

        connection = mysql.connector.connect(
            host="localhost",
            user="grafana",
            password="Grafana@123",
            database="threat_intelligence"
        )

        cursor = connection.cursor()

        cursor.execute(
    """
    INSERT INTO threats (
        url,
        ip,
        virustotal_score,
        abuseipdb_score,
        otx_pulses,
        risk_score
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """,
    (
        result["url"],
        result["ip"],
        result["virustotal"],
        result["abuseipdb_score"],
        result["otx_pulses"],
        result["risk_score"]
    )
)

        connection.commit()
        connection.close()

        if result["risk_score"] >= 70:

            result["message"] = "Dangerous website detected"

        elif result["risk_score"] >= 40:

            result["message"] = "Suspicious website"

        else:

            result["message"] = "Website appears safe"

        print("Final Response:")
        print(result)
        print("=" * 50 + "\n")

        return jsonify(result)

    except Exception as e:

        print("\n" + "=" * 50)
        print("BACKEND ERROR")
        print(str(e))
        print("=" * 50 + "\n")

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )