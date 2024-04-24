from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'WAPPALYZER_API_KEY' #wappalyzer api key
WAPPALYZER_API_ENDPOINT = 'https://api.wappalyzer.com/v2/lookup/'

@app.route('/analyze', methods=['GET'])
def analyze_url():
    url = request.args.get('url')
    print("Url is:-",url)
    
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    headers = {
        'x-api-key': API_KEY
    }

    try:
        # check_balance_url = "https://api.wappalyzer.com/v2/credits/balance/"
        # balance_response = requests.get(check_balance_url, headers=headers)
        # print("balance is:-",balance_response.text)
        print("Final url is:-",f"{WAPPALYZER_API_ENDPOINT}?urls={url}")
        response = requests.get(f"{WAPPALYZER_API_ENDPOINT}?urls={url}", headers=headers)
        print("Response is:- ",response.text)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to retrieve data', 'status_code': response.status_code}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
