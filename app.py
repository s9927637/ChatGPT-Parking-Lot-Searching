from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    # Handle Dialogflow webhook request here
    req = request.get_json(force=True)
    print('Dialogflow request:', req)

    # Process the request and prepare the response
    response = {
        "fulfillmentText": "This is a sample response from the webhook."
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
