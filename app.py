from flask import Flask, jsonify, Response, make_response, request
import requests
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)

@app.route("/api/v1/get_UDID_details", methods=["POST"])
def get_UDID_details():
    try:
        url = "https://swavlambancard.gov.in/api/rest/trackapplication"
        UDID = request.json.get("UDID_Number")
        session = requests.Session()

        postBody = {
            "udid_number": UDID
        }

        response = session.post(url, json=postBody)

        return jsonify(response.json())
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching UDID Number Details"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=5001)