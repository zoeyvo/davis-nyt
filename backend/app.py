from flask import Flask, jsonify, send_from_directory, request
import os
from flask_cors import CORS
import requests

static_path = os.getenv('STATIC_PATH','static')
template_path = os.getenv('TEMPLATE_PATH','templates')

app = Flask(__name__, static_folder=static_path, template_folder=template_path)
CORS(app)

@app.route('/api/key')
def get_key():
    return jsonify({'apiKey': os.getenv('NYT_API_KEY')})

@app.route('/api/articles', methods=['GET'])
def get_articles():

    NYT_API_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    api_key = os.getenv('NYT_API_KEY')

    if not api_key:
        print("Error: NYT_API_KEY is not set")
        return jsonify({'error': 'API key not found'}), 500

    query = request.args.get('query', 'California')
    fq = f'timesTag.location:("{query}")'
    api_url = f"{NYT_API_URL}?fq={fq}&api-key={api_key}"

    print(f"Requesting URL: {api_url}")  # Log the API URL

    try:
        response = requests.get(api_url)
        print(f"Response Status Code: {response.status_code}")  # Log the status code
        print(f"Response Content: {response.text}")  # Log the response content
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles: {e}")  # Log the error
        return jsonify({'error': str(e)}), 500

@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path=''):
    if path != '' and os.path.exists(os.path.join(static_path,path)):
        return send_from_directory(static_path, path)
    return send_from_directory(template_path, 'index.html')

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)),debug=debug_mode)