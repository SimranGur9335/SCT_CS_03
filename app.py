from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_strength(password):
    strength = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "digit": re.search(r'\d', password) is not None,
        "special": re.search(r'[^A-Za-z0-9]', password) is not None
    }

    strength = sum(criteria.values())

    if strength <= 2:
        result = "Weak"
    elif strength in [3, 4]:
        result = "Moderate"
    else:
        result = "Strong"

    return {"strength": result, "criteria": criteria}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    password = data.get('password', '')
    result = check_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
