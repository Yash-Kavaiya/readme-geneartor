from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Function to call Mistral API
def call_mistral_api(text, use_table, use_icon, add_license, add_contribution, add_author):
    mistral_url = "https://api.mistral.com/generate"  # Replace with the actual API endpoint
    api_key = "your_api_key_here"  # Replace with your API key if needed
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "use_table": use_table,
        "use_icon": use_icon,
        "add_license": add_license,
        "add_contribution": add_contribution,
        "add_author": add_author
    }
    
    response = requests.post(mistral_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json().get("readme", "")
    else:
        return "Error generating README"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_readme', methods=['POST'])
def generate_readme():
    data = request.json
    text = data.get('text', '')
    use_table = data.get('use_table', False)
    use_icon = data.get('use_icon', False)
    add_license = data.get('add_license', False)
    add_contribution = data.get('add_contribution', False)
    add_author = data.get('add_author', False)

    # Call Mistral API to generate README content
    readme_content = call_mistral_api(text, use_table, use_icon, add_license, add_contribution, add_author)
    
    return jsonify({"readme": readme_content})

if __name__ == '__main__':
    app.run(debug=True)
